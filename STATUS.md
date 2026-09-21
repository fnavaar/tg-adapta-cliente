# STATUS — Projeto TG Mais Serviços de Tecnologia e RH LTDA

> **Atualizado em:** 2026-09-21 · **Por:** Adapta / Champion
> O painel do projeto: fase atual, progresso e o que precisa de atenção.

## Onde estamos

- **Fase atual:** 2 — Sistema de campanhas e experimentação de Growth Marketing (LIBERADA PARA EXECUÇÃO).
- **Task ativa:** nenhuma — F2-T05 concluída e validada em 2026-09-21.
- **Task anterior:** F2-T04 concluída e validada em 2026-09-17.
- **Progresso:** 5 de 9 tasks concluídas (56%); próximas elegíveis: F2-T06 e F2-T07.

## Resultado técnico da F2-T01

- Commit de implementação: `c6b77ef9796ef760ccaf7d04db412d6597831dcf`.
- Commit de evidência individual: `27d4e5c963a0fe346918ce3da07cdb1201770e25`.
- Massa sintética: `EXP-F2-IN-001` e `EXP-F2-OUT-001`.
- TDD: 20/20 aprovados, 0 falhas.
- Evidências individuais registradas em `05_entregas/fase-2/f2-t01/evidence/test-results.json`.
- Relatório: `05_entregas/fase-2/f2-t01/report/atendimento-criterios-f2-t01.md`.
- Validação humana: aprovada expressamente.

## Resultado da F2-T02

- Relatório de fechamento: `05_entregas/fase-2/f2-t02/relatorio-fechamento.md`.
- Validação humana: testes RED, duplicidade, versionamento/histórico, separação de preparação/publicação/gasto e permissões aprovados ou comprovados conforme relatório.
- Correções retestadas: v0.0.60 (validação do RED) e v0.0.61 (mensagem de duplicidade); QA completo passou nas duas versões.
- Limite: publicação e gasto foram validados exclusivamente como controles sintéticos; não houve execução real.
- Ressalva: CA-2-02 e CA-2-03, em sentido amplo de captura de leads e relatório de métricas, não são declarados como entregues pela F2-T02.

## Resultado da F2-T03

- Relatório de fechamento: `05_entregas/fase-2/f2-t03/relatorio-fechamento.md`.
- Entrega: contrato de atribuição de fonte única, três fixtures sintéticas e registro da pendência multi-fonte.
- Fixtures: `ATR-F2-IN-001`, `ATR-F2-OUT-001` e `ATR-F2-UNK-001`.
- Migration: `0019_f2_t03_atr_fonte_unica` aplicada no Skip.
- Skip: v0.0.64, hash `00bb006`.
- QA oficial: setup, análise estática, build, integrações e testes passaram.
- Validação humana: 4/4 testes aprovados em 2026-09-14.
- Limites: sem Meta, RD Station, 1CRM, segunda fonte, schema novo, campo novo, hook novo ou decisão de identidade global/composta.

## Resultado da F2-T04

- Relatório de fechamento: `05_entregas/fase-2/f2-t04/relatorio-fechamento.md`.
- Entrega: lote-fonte sintético independente, engine determinística em dry-run, relatório fonte×pipeline, tratamento de desconhecido/duplicidade/conflito e replay idempotente.
- Lote: 17 linhas, 14 chaves preenchidas, 1 linha sem chave, 1 grupo de duplicidade e 1 grupo de conflito; baseline de 10 registros.
- Skip funcional: v0.0.66, hash `c27bc10`.
- QA oficial: setup, análise estática, build, integrações e testes passaram.
- Verificações próprias: 7/7 aprovadas; replay com 0 novas criações.
- Validação humana: 3/3 testes aprovados em 2026-09-17.
- Regressão: painel 10 × fonte 10, diferença 0; nenhum `T04-*` gravado; Fase 1 e F2-T01/T02/T03 preservadas.
- Limites: sem Meta, RD Station, 1CRM, dados reais, identidade global/multi-fonte, relação `demandas` ↔ `experimentos_f2`, nova collection/campo, alteração de RLS/hook/schema ou início da F2-T05.

## Resultado da F2-T05

- Relatório de fechamento: `05_entregas/fase-2/f2-t05/relatorio-fechamento.md`.
- Entrega: collection `decisoes_f2` (migration `0020_f2_t05_decisoes`), hook exclusivo de invariantes, seção Decisão de Marketing no detalhe do experimento e fila `/decisoes-f2`, com fixtures sintéticas RED/GREEN/rollback.
- Skip funcional da entrega: v0.0.78, hash `2a06902` (versão corrente v0.0.79, `d42864c`).
- QA oficial: setup, análise estática, build, integrações e testes passaram.
- TDD determinístico: 6/6 aprovados.
- Validação humana: 3/3 testes aprovados em 2026-09-18 (RED, GREEN, rollback) + reteste do GREEN aprovado em 2026-09-21 após correção do detector.
- Rollback provado: `DEC-F2-004` com `previous_decision_id = DEC-F2-002`; `DEC-F2-002` preservada como revogada; histórico sem exclusão.
- Debugs registrados: `06_notas/debug/debug-2026-09-18-f2-t05-decisao-subsequente.md` e `06_notas/debug/debug-2026-09-18-f2-t05-detector-red-green.md`.
- Limites: sem Meta, RD Station, 1CRM, Omie, dados reais, publicação, orçamento, decisão automática, relação `demandas` ↔ `experimentos_f2`, identidade global ou início de F2-T06/F2-T07.

## Regularização documental e liberação da F2-T05 (2026-09-17)

- Publicadas as SPECs **F2-003** (decisão do experimento) e **F2-004** (prova Meta ou fallback manual), que constavam da decomposição aprovada em 03/09 mas não haviam sido enviadas na liberação original da fase — causa do bloqueio documental da F2-T05 identificado pelo Champion.
- As SPECs F2-001 e F2-002 foram substituídas pelas versões validadas da mesma decomposição (arquivos antigos arquivados com nota de substituição), encerrando a divergência de numeração CA/RN registrada como aberta desde a F2-T03.
- As tasks F2-T01..T04 foram executadas contra os contratos destas versões (fixtures `EXP-F2-*`, `ATR-F2-*`, reconciliação por `record_id`); nenhum resultado, evidência ou aceite foi alterado retroativamente.
- **F2-T05 AUTORIZADA**: o Champion confirmou positivamente a liberação; decisor registrado na SPEC/jornada/matriz — João Paulo (Champion/direção); critério de decisão conforme briefing de cada experimento (RN-F2-008) — na prova sintética, o briefing sintético; decisão real exige critério real.

## Gate atual

**Nenhuma task em execução.** F2-T05 concluída e validada (2026-09-21). F2-T06 (Leva 6) e F2-T07 (Leva 5) estão elegíveis e aguardam autorização expressa do Champion — uma por vez. F2-T08 bloqueada por dependência da T07; F2-T09 condicional.

## Pendências preservadas

- A pendência arquitetural de identidade técnica/multi-fonte permanece para tasks posteriores.
- Na F2-T04, `record_id` foi usado somente no escopo da fonte declarada; não houve identidade global ou composta.
- O `.skip.config.json` mantém a alteração preexistente `deployment.lastDevBuildRef = c67ddca`, correspondente ao Skip v0.0.63; a alteração não modificou proteções, rotas, entrypoint ou regras, e não foi causada pela T04.
- Nenhuma integração Meta, RD Station ou 1CRM foi executada.
- Nenhuma relação estrutural entre `demandas` e `experimentos_f2` foi criada.
- Na F2-T05, `DEC-F2-003` permanece na massa sintética como registro criado pelo botão genérico durante o teste (sem vínculo de rollback); preservada sem alteração.

## Fase 1 arquivada e homologada visualmente

- Fase 1 foi encerrada em 2026-09-03 e está preservada em `05_entregas/fase-1/`.
- Em 11/09/2026, foi realizada homologação visual retroativa pelo Champion, com **6 homologações executadas e 6/6 aprovadas**.
- F1-T01 a F1-T06 permanecem concluídas.
- A Fase 1 passa a ter evidência técnica e validação visual retroativa pelo Champion.
- Nenhuma alteração funcional foi necessária durante a homologação.
- Nenhum código, banco, migration, hook, dado ou regra da Fase 1 foi alterado.

## F2-T01 a F2-T05 preservadas

- F2-T01, F2-T02, F2-T03, F2-T04 e F2-T05 permanecem concluídas e validadas.
- F2-T06 e F2-T07 elegíveis, aguardando autorização expressa; F2-T08 bloqueada; F2-T09 condicional.
