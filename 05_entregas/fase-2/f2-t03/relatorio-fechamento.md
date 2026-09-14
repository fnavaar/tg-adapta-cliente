# Atendimento e fechamento — F2-T03

**Data do fechamento:** 2026-09-14  
**Task:** F2-T03 — Configurar/registrar contrato de atribuição de fonte única e fixtures de qualidade, sem agregação multi-fonte  
**Champion:** João Paulo  
**SPEC de referência:** F2-002 — Integração Meta Ads e atribuição de origem  
**Resultado:** CONCLUÍDA — validação humana aprovada, 4/4 testes aprovados.

## Escopo entregue

A entrega foi mantida exatamente no recorte operacional definido para a F2-T03:

- fonte declarada única: collection `demandas` do Skip;
- chave registrada no escopo dessa fonte: `record_id`;
- fixtures sintéticas `ATR-F2-IN-001`, `ATR-F2-OUT-001` e `ATR-F2-UNK-001`;
- mapa de campos demonstrado pelo painel e pelos registros;
- origem inbound, outbound e desconhecida preservadas;
- campanha preservada quando declarada;
- pendência de identidade/multi-fonte registrada para tasks posteriores;
- nenhuma agregação entre fontes técnicas.

Não houve integração Meta, RD Station, 1CRM ou segunda fonte; não houve decisão de identidade global ou composta.

## Implementação técnica

- Migration aplicada: `0019_f2_t03_atr_fonte_unica`.
- Skip: **v0.0.64**, hash **`00bb006`**.
- A migration foi somente de dados sintéticos na collection existente `demandas`.
- Nenhuma collection nova foi criada.
- Nenhum campo, índice, schema ou hook foi alterado.
- Nenhuma alteração funcional adicional foi feita no fechamento.

## Registros confirmados

Leitura direta da fonte confirmou exatamente três registros ATR:

| Record ID | Origem | Canal | Campanha | Qualidade |
|---|---|---|---|---|
| `ATR-F2-IN-001` | inbound | site | `F2-ATR-FONTE-UNICA-IN` | ok |
| `ATR-F2-OUT-001` | outbound | linkedin | `F2-ATR-FONTE-UNICA-OUT` | ok |
| `ATR-F2-UNK-001` | desconhecido | vazio | vazio | desconhecido |

Total da collection após a aplicação: **10 registros**, preservando as 7 fixtures F1 anteriores.

## QA e regressão

- setup: passou;
- análise estática: passou;
- build: passou;
- integrações: passou;
- testes: passou;
- migration 0019: status `applied`;
- schema de `demandas`: preservado, sem campo novo;
- regressão do painel Fase 1 (`/`): passou;
- regressão do módulo F2-T01/T02 (`/experimentos`): passou;
- IN v3, OUT v3 e RED v4 preservados;
- histórico, bloqueios e aprovações da F2-T01/T02 preservados;
- nenhum registro ATR adicional criado.

## Validação humana — 4/4 aprovados

### Teste 1 — visualização geral das fixtures

Aprovado. As três fixtures ATR apareceram, as fixtures F1 permaneceram visíveis, nenhum registro foi mesclado e a reconciliação geral mostrou painel 10 × fonte 10, diferença 0.

### Teste 2 — filtro por origem

Aprovado com três capturas:

- inbound: 5 registros, diferença 0;
- outbound: 3 registros, diferença 0;
- desconhecido: 2 registros, diferença 0.

`ATR-F2-UNK-001` permaneceu sem origem, canal ou campanha inferidos.

### Teste 3 — campanha e identificador preservados

Aprovado:

- `F2-ATR-FONTE-UNICA-IN` isolou `ATR-F2-IN-001`;
- `F2-ATR-FONTE-UNICA-OUT` isolou `ATR-F2-OUT-001`;
- cada seleção apresentou 1 × 1, diferença 0, PASSOU;
- as campanhas F1 permaneceram disponíveis.

O OCR de um print leu parcialmente o ID OUT, mas a leitura direta da fonte confirmou o valor real `ATR-F2-OUT-001`.

### Teste 4 — atualização de fonte sob filtro

Aprovado:

- filtro `F2-ATR-FONTE-UNICA-IN` permaneceu aplicado;
- apenas `ATR-F2-IN-001` permaneceu na tabela;
- o horário de consulta mudou de 17:43:05 para 09:26:32;
- reconciliação final: painel 1 × fonte 1, diferença 0, PASSOU.

## Divergências e pendências preservadas

1. A divergência de numeração entre `fase.md`/matriz e a SPEC F2-002 permanece aberta. A F2-T03 foi executada pelo recorte específico da linha da task em `fase.md`, conforme autorização do Navaar e do Champion; nenhum documento foi corrigido unilateralmente.
2. A estratégia de identidade técnica entre múltiplas fontes (`record_id` global, chave composta ou outra) permanece pendente para tasks posteriores.
3. O `.skip.config.json` já estava alterado antes da F2-T03. A diferença ficou limitada a `deployment.lastDevBuildRef`, de `1293baa` para `c67ddca`, correspondente ao Skip v0.0.63. Não houve alteração de proteções, rotas, entrypoint, regras ou comportamento funcional; a alteração não foi causada pela migration 0019 e foi preservada por autorização expressa.
4. F2-T01 e F2-T02 permanecem concluídas e validadas.
5. Fase 1 permanece concluída, homologada visualmente e preservada.
6. F2-T04 não foi iniciada.

## Evidências

- Preview: https://repositorio-adapta-cc556--preview.goskip.app/
- Migrations aplicadas: 0001–0005, 0006–0015, 0017–0019.
- Evidências humanas: prints/PDFs dos quatro testes aprovados no chat do Champion.
- Evidência técnica: migration 0019, leitura direta dos três IDs, schema de `demandas`, QA do Skip e regressão das rotas `/` e `/experimentos`.
- Evidências de preservação: estado final dos experimentos IN/OUT/RED, histórico, aprovações e bloqueios conferidos no preview.

## Critério de fechamento

Todos os itens observáveis da linha da F2-T03 foram atendidos, o QA passou e o Champion aprovou expressamente os 4 testes humanos. A task está formalmente concluída. Nenhuma task posterior foi iniciada.
