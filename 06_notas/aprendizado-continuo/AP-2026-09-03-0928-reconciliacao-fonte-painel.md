# AP-2026-09-03-0928 — Reconciliação deve comparar IDs da fonte

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F1-T06 / SPEC-F1-002
- Sinal: a primeira versão do painel usava diferença visual estática; a correção passou a consultar a fonte com os mesmos filtros e comparar os IDs retornados.
- Evidência: Skip v0.0.31; reconciliação painel/fonte com diferença 0 nos filtros testados; evidência em 04-fase-atual/pipeline-f1-f1-t06.md.
- Regra reutilizável: uma visão derivada só é reconciliada quando quantidade e identidade dos registros coincidem com consulta equivalente da fonte.
- Quando aplicar: em qualquer painel ou relatório derivado da collection operacional.
- Quando não aplicar: não substituir a fonte nem usar a reconciliação para criar regra de negócio ou identidade técnica.
- Confiança: alta — confirmada por testes de UI e consultas de leitura.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
