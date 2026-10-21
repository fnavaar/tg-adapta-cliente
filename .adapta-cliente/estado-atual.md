# Estado atual — Adapta Cliente

- fase: 3
- champion: João Paulo
- task_elegivel: F3-T01
- tasks_fase_3: 0/8 concluídas; F3-T01 elegível, F3-T02..T08 bloqueadas por dependências
- prazo_referencia: ajustável pelo Champion (referência inicial 30/09/2026 vencida; decisão Navaar 07/10/2026 — sem trava de prazo)
- ambiente: Skip (GoSkip + SkipCloud), conforme regra geral do consultor
- autorizacao_liberacao: confirmada por Navaar em 2026-09-23 — "quero que as tasks estejam liberadas"
- autorizacao_implementacao: segue o fluxo normal — o Champion autoriza cada task (uma por vez); sem trava documental pendente desde 07/10/2026
- teste_humano: não aplicável à liberação documental; obrigatório ao fim de cada task executada
- bloqueios: B3-META-01, B3-ID-01, B3-MET-01, B3-RACI-01, B3-DHO-01
- ultima_acao: 2026-10-21 — Champion aprovou e registrou a DECISÃO de segregação sintético×produção no ETHOS 51414 (campo origem_dado {sintetico, producao}; indicadores oficiais só produção; modo homologação preservado; dedup por identidade composta, não só e-mail; LGPD pendente antes de dado real; B3-MET-01 mantido) — changelog commit 2409160, verificado byte a byte; escopo do ciclo: apenas documental, nenhuma migration/coleção/dashboard/publicação. Antes disso (20/10): inventário real do 51414 concluído (10 registros sintéticos em demandas, demais coleções vazias).
- proxima_acao: aguardar autorização expressa do Champion para a E2 (migration não destrutiva origem_dado + backfill dos 10 + núcleo de consulta com filtro); E2 não executada. Em paralelo, F3-T01 segue com E2 (coleções) bloqueada por D4, E5 por D4/D5 e E6 por D6 — emendas do Navaar pendentes.

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
