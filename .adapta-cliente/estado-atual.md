# Estado atual — Adapta Cliente

- fase: 3
- champion: João Paulo
- task_elegivel: F3-T01
- tasks_fase_3: 0/8 concluídas; F3-T01 elegível, F3-T02..T08 bloqueadas por dependências
- prazo_referencia: ajustável pelo Champion (referência inicial 30/09/2026 vencida; decisão Navaar 07/10/2026 — sem trava de prazo)
- ambiente: Skip (GoSkip + SkipCloud), conforme regra geral do consultor
- etapa: aguardando_teste_humano (E2 — migration origem_dado; autorização do Champion/owner em 22/10/2026: "Autorizo a E2 — pode implementar")
- autorizacao_implementacao: confirmada 2026-10-22 15:59 — "Autorizo a E2 — pode implementar" (mensagem do Champion/owner após relatório de status)
- teste_humano: pendente (roteiro entregue ao Champion em 22/10/2026)
- verificacao_automatica: passou — QA Skip (setup/static/build/integrations OK; v0.0.97 ref 08c6e6a e v0.0.98 ref 2aab7da); banco conferido via API: total 10, sintetico 10, producao 0, vazio 0; migration 0021_origem_dado applied
- aprendizado: capturado:06_notas/aprendizado-continuo/controle.md (AP-2026-10-22-1600)
- bloqueios: B3-META-01, B3-ID-01, B3-MET-01, B3-RACI-01, B3-DHO-01
- ultima_acao: 2026-10-22 — E2 implementada com autorização do Champion: migration 0021_origem_dado (campo select {sintetico, producao} em demandas + backfill dos 10 registros como sintetico, não destrutiva, com rollback), núcleo de consulta src/lib/origem-dado.ts (filtroOrigemDado, resumirSegregacao, filtrarPorOrigem, normalizarOrigemDado; default seguro: sem campo = sintetico) e painel oficial Index.tsx exibindo somente producao com selo de segregação e reconciliação/opções filtradas por producao.
- proxima_acao: teste humano do Champion no painel (10 registros saem do painel oficial; selo "Painel oficial — somente origem_dado=producao" visível; modo homologação preservado). Após aceite: E3 (painéis com filtro) aguarda autorização. F3-T01 segue com E2 (coleções) bloqueada por D4, E5 por D4/D5 e E6 por D6 — emendas do Navaar pendentes.

## Defaults conservadores da F3-T01 (protocolo anti-trava — Constituição §Dúvidas e insumos, 07/10/2026)

Adotados pelo Champion em 09/10/2026 enquanto as emendas não chegam; nenhuma DÚVIDA é considerada resolvida:

- **D1 (vocabulário R&S/Alocação/SOS):** fixtures usam exclusivamente R&S / TMO / R&S + TMO como valores de `oferta_servico` (decisão Champion 07/10, changelog); "R&S/Alocação/SOS" na SPEC é lido como descrição da operação que devolve o retorno, não valor de campo. SOS = Serviço Orientado a Substituições, dentro do TMO.
- **D2 (área + lista v1):** área = departamento funcional do cargo; lista fechada v1 com 13 áreas (TI, Comercial/Vendas, Logística/Supply Chain, Projetos/PMO, Engenharia/Manutenção, Financeiro/Contábil, Administrativo, Marketing, Recursos Humanos, Operações/Produção, Educacional/Acadêmico, Auditoria/Riscos, Laboratorial/Saúde); "Não informado" = condição provisória, não área definitiva (DECISÃO 08/10).
- **D3 (RN-F3-002 × Não informado):** área "Não informado" não bloqueia avanço e não gera pendência automática nova; confirmação humana responsável (DECISÃO 08/10).
- **D4 (persistência do estado do retorno):** SEM default seguro — E2 (migrations) BLOQUEADA até emenda ou decisão do Champion sobre onde "estado do retorno" persiste (campo da coleção × atributo do log).
- **D5 (encerramento da substituição):** SEM default aprovado — "Substituição encerrada" NÃO aprovado; cenários de substituição nos fixtures param em "Substituição em andamento" com motivo; E5 bloqueada até emenda.
- **D6 (regras de recuperação/RN-F3-004):** SEM default na SPEC — regras do Champion de 24/09 (3 tentativas, 90 dias corridos, sugestão de sem timing com confirmação do Comercial, recusa=perdido) NÃO constam da RN-F3-004; E6 bloqueada até emenda; fixture STUCK registra apenas pendência com dono provisório conforme RN-F3-004 vigente.

## DÚVIDAs documentais pendentes (lote único ao consultor)

D1–D6 conforme 06_notas/f3-t01-pacote-harmonizacoes-2026-10-08.md e entradas no changelog de 07–08/10/2026. Nenhuma resolvida; aguardando emenda datada do consultor (Navaar).
