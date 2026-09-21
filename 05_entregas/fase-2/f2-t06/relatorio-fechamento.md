# Atendimento e fechamento — F2-T06

**Data do fechamento:** 2026-09-21  
**Task:** F2-T06 — Provar decisão baseada em qualidade e o histórico de ajuste/revogação  
**Champion:** João Paulo  
**SPEC de referência:** F2-003 — Decisão humana de continuar, ajustar ou interromper  
**Resultado:** CONCLUÍDA — revalidação somente leitura aprovada; CA-2-07, CA-2-08 e CA-2-09 íntegros.

## Escopo autorizado

A F2-T06 foi executada exclusivamente como task de prova, revalidação e fechamento documental, conforme autorização expressa do Champion. Não houve implementação funcional, mutação de dados ou repetição mutativa dos testes humanos da F2-T05.

Não foram criados nem alterados:

- tela, rota ou componente;
- collection, campo, migration, índice ou schema;
- hook, RLS ou regra funcional;
- fixture ou decisão existente;
- integração Meta, RD Station, 1CRM ou Omie;
- collection `demandas`, F2-T04 ou qualquer dado externo.

## Fontes e método de revalidação

Foram confrontados, em leitura, a SPEC F2-003, `fase.md`, a matriz de rastreabilidade, Tasks Gerais, STATUS, changelog, relatório de fechamento da F2-T05, debug/aprendizados da T05 e o estado real do Skip.

A leitura do backend confirmou:

- migration `0020_f2_t05_decisoes` com status `applied`;
- collection `decisoes_f2` presente, com os campos, índices e regras da F2-T05;
- seis registros decisórios sintéticos preservados;
- `DEC-F2-004.previous_decision_id = DEC-F2-002`;
- nenhuma escrita, criação, atualização ou exclusão realizada nesta task.

Baseline vivo consultado, sem mutação:

- `demandas`: 10 registros;
- `experimentos_f2`: 3 experimentos (`EXP-F2-IN-001`, `EXP-F2-OUT-001`, `EXP-F2-RED-001`);
- `experimento_versoes_f2`: 26 versões/históricos;
- `aprovacoes_f2`: 4 registros;
- `bloqueios_f2`: 2 registros;
- `decisoes_f2`: 6 registros.

## Matriz de fechamento

| Critério | Regra | Evidência utilizada | Resultado da revalidação |
|---|---|---|---|
| **CA-2-07** — decisão humana vinculada a volume e qualidade | `RN-F2-008` exige critério e evidência; decisão final é humana. | `DEC-F2-004`: `status=registrada`, `decision=ajustar`, `evidence_ref=F2-T04-SOURCE-001 / snapshot sintético/manual`, volume `12 cliques; 3 capturas sintéticas`, qualidade `1 lead qualificado sintético; 0 oportunidades`, owner João Paulo, próxima ação e prazo. | **PASSOU.** Há decisão humana, referência do relatório/lote, evidência de volume e evidência positiva de qualidade; o registro permanece sintético/manual. |
| **CA-2-08** — resultado incompleto ou só de clique permanece pendente | `RN-F2-009` impede declarar qualidade/sucesso com clique, impressão ou abandono isolado. | `DEC-F2-RED-001`: `status=pendente`, sem decisão final, volume `12 cliques; 0 leads qualificados; 0 oportunidades`, qualidade `Somente clique/atividade; qualidade comercial ausente`, leitura de amostra insuficiente e próxima ação de coleta. | **PASSOU.** O RED continua pendente e não é apresentado como êxito; a evidência de atividade não foi convertida em qualidade. |
| **CA-2-09** — ajuste/revogação preserva histórico e aponta próxima ação | `RN-F2-010` exige próxima ação; rollback revoga sem apagar e nova leitura referencia o estado anterior. | `DEC-F2-002`: `status=revogada`, motivo e timestamp preservados. `DEC-F2-004`: `status=registrada`, `decision=ajustar`, próxima ação `Criar nova versão do briefing e repetir a janela`, `previous_decision_id=DEC-F2-002`. | **PASSOU.** A decisão anterior permanece no histórico, a revogação é rastreável e a decisão subsequente aponta explicitamente para a anterior. |

## Registros decisórios revalidados

### `DEC-F2-RED-001`

- Permanece `pendente`.
- Representa somente clique/atividade, sem evidência comercial positiva.
- Não possui decisão final registrada.
- Mantém owner, prazo e próxima ação de coleta/definição de critério.
- Não foi utilizado como êxito nem alterado nesta task.

### `DEC-F2-004`

- Permanece `registrada` com decisão `ajustar`.
- Referencia `F2-T04-SOURCE-001 / snapshot sintético/manual`.
- Contém evidência de volume e qualidade.
- Mantém owner João Paulo (Champion/direção).
- Mantém a próxima ação de criar nova versão do briefing e repetir a janela.
- Mantém prazo e estado da próxima ação como pendente.

### `DEC-F2-002`

- Permanece `revogada`.
- Motivo, responsável e timestamp de revogação permanecem registrados.
- Não foi reaberta, apagada ou sobrescrita.

### Cadeia de rollback

A consulta direta confirmou:

```text
DEC-F2-004.previous_decision_id = DEC-F2-002
DEC-F2-002.status = revogada
DEC-F2-004.status = registrada
```

### `DEC-F2-003`

- Permanece `pendente` e `synthetic_only=true`.
- Foi criada pelo botão genérico durante a validação humana da F2-T05.
- Não possui `previous_decision_id`.
- Não faz parte da cadeia de rollback.
- Foi preservada como massa sintética transparente e não foi utilizada como evidência de CA-2-09.

## Evidências humanas reutilizadas

A autorização determinou que não fossem refeitos testes mutativos. Foram reutilizadas as provas humanas já aprovadas na F2-T05:

1. **RED:** clique isolado bloqueado e registro mantido pendente.
2. **GREEN:** decisão `Ajustar` com volume, qualidade, owner e próxima ação.
3. **Rollback:** decisão anterior revogada, preservada e sucedida por nova decisão vinculada.
4. **Reteste GREEN:** `DEC-F2-004` aceita após a correção do detector de evidência positiva.

O TDD determinístico da T05 permanece em **6/6**.

## Preservação das entregas anteriores

A leitura do estado real e das evidências oficiais confirmou:

- **Fase 1:** painel e fonte preservados; `demandas` permanece com 10 registros; nenhuma migration, regra, hook, RLS ou dado da Fase 1 foi alterado.
- **F2-T01:** briefings `EXP-F2-IN-001`, `EXP-F2-OUT-001` e `EXP-F2-RED-001` permanecem preservados com seus estados e versões.
- **F2-T02:** históricos, bloqueios e aprovações sintéticas permanecem preservados.
- **F2-T03:** `ATR-F2-IN-001`, `ATR-F2-OUT-001` e `ATR-F2-UNK-001` permanecem na fonte declarada, sem identidade multi-fonte.
- **F2-T04:** lote-fonte, dry-run, reconciliação, duplicidade, conflito e replay permanecem preservados; nenhum `T04-*` foi gravado em `demandas`.
- **F2-T05:** collection `decisoes_f2`, migration `0020`, hook exclusivo, fila, seção de decisão, registros e histórico permanecem preservados.

## Verificação de escopo

- Produto funcional alterado nesta task: **não**.
- Escrita funcional ou de dados no Skip durante a revalidação: **não**; após a leitura, foi atualizado somente o arquivo de estado de governança e consolidado o checkpoint documental autorizado (Skip v0.0.81).
- Nova migration/collection/campo/hook/RLS: **não**.
- Nova fixture ou decisão: **não**.
- Meta/RD Station/1CRM/Omie: **não**.
- F2-T07 iniciada: **não**.

## Veredito

Todos os critérios da F2-T06 foram revalidados com evidência observável e passaram:

- CA-2-07: **PASSOU**;
- CA-2-08: **PASSOU**;
- CA-2-09: **PASSOU**.

A F2-T06 está formalmente concluída como task de prova e fechamento documental. A próxima task elegível é a F2-T07, que permanece sem autorização e não foi iniciada.
