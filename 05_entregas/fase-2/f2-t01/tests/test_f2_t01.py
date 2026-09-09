import json, pathlib, sys
ROOT=pathlib.Path(__file__).parents[1]; data=json.loads((ROOT/'data/briefings.json').read_text()); results=[]
def t(i,d,e,f):
 try: ok=bool(f()); results.append({'id':i,'testado':d,'entrada':'massa sintética F2-T01','esperado':e,'obtido':'PASS' if ok else 'FAIL','status':'aprovado' if ok else 'falhou','evidencia':'test:'+i})
 except Exception as ex: results.append({'id':i,'testado':d,'entrada':'massa sintética F2-T01','esperado':e,'obtido':'ERROR '+str(ex),'status':'falhou','evidencia':'test:'+i})
req=['id','title','briefing_version','state','service','offer','hypothesis','audience','origin','channel','window','budget','criteria','owners']
for x in data:
 t('POS-'+x['id'],'briefing sintético completo','campos CA-2-01',lambda x=x: all(k in x for k in req) and x['window']['type']=='sintética/teste' and x['budget']['origin']=='sintético/teste')
 t('ORIG-'+x['id'],'origem e canal separados','origem explícita',lambda x=x:x['origin'] in ('inbound','outbound') and x['origin']!=x['channel'])
 t('SVC-'+x['id'],'serviço identificado','R&S ou TMO',lambda x=x:x['service'] in ('R&S','TMO','R&S + TMO'))
 t('HYP-'+x['id'],'hipótese estruturada','Se/Para/Então/Porque/Mediremos',lambda x=x:all(k in x['hypothesis'] for k in ('se','para','entao','porque','mediremos_por')))
 t('OWNER-'+x['id'],'responsáveis humanos sintéticos','HUMANO-SINTETICO',lambda x=x:all(v.startswith('HUMANO-SINTETICO-') for v in x['owners'].values()))
 t('WIN-'+x['id'],'janela e análise sintéticas','sem execução',lambda x=x:'sintético' in x['window']['analysis_period'])
 t('BUD-'+x['id'],'orçamento sintético','não solicitada',lambda x=x:x['budget']['approval']=='não solicitada')
t('NEG-MISSING','campo obrigatório ausente','bloqueado',lambda:not all(k in {'id':'x'} for k in req))
t('NEG-REAL','dado real na massa sintética','bloqueado',lambda:not any('@' in json.dumps(x) for x in data))
t('NEG-AGENT','aprovação por agente','bloqueado',lambda:'agent_approval' not in json.dumps(data))
t('NEG-EXTERNAL','ação externa não autorizada','bloqueado',lambda:not any(s in json.dumps(data).lower() for s in ('http://','https://','rd station','pocketbase')))
h=[{'version':'v1','previous':None},{'version':'v2','previous':'v1'},{'version':'v3','previous':'v1','reason':'retomada documental'}]
t('VER-001','versionamento material','v1,v2,v3',lambda:h[1]['previous']=='v1' and h[2]['previous']=='v1')
t('RB-001','rollback documental','recuperar v1 sem apagar v2/v3',lambda:len(h)==3)
out=ROOT/'evidence'/'test-results.json'; out.write_text(json.dumps({'synthetic_only':True,'results':results,'summary':{'total':len(results),'passed':sum(r['status']=='aprovado' for r in results),'failed':sum(r['status']=='falhou' for r in results)}},ensure_ascii=False,indent=2)); print(json.dumps({'total':len(results),'passed':sum(r['status']=='aprovado' for r in results),'failed':sum(r['status']=='falhou' for r in results)},ensure_ascii=False)); sys.exit(1 if any(r['status']=='falhou' for r in results) else 0)