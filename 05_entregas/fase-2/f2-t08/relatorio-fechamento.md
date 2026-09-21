# Atendimento e fechamento — F2-T08

**Data do fechamento:** 2026-09-21  
**Task:** F2-T08 — Provar o fallback manual e a recuperação simulada de falhas sem escrita externa ou duplicidade  
**Champion:** João Paulo  
**SPEC:** F2-004 — Prova de integração Meta ou fallback manual explícito  
**Resultado:** CONCLUÍDA — bateria humana 5/5 aprovada; CA-2-10 e CA-2-12 no recorte simulado atendidos.

## Escopo fechado

A F2-T08 foi fechada exclusivamente no ciclo documental autorizado após a implementação e a aprovação humana dos cinco testes. Não houve implementação adicional no fechamento.

- T04 continua sendo o adapter compatível da reconciliação.
- O núcleo compartilhado está em `src/lib/f2/reconciliation/core.ts`.
- O adapter/contrato manual está em `src/lib/f2/t08/manualBatch.ts`.
- A superfície usa a rota existente `/atribuicao-t04`, com seção explicitamente sintética da T08.
- O lote `META-F2-MANUAL-001` é 100% sintético e processado em memória.
- O mesmo `batch_id` com o mesmo payload resulta em `replay_skip`.
- O mesmo `batch_id` com payload diferente resulta em `payload_conflict`, estado `bloqueada` e decisão humana necessária.
- 401/403/429/timeout/payload inválido são eventos simulados, sem chamada Meta e sem retry automático.

## Matriz de critérios

| Critério | Regra/prova | Evidência | Veredito |
|---|---|---|---|
| CA-2-10 | Sem acesso Meta validado, manter `fallback_manual`/`bloqueada`; não criar nem alegar integração | `META-F2-001` aprovado na T07; superfície T08 identifica lote como `manual_export`; proteção de escopo afirma ausência de Meta, token/OAuth e escrita | **PASSOU** |
| CA-2-12 — lote/replay | Reconciliar lote sintético sem duplicidade ou overwrite | T08 8/8; 5 classificações; `replay_skip`; `payload_conflict`/`bloqueada`; primeira execução só planeja uma criação | **PASSOU** |
| CA-2-12 — erros | 401/403/429/timeout/payload inválido devem parar o caminho seguro sem escrita | Cinco blocos marcados `SIMULADO · sem chamada externa · sem retry automático`; fallback em 401/403/429/timeout; bloqueio em payload inválido | **PASSOU** |
| Regressão T04 | Preservar engine, replay e reconciliação já homologados | T04 7/7 no preview; baseline 10; pipeline 10; replay 0 | **PASSOU** |
| Proteção de dados/escopo | Sem dados reais/pessoais, leads, contatos, Meta ou escrita em `demandas` | Bateria humana 5/5; consulta viva: demandas 10, migrations até 0020, collections inalteradas | **PASSOU** |

## Bateria humana

1. **T04 preservada — APROVADO:** 7/7 checks verdes, pipeline 10, replay 0.
2. **Lote manual — APROVADO:** T08 8/8, 5 classificações corretas e estado seguro `bloqueada`.
3. **Replay/conflito — APROVADO:** `replay_skip` sem duplicidade; conflito de payload bloqueado sem overwrite.
4. **Falhas simuladas — APROVADO:** cinco códigos identificados como simulados, sem chamada externa; estados seguros corretos.
5. **Regressão/proteção — APROVADO:** demandas 10, criações 0/0 no teste final, rotas acessíveis, sem Meta/token/dado real.

Evidências fornecidas pelo Champion:

- `uploads/d1df2dc5-teste_t08.pdf`
- `uploads/3f201c65-teste_t08_1.pdf`
- `uploads/245f65bd-image.png`
- `uploads/cd87c996-image.png`
- `uploads/971ea98a-teste_t08_5.pdf`

## Verificação automatizável final

- Skip **v0.0.85**, hash **`25c717a`**.
- QA oficial: setup, análise estática, build, integrações e testes — todos passaram.
- T04: **7/7**.
- T08: **8/8**.
- Preview revalidado após o aceite humano.
- `demandas`: 10 registros.
- Migrations aplicadas: até `0020_f2_t05_decisoes`.
- Collections: somente as existentes antes da T08.
- Nenhuma escrita em `demandas`.
- Nenhuma chamada externa, token/OAuth, dado real/pessoal, publicação ou alteração de orçamento.
- F2-T09 não iniciada.

O arquivo de verificador independente previsto pela rotina não estava disponível neste runtime; o checklist equivalente foi executado em série e essa limitação permanece explicitamente registrada.

## Preservação

- Produto funcional preservado em v0.0.85 (`25c717a`).
- Fase 1 e F2-T01–T07 preservadas.
- T04 preservada como adapter compatível do núcleo generalizado.
- Nenhuma implementação adicional foi feita durante o fechamento.
- `.skip.config.json` permanece como metadado preexistente de build; não foi tratado como alteração funcional.

## Veredito

A F2-T08 está **formalmente concluída**. A F2-T09 permanece condicional, não foi iniciada e exige nova análise oficial, autorização própria, acesso de leitura, payload autorizado, política de dados e contrato de identidade antes de qualquer conexão ou chamada real ao Meta.
