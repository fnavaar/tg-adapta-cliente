# Estado atual — Adapta Cliente

- fase: 3
- champion: João Paulo
- task_elegivel: F3-T01
- tasks_fase_3: 0/13 concluídas (8 originais + F3-T09..T13 publicadas em 22/10/2026); F3-T01 em andamento; ordem recomendada: F3-T01 → T09 → T10 → T11 → T12 → T13 → T02 → T03..T08
- prazo_referencia: ajustável pelo Champion (referência inicial 30/09/2026 vencida; decisão Navaar 07/10/2026 — sem trava de prazo)
- ambiente: Skip (GoSkip + SkipCloud), conforme regra geral do consultor
- etapa: concluida (E2 da F3-T01 — segregação origem_dado; F3-T01 segue em andamento com etapas bloqueadas por D4/D5/D6)
- autorizacao_implementacao: confirmada 2026-10-22 15:59 — "Autorizo a E2 — pode implementar" (mensagem do Champion/owner após relatório de status)
- teste_humano: aprovado 2026-10-23 11:47 — "Confirmo o aceite — concluir a E2 e registrar" (print do painel oficial: selo de segregação, 8 cards em 0, modo homologação com 10 preservados)
- verificacao_automatica: passou — QA Skip (setup/static/build/integrations OK; v0.0.97 ref 08c6e6a e v0.0.98 ref 2aab7da); banco conferido via API: total 10, sintetico 10, producao 0, vazio 0; migration 0021_origem_dado applied
- aprendizado: capturado:06_notas/aprendizado-continuo/controle.md (AP-2026-10-22-1600; fechamento 23/10 sem sinal adicional)
- bloqueios: B3-META-01 (alterado 22/10: só métricas de campanha pela SPEC-F3-006), B3-META-LEITOR (novo, antes da F3-T12), B3-LGPD-01 (formalizado), B3-ID-01, B3-MET-01, B3-RACI-01, B3-DHO-01
- protocolo_interacao: vigente desde 22/10/2026 — explicar fase/task atual/próxima, combinar cada passo, pedir para conferir no Skip, fechar com resumo (CLAUDE.md)
- projeto_skip: "repositório adapta" (GitHub talentgroupepress-web); nenhum dado em outro projeto Skip
- ultima_acao: 2026-10-23 — E2 concluída: revalidação do zero pelo ETHOS (banco 10/10/0/0, migration applied, núcleo+painel presentes no Skip 51414 v0.0.98), aceite humano registrado, changelog/fase/STATUS/estado atualizados. Implementação em 22/10: migration 0021_origem_dado (campo select {sintetico, producao} em demandas + backfill dos 10 registros como sintetico, não destrutiva, com rollback), núcleo de consulta src/lib/origem-dado.ts (filtroOrigemDado, resumirSegregacao, filtrarPorOrigem, normalizarOrigemDado; default seguro: sem campo = sintetico) e painel oficial Index.tsx exibindo somente producao com selo de segregação e reconciliação/opções filtradas por producao.
- proxima_acao: iniciar F3-T09 (diagnóstico somente leitura) por decisão do Champion; F3-T01 segue aberta com E2-coleções bloqueada por D4, E5 por D4/D5 e E6 por D6 — emendas do consultor pendentes.

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