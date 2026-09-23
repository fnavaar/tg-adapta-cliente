# Matriz de rastreabilidade — Fase 2

| Origem do escopo | SPEC | Critério de aceite | Task(s) | Prova/Evidência | Estado |
|---|---|---|---|---|---|
| Fase 2; C-02; DC-001/DC-004; G-006 | F2-001 | CA-2-01..03 | F2-T01, F2-T02 | Briefings, bloqueios, versões e referência de aprovação | F2-T01 e F2-T02 concluídas e validadas |
| Fase 2; C-01/C-04; DC-004; G-001/G-009 | F2-002 | CA-2-04..06 | F2-T03, F2-T04 | Relatório, IDs, reconciliação e lacunas | F2-T03 e F2-T04 concluídas e validadas; 3/3 testes humanos T04, 7/7 determinísticos e replay idempotente |
| Fase 2; C-02/C-04; DC-007 | F2-003 | CA-2-07..09 | F2-T05, F2-T06 | Decisão humana e histórico de versões | F2-T05 e F2-T06 concluídas e validadas em 2026-09-21 |
| Fase 2; DC-003; G-009 | F2-004 | CA-2-10..12 | F2-T07, F2-T08 | Checklist, fallback, falhas simuladas | F2-T07 e F2-T08 concluídas e validadas em 2026-09-21; T08 bateria humana 5/5 |
| Fase 2; DC-003; G-009 | F2-004 | CA-2-11..12 | F2-T09 | Consulta Meta de leitura, reconciliação e erro real | Concluída e validada em 2026-09-23 — leitura real limitada (TalentGroup_01, 15–21/09, campos do contrato, HTTP 200), prova 10/10, teste humano aprovado (PDF 5 págs); CA-2-11 e CA-2-12 (real) atendidos. Histórico preservado: a task nasceu condicional/não elegível (2026-09-21), foi autorizada via gates 1–5 (2026-09-22), ficou bloqueada por dependência externa do conector (2026-09-22) e foi retomada/concluída após a conexão (2026-09-23) |

## Ressalvas de rastreabilidade

- A divergência de numeração entre `fase.md`/esta matriz e as SPECs foi encerrada em 2026-09-17; a numeração CA-2-01..12 e RN-F2-001..014 é única e coerente.
- A pendência de identidade técnica/multi-fonte permanece; T04, T08 e T09 usam `record_id` somente no escopo da fonte declarada.
- `META-F2-001` foi aprovado humanamente com `fallback_manual`; o registro `META-F2-002` (T09) classifica a modalidade como `integrada_validada` em dry-run, com leitura real limitada registrada — sem escrita e sem alteração de campanha/orçamento/criativo.
- `META-F2-MANUAL-001` foi processado somente como lote sintético em dry-run; os erros da T08 são simulados, não respostas reais.
- Histórico da F2-T09 preservado: a task esteve condicional/não elegível (2026-09-21), foi autorizada via gates 1–5 (2026-09-22), bloqueada por dependência externa do conector Meta (2026-09-22, "No connected account") e concluída/validada após a conexão do conector (2026-09-23). O estado final é concluída; o histórico de bloqueio permanece registrado no `changelog.md` e em `05_entregas/fase-2/f2-t09/relatorio-fechamento.md`.
- Pendências de governança da T09 preservadas para a próxima fase: o principal conectado no conector é o owner nominal (João Paulo Oliveira), não o leitor dedicado do gate 2; agência externa mantém escrita na conta de anúncios; nenhuma relação estrutural `demandas` ↔ `experimentos_f2` foi criada.
