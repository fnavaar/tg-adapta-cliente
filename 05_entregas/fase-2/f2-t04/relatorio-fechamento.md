# Atendimento e fechamento — F2-T04

**Data do fechamento:** 2026-09-17  
**Task:** F2-T04 — Provar atribuição, desconhecido, duplicidade e reconciliação por IDs contra a fonte declarada  
**Champion:** João Paulo  
**SPEC de referência:** F2-002 — Integração Meta Ads e atribuição de origem  
**Resultado:** CONCLUÍDA — validação humana aprovada, 3/3 testes aprovados.

## Escopo entregue

A entrega ficou exatamente no recorte autorizado para a F2-T04:

- lote-fonte sintético independente, sem integração externa;
- leitura somente da fonte declarada para reconciliação;
- engine determinística em dry-run, sem escrita em `demandas`;
- relatório fonte × pipeline por `record_id`;
- tratamento explícito de origem desconhecida sem inferência;
- identificação de duplicidade com payload idêntico;
- identificação de conflito com mesmo `record_id` e payload divergente;
- prova de replay idempotente;
- lista de lacunas com responsável pela qualidade da fonte.

Não houve Meta, RD Station, 1CRM, dado real, segunda fonte técnica, identidade global/multi-fonte ou relação estrutural entre `demandas` e `experimentos_f2`.

## Lote-fonte sintético

O lote contém **17 linhas**, com **14 chaves preenchidas**:

| Grupo | Evidência | Quantidade |
|---|---|---:|
| Baseline preservado da Fase 1/F2-T03 | 10 registros comparados com a fonte declarada | 10 |
| GREEN inbound/outbound | `T04-GREEN-IN-001` e `T04-GREEN-OUT-001` | 2 |
| Replay idêntico | `T04-DUP-REPLAY-001` em duas linhas | 2 linhas / 1 grupo |
| Conflito | `T04-CONFLICT-001` com duas versões divergentes | 2 linhas / 1 grupo |
| RED sem chave/origem | linha bloqueada sem inferência | 1 |

Os dois GREEN foram somente planejados no dry-run; não foram gravados no pipeline.

## Implementação técnica

- Rota isolada: `/atribuicao-t04`.
- Arquivos funcionais da T04: lote-fonte, engine determinística e página de reconciliação; rota e navegação foram adicionadas sem alterar as telas homologadas.
- Skip funcional: **v0.0.66**, hash **`c27bc10`**.
- QA oficial: setup, análise estática, build, integrações e testes passaram.
- Não foi criada migration da T04.
- Não foi criada collection, campo, índice ou schema.
- Nenhum hook ou RLS foi alterado.
- A única pendência do working tree é o `.skip.config.json` preexistente, preservado como metadado de build (`deployment.lastDevBuildRef=c67ddca`); não foi causado pela T04.

## Verificações determinísticas — 7/7 aprovadas

1. **Baseline:** 10 linhas da fonte × 10 registros no pipeline, sem mutação.
2. **GREEN:** duas ações de criação planejadas no dry-run, uma inbound e uma outbound.
3. **RED:** uma linha sem chave/origem bloqueada; nenhuma inferência ou criação.
4. **Duplicidade:** `T04-DUP-REPLAY-001` sinalizado; nenhuma segunda gravação.
5. **Conflito:** `T04-CONFLICT-001` bloqueado; nenhum overwrite silencioso.
6. **Replay:** reprocessamento com **0 novas criações**.
7. **Pureza:** a lista real do pipeline permaneceu com 10 registros.

## Validação humana — 3/3 aprovados

### Teste 1 — lote e proteção de escopo

Aprovado pelo Champion. A tela mostrou 17 linhas da fonte, 10 registros consultados, 7/7 verificações verdes, duas criações apenas planejadas, duplicidade e conflito explícitos, e o aviso de que não havia escrita em `demandas`.

A leitura inicial de PDF apresentou `2 duplicidade` por artefato de OCR; a conferência ao vivo confirmou o valor correto: **1 duplicidade**.

### Teste 2 — replay idempotente

Aprovado pelo Champion. O relatório mudou para `replay`; os dois GREEN passaram a `skip`/preservado no pipeline simulado; `T04-DUP-REPLAY-001` permaneceu `skip`; `T04-CONFLICT-001` permaneceu `conflict`; não restou nenhuma ação `create`; o botão de replay desapareceu; o pipeline real permaneceu em 10.

### Teste 3 — regressão e ausência de mutação

Aprovado pelo Champion:

- painel `/`: 10 registros, fonte 10, diferença 0, IDs coincidentes;
- nenhum `T04-*` apareceu em `demandas`;
- timestamp de consulta da fonte foi atualizado após `Atualizar fonte`;
- `/experimentos`: `EXP-F2-IN-001` e `EXP-F2-OUT-001` permaneceram `Aprovado para preparação`; `EXP-F2-RED-001` permaneceu `Rascunho`.

## Regressão e preservação

- Fase 1 preservada e sem alteração funcional.
- F2-T01 preservada.
- F2-T02 preservada, incluindo IN/OUT/RED, versões, aprovações e bloqueios.
- F2-T03 preservada, incluindo as três fixtures ATR e a pendência multi-fonte.
- Collection `demandas`: 10 registros; schema, campos, regras, índices e RLS preservados.
- Migrations: nenhuma migration nova; a última permanece `0019_f2_t03_atr_fonte_unica`.
- Nenhum registro `T04-*` foi gravado.
- Nenhuma relação estrutural `demandas` ↔ `experimentos_f2` foi criada.
- F2-T05 não foi iniciada.

## Divergências, limites e pendências preservados

1. A divergência documental de numeração entre `fase.md`/matriz e a SPEC F2-002 permanece aberta; nenhum documento foi corrigido unilateralmente.
2. A pendência arquitetural de identidade técnica/multi-fonte permanece para tasks posteriores.
3. `record_id` foi usado somente no escopo da fonte declarada; não foi tratado como identidade global.
4. O `.skip.config.json` preexistente foi preservado; sua alteração de metadado não é mudança funcional da T04.
5. Não houve Meta, RD Station, 1CRM, dados reais, publicação, gasto, contato externo ou automação externa.
6. O fechamento desta task foi exclusivamente documental e de governança; não houve alteração funcional adicional no produto.

## Evidências

- Preview funcional: https://repositorio-adapta-cc556--preview.goskip.app/atribuicao-t04
- Painel de regressão: https://repositorio-adapta-cc556--preview.goskip.app/
- Módulo preservado: https://repositorio-adapta-cc556--preview.goskip.app/experimentos
- Versão funcional: Skip v0.0.66, hash `c27bc10`.
- QA: resultado persistido no apply v0.0.66.
- Evidências humanas: capturas/PDFs anexados pelo Champion no canal da validação, correspondentes aos três testes aprovados.
- Fonte de governança: `04_fase-atual/fase.md`, `STATUS.md`, `changelog.md`, matriz e estado persistente.

## Critério de fechamento

Todos os critérios observáveis da linha F2-T04 foram revalidados do zero, o QA oficial passou, as verificações determinísticas passaram 7/7 e o Champion aprovou expressamente os 3 testes humanos. A F2-T04 está formalmente concluída.

Nenhuma task posterior foi iniciada. A F2-T05 permanece pendente de autorização expressa.
