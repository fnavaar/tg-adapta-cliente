# Matriz de rastreabilidade — Fase 2

| Origem do escopo | SPEC | Critério de aceite | Task(s) | Prova/Evidência | Estado |
|---|---|---|---|---|---|
| Fase 2; C-02; DC-001/DC-004; G-006 | F2-001 | CA-2-01..03 | F2-T01, F2-T02 | Briefings, bloqueios, versões e referência de aprovação | F2-T01 e F2-T02 concluídas e validadas |
| Fase 2; C-01/C-04; DC-004; G-001/G-009 | F2-002 | CA-2-04..06 | F2-T03, F2-T04 | Relatório, IDs, reconciliação e lacunas | F2-T03 e F2-T04 concluídas e validadas; F2-T04 com 3/3 testes humanos, 7/7 verificações determinísticas e replay idempotente |
| Fase 2; C-02/C-04; DC-007 | F2-003 | CA-2-07..09 | F2-T05, F2-T06 | Decisão humana e histórico de versões | F2-T05 elegível — aguarda decisor e critério de decisão (insumo do Champion) e autorização expressa |
| Fase 2; DC-003; G-009 | F2-004 | CA-2-10..12 | F2-T07, F2-T08 | Checklist, fallback, falhas simuladas | F2-T07 elegível mediante autorização expressa; F2-T08 bloqueada por dependência |
| Fase 2; DC-003; G-009 | F2-004 | CA-2-11..12 | F2-T09 | Consulta Meta de leitura, reconciliação e erro real | Condicional — não elegível |

## Ressalvas de rastreabilidade

- A divergência de numeração entre `fase.md`/esta matriz e as SPECs foi **encerrada em 2026-09-17**: as SPECs F2-001/F2-002 foram substituídas pelas versões validadas da decomposição de 03/09 e as SPECs F2-003/F2-004 foram publicadas. A numeração CA-2-01..12 e RN-F2-001..014 agora é única e coerente em toda a fase.
- A pendência de identidade técnica/multi-fonte permanece para tasks posteriores; a F2-T04 usou `record_id` somente no escopo da fonte declarada.
- F2-T05 exige decisor identificado e critério de decisão definido no briefing como insumo do Champion (RN-F2-008); esses insumos não podem ser inferidos pelo agente.
