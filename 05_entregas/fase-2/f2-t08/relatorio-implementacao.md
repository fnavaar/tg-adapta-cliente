# Atendimento e implementação — F2-T08

**Data:** 2026-09-21  
**Task:** F2-T08 — Provar o fallback manual e a recuperação simulada de falhas sem escrita externa ou duplicidade  
**Champion:** João Paulo  
**SPEC:** F2-004 — Prova de integração Meta ou fallback manual explícito  
**Estado:** implementação concluída; aguardando validação humana; não é fechamento formal.

## Decisão de arquitetura aplicada

A autorização foi respeitada exatamente:

- T04 continua sendo o adapter compatível da reconciliação existente.
- O núcleo compartilhado foi generalizado em `src/lib/f2/reconciliation/core.ts`.
- T08 usa o núcleo por meio de `src/lib/f2/t08/manualBatch.ts`.
- Não foi criada uma segunda engine de reconciliação.
- A superfície visual reutiliza `/atribuicao-t04` e apresenta uma seção explicitamente sintética da T08; não foi criada uma nova página isolada.

## Contrato e lote

O lote `META-F2-MANUAL-001` é uma fixture 100% sintética, definida no código da prova e processada em memória. Não é export real da Meta e não representa uma conexão Meta.

O envelope contém `batch_id`, `received_at`, `period_start`, `period_end`, `source_mode`, `source_owner`, `unit_label`, `provided_fields`, `missing_fields` e estado de reconciliação. O `source_mode` autorizado é `manual_export`; `meta_integrated` é rejeitado.

O lote tem cinco linhas sintéticas:

1. `FIX-IN-001` — vinculado e preservado.
2. `META-UNLINKED-001` — não vinculado; criação apenas planejada no dry-run.
3. `META-UNKNOWN-001` — desconhecido; sem inferência de canal/campanha.
4. `FIX-OUT-001` — divergente em relação ao destino; sem overwrite.
5. linha sem `record_id` — inválida; bloqueada sem inferência ou criação.

Não entram nome de pessoa, e-mail, telefone, cargo, lead, formulário, contato, Pixel ou qualquer dado pessoal.

## Idempotência e retorno seguro

- O ledger é somente em memória para a prova.
- O mesmo `batch_id` com o mesmo fingerprint retorna `replay_skip`, zero ações e zero nova contagem.
- O mesmo `batch_id` com fingerprint diferente retorna `payload_conflict`, estado seguro `bloqueada`, preserva o resultado original e exige decisão humana.
- Lote com inválido/divergente termina em `bloqueada`; falhas de autorização/limite/timeout retornam a `fallback_manual`.
- Não há retry automático, overwrite silencioso ou escrita no destino.

## Falhas simuladas

401, 403, 429, timeout e payload inválido são eventos injetados pela função `simulateT08Failure`. A superfície mostra explicitamente `SIMULADO · sem chamada externa · sem retry automático`. Portanto, não são respostas reais da API Meta.

- 401: `fallback_manual`.
- 403: `fallback_manual`.
- 429: `fallback_manual`.
- timeout: `fallback_manual`.
- payload inválido: `bloqueada`.

## Evidência automatizável

- Skip v0.0.85, hash `25c717a`.
- QA oficial: setup, análise estática, build, integrações e testes — todos passaram.
- TDD T04: 7/7 passou.
- TDD T08: 8/8 passou no preview.
- Preview: `https://repositorio-adapta-cc556--preview.goskip.app/atribuicao-t04`.
- Pipeline consultado: 10 registros.
- Primeira execução T08: 1 ação `create` apenas planejada, sem escrita.
- Replay: `replay_skip`, 0 novas ações.
- Payload alterado no mesmo `batch_id`: `payload_conflict`, `bloqueada`, decisão humana necessária.
- Falhas simuladas: 5/5 identificadas, todas sem chamada externa.
- Migrations: permanecem até `0020_f2_t05_decisoes`.
- Collections: permanecem somente as existentes; nenhuma coleção Meta/manual foi criada.

## Regressões e limites

- T04 continua com 7/7 verificações determinísticas.
- `demandas` permanece com 10 registros.
- F2-T01 a F2-T07 permanecem preservadas.
- Nenhuma migration, collection, campo, hook ou RLS foi criado/alterado nesta task.
- Nenhuma chamada Meta, token/OAuth, importação externa, dado real/pessoal, publicação ou alteração de orçamento ocorreu.
- F2-T09 não foi iniciada.

## Correção durante a execução

A primeira execução do TDD revelou uma expectativa incorreta: o lote sintético tem quatro `record_id`s preenchidos contra dez registros no pipeline, portanto oito registros do destino ficam fora do lote parcial. O check foi corrigido de 6 para 8; a regra de reconciliação não foi alterada. O QA completo foi repetido e passou na versão 0.0.84, e novamente na versão final 0.0.85 após remoção de arquivo auxiliar não utilizado.

## Veredito técnico

A implementação mínima autorizada está pronta para teste humano. O veredito formal da F2-T08 continua pendente do Champion; não concluir automaticamente.
