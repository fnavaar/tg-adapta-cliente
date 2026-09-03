# STATUS — Projeto TG Mais Serviços de Tecnologia e RH LTDA

> **Atualizado em:** 2026-09-03 · **Por:** Adapta / Pepe
> O painel do projeto: fase atual, progresso e o que precisa de atenção.

## Onde estamos

- **Fase atual:** 1 — Sistema de baseline, dicionário e pipeline mínimo · encerrada em 2026-09-03
- **Objetivo desta fase:** materializar o dicionário, o baseline reproduzível e um pipeline/painel mínimo com evidências.
- **No prazo?** Fase 1 concluída — 6 de 6 tasks concluídas (100%).

## Progresso da fase

- **Tasks:** 6/6 concluídas (100%)
  - F1-T01 — dicionário de demanda (concluída)
  - F1-T02 — amostra e checagens de qualidade (concluída)
  - F1-T03 — baseline reproduzível e gate de alvo (concluída)
  - F1-T04 — taxonomia e regras do pipeline (CONCLUÍDA e validada humanamente em 01/09/2026)
  - F1-T05 — jornada e handoff controlado (CONCLUÍDA e validada humanamente em 01/09/2026)
  - F1-T06 — painel mínimo, reconciliação e rollback (CONCLUÍDA e validada humanamente em 03/09/2026)
- **Próxima ação:** nenhuma — Fase 1 encerrada. Aguardar nova autorização expressa para qualquer próxima fase/task.

## Travas ativas

| Trava | Desde | Quem resolve | Ação em curso |
|---|---|---|---|
| Nenhum bloqueio de fechamento | 2026-09-03 | — | Fase 1 encerrada após aprovação humana da F1-T06. Pendência arquitetural de identidade técnica permanece para fase futura. |

## Pendências futuras que não bloqueiam o fechamento

- Definir, antes de integração efetiva com múltiplas fontes, a identidade técnica: `record_id` global, `sistema_origem_tecnico + record_id` ou outra chave aprovada.
- Após essa decisão, reavaliar proteção em duas camadas: aplicação e restrição `UNIQUE` apropriada no banco.

## Entregas concluídas

| Fase | O que foi entregue | Fechada em |
|---|---|---|
| 1 | Pasta operacional, SPECs e tasks preparadas; execução pendente | — |
| 1 | F1-T01: dicionário de demanda + collection `demandas` no Skip Cloud | 2026-08-19 |
| 1 | F1-T02: amostra validada, checagens origem/duplicidade/qualidade/privacidade | 2026-08-19 |
| 1 | F1-T03: baseline comercial, gate, Dicionário Comercial v1, definição de Lead Qualificado | 2026-08-27 |
| 1 | F1-T04: migration 0004 (4 campos) + hooks de validação + correções (autopreenchimento conversão; motivo recusa) | 2026-09-01 |
| 1 | F1-T05: migration 0005, handoff/ICP, jornadas, regressão técnica e validação humana | 2026-09-01 |
| 1 | F1-T06: painel mínimo, reconciliação, reprocessamento controlado, rollback e validação humana | 2026-09-03 |

## Próxima reunião

Fase 1 encerrada em 2026-09-03. Próxima fase/task depende de nova autorização expressa do Champion.
