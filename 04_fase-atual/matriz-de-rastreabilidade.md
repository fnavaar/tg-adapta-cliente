# Matriz de rastreabilidade — Fase 3 (TG Mais)

**Escopo:** `03-Projeto/02-Escopo-Definitivo.md` · Fase 3 — Sistema integrado de pipeline, dashboard e handoffs
**Run:** `20260923T1514Z-6b09d189-liberar-f3`
**Estado:** Fase 3 liberada; 0/8 tasks concluídas; F3-T01 única elegível.

| Origem do escopo / evolução | SPEC | Critérios de aceite | Task(s) | Prova / evidência | Estado |
|---|---|---|---|---|---|
| C-03; DC-001/DC-004; RQ-003/RQ-004; G-002 | F3-001 pipeline integrado | CA-3-01..03 | F3-T01, F3-T02 | Jornada inbound/outbound, proposta/vaga, retorno, escalonamento, log append-only, equivalência humana | F3-T01 elegível; F3-T02 bloqueada por F3-T01 + B3-RACI-01 |
| C-04; DC-002/DC-004; RQ-001/RQ-006/RQ-007; G-001/G-005 | F3-002 dashboard/gargalos | CA-3-04..05 | F3-T03, F3-T04 | Visões por estado, gargalo, tempos, retorno, contagens pela fonte, bloqueio de KPI sem alvo | F3-T03 bloqueada por F3-T01; F3-T04 bloqueada por F3-T03 + B3-MET-01 |
| C-05; DC-004/DC-005; RQ-004; G-004/G-005 | F3-003 handoffs por papel | CA-3-06..08 | F3-T05, F3-T06 | Registro, aceite/recusa, SLA, escalonamento, falha segura, recuperação e matriz RACI | F3-T05 bloqueada por F3-T01; F3-T06 bloqueada por F3-T05 + B3-RACI-01 |
| C-06; DC-005/DC-006; RQ-009; G-003 | F3-004 sinais DHO | CA-3-09..10 | F3-T07, F3-T08 | Objeto separado, lista fechada, prova negativa de acesso, encaminhamento humano, fail-closed | F3-T07 bloqueada por F3-T01 + decisão C-06; F3-T08 bloqueada por F3-T07 |
| EV-01/EV-02 — governança Meta | F3-001..004 | transversal | todas | Nenhuma task F3 lê Meta; regularização pelo leitor dedicado antes de eventual emenda | B3-META-01 aberto |
| EV-03 — identidade multi-fonte | F3-001/F3-002 | CA-3-01..05 | F3-T01..T04 | Identidade explícita por fonte; sem dedupe por inferência; `demandas`↔`experimentos_f2` não é criado automaticamente | B3-ID-01 aberto |
| EV-06 — G-001 e lead qualificado | F3-001/F3-002 | CA-3-04..05 | F3-T03/F3-T04 | Distribuição/tempos/gargalos permitidos; KPI contra alvo bloqueado com pendência visível | B3-MET-01 aberto |
| EV-04/EV-07/EV-08 — falha segura, prova e UI | F3-001..004 | transversal | todas | Estado seguro sem retry cego; prova automatizável + bateria humana; limitações registradas | Incorporado às SPECs/TDDs |

## Bloqueios e decisões preservados

- **B3-META-01:** nenhuma leitura Meta na F3 antes da regularização da conexão pelo leitor dedicado.
- **B3-ID-01:** contrato de identidade por fonte; sem chave global ou deduplicação por inferência.
- **B3-MET-01:** alvo, fórmula, período e definição de lead qualificado antes de KPI de resultado.
- **B3-RACI-01:** matriz nominal de handoffs antes da prova F3-T06.
- **B3-DHO-01:** lista de sinais autorizados e política de acesso antes de dado real de sinal; F3-004 permanece fail-closed com fixtures.

## Projeções

- Jornada: `00.tasks_per_fase/fase_3.md`, 8 tasks, fase-format:2, F3-T01 única elegível.
- Tasks Gerais: `03-Projeto/02-Plano_de_acao/03.Fase_3/00-Tasks_Gerais.md`.
- SPECs: F3-001..004, cada uma com TDD, critérios binários, bloqueios e tasks vinculadas.
