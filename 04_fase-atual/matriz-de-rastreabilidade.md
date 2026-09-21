# Matriz de rastreabilidade — Fase 2

| Origem do escopo | SPEC | Critério de aceite | Task(s) | Prova/Evidência | Estado |
|---|---|---|---|---|---|
| Fase 2; C-02; DC-001/DC-004; G-006 | F2-001 | CA-2-01..03 | F2-T01, F2-T02 | Briefings, bloqueios, versões e referência de aprovação | F2-T01 e F2-T02 concluídas e validadas |
| Fase 2; C-01/C-04; DC-004; G-001/G-009 | F2-002 | CA-2-04..06 | F2-T03, F2-T04 | Relatório, IDs, reconciliação e lacunas | F2-T03 e F2-T04 concluídas e validadas; 3/3 testes humanos T04, 7/7 determinísticos e replay idempotente |
| Fase 2; C-02/C-04; DC-007 | F2-003 | CA-2-07..09 | F2-T05, F2-T06 | Decisão humana e histórico de versões | F2-T05 e F2-T06 concluídas e validadas em 2026-09-21 |
| Fase 2; DC-003; G-009 | F2-004 | CA-2-10..12 | F2-T07, F2-T08 | Checklist, fallback, falhas simuladas | F2-T07 e F2-T08 concluídas e validadas em 2026-09-21; T08 bateria humana 5/5 |
| Fase 2; DC-003; G-009 | F2-004 | CA-2-11..12 | F2-T09 | Consulta Meta de leitura, reconciliação e erro real | Condicional — não elegível |

## Ressalvas de rastreabilidade

- A divergência de numeração entre `fase.md`/esta matriz e as SPECs foi encerrada em 2026-09-17; a numeração CA-2-01..12 e RN-F2-001..014 é única e coerente.
- A pendência de identidade técnica/multi-fonte permanece; T04 e T08 usam `record_id` somente no escopo da fonte declarada.
- `META-F2-001` foi aprovado humanamente com `fallback_manual`; não há integração Meta validada.
- `META-F2-MANUAL-001` foi processado somente como lote sintético em dry-run; os erros da T08 são simulados, não respostas reais.
- F2-T09 permanece condicional e não foi iniciada.
