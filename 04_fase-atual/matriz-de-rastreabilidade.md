# Matriz de rastreabilidade — Fase 3 (TG Mais)

**Escopo:** `03-Projeto/02-Escopo-Definitivo.md` · Fase 3 — Sistema integrado de pipeline, dashboard e handoffs
**Run:** `20260923T1514Z-6b09d189-liberar-f3`
**Estado:** Fase 3 em execução; 0/13 tasks concluídas; F3-T01 em andamento. Atualizada em 22/10/2026 (5ª call, decisão P1, evoluções EV-5C-01..06).

| Origem do escopo / evolução | SPEC | Critérios de aceite | Task(s) | Prova / evidência | Estado |
|---|---|---|---|---|---|
| C-03; DC-001/DC-004; RQ-003/RQ-004; G-002 | F3-001 pipeline integrado | CA-3-01..03 + CA-3-04 (E-F3-001-01: hierarquia Demanda→Propostas→Vagas) | F3-T01, F3-T02 | Jornada inbound/outbound, proposta/vaga, retorno, escalonamento, log append-only, equivalência humana, hierarquia com coleções relacionadas | F3-T01 elegível; F3-T02 bloqueada por F3-T01 + B3-RACI-01 |
| C-04; DC-002/DC-004; RQ-001/RQ-006/RQ-007; G-001/G-005 | F3-002 dashboard/gargalos | CA-3-11..12 (renumerados de CA-3-04..05 por E-F3-002-01) | F3-T03, F3-T04 | Visões por estado, gargalo, tempos, retorno, contagens pela fonte, bloqueio de KPI sem alvo | F3-T03 bloqueada por F3-T01; F3-T04 bloqueada por F3-T03 + B3-MET-01 |
| C-05; DC-004/DC-005; RQ-004; G-004/G-005 | F3-003 handoffs por papel | CA-3-06..08 | F3-T05, F3-T06 | Registro, aceite/recusa, SLA, escalonamento, falha segura, recuperação e matriz RACI | F3-T05 bloqueada por F3-T01; F3-T06 bloqueada por F3-T05 + B3-RACI-01 |
| C-06; DC-005/DC-006; RQ-009; G-003 | F3-004 sinais DHO | CA-3-09..10 | F3-T07, F3-T08 | Objeto separado, lista fechada, prova negativa de acesso, encaminhamento humano, fail-closed | F3-T07 bloqueada por F3-T01 + decisão C-06; F3-T08 bloqueada por F3-T07 |
| §12.2 C-04a; EV-5C-01; P1 | F3-005 funil Kanban | CA-3-13..14 | F3-T10, F3-T11 | Colunas por estado, cartão com origem/serviço/dono/próxima ação, Jornada, filtros, arrastar = transição com evidência | F3-T10 bloqueada por F3-T01; F3-T11 por F3-T10 |
| §12.2 C-04b; EV-5C-02/03/05/06; P1; G-009 | F3-006 campanhas Meta via Maestro | CA-3-15..17 | F3-T09, F3-T12, F3-T13 | Diagnóstico de automações e destino dos leads; tela Campanhas; automação diária no Maestro só leitura; aviso de conexão; idempotência; destino único | F3-T09 elegível após F3-T01; F3-T12 bloqueada por F3-T09 + B3-META-LEITOR; F3-T13 por F3-T12 |
| EV-01/EV-02 — governança Meta (alterado por EV-5C-02 em 22/10) | F3-006 | CA-3-15..17 | F3-T09, F3-T12, F3-T13 | Leitura Meta só de métricas de campanha pela SPEC-F3-006; sem dado pessoal, sem escrita; demais SPECs F3 não leem Meta | B3-META-01 alterado; B3-META-LEITOR aberto |
| EV-5C-04 — visibilidade | F3-001..006 | transversal | todas | Cada task declara "Onde executar" e "O que você vai ver" (emendas E-F3-001-03, E-F3-002-02, E-F3-003-02, E-F3-004-01) | Incorporado |
| EV-03 — identidade multi-fonte | F3-001/F3-002 | CA-3-01..04, CA-3-11..12 | F3-T01..T04 | Identidade explícita por fonte; sem dedupe por inferência; `demandas`↔`experimentos_f2` não é criado automaticamente | B3-ID-01 aberto |
| EV-06 — G-001 e lead qualificado | F3-001/F3-002 | CA-3-11..12 | F3-T03/F3-T04 | Distribuição/tempos/gargalos permitidos; KPI contra alvo bloqueado com pendência visível | B3-MET-01 aberto |
| EV-04/EV-07/EV-08 — falha segura, prova e UI | F3-001..004 | transversal | todas | Estado seguro sem retry cego; prova automatizável + bateria humana; limitações registradas | Incorporado às SPECs/TDDs |

## Bloqueios e decisões preservados

- **B3-META-01 (alterado 22/10):** leitura Meta na F3 só de métricas de campanha, pela SPEC-F3-006; sem dado pessoal e sem escrita.
- **B3-META-LEITOR (novo 22/10):** leitor dedicado somente leitura conectado, ou aceite do Champion registrado para o principal atual, antes da F3-T12.
- **B3-LGPD-01 (formalizado 22/10):** dado real de contato só após política aprovada; até lá, selo TESTE.
- **B3-ID-01:** contrato de identidade por fonte; sem chave global ou deduplicação por inferência.
- **B3-MET-01:** alvo, fórmula, período e definição de lead qualificado antes de KPI de resultado.
- **B3-RACI-01:** matriz nominal de handoffs antes da prova F3-T06.
- **B3-DHO-01:** lista de sinais autorizados e política de acesso antes de dado real de sinal; F3-004 permanece fail-closed com fixtures.

## Projeções

- Jornada: `00.tasks_per_fase/fase_3.md`, 13 tasks, fase-format:2, F3-T01 em andamento; F3-T09..T13 sem id até a sincronização do quadro.
- Tasks Gerais: `03-Projeto/02-Plano_de_acao/03.Fase_3/00-Tasks_Gerais.md`.
- SPECs: F3-001..006, cada uma com TDD, critérios binários, bloqueios e tasks vinculadas.