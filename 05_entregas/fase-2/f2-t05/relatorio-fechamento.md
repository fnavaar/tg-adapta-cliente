# Atendimento e fechamento — F2-T05

**Data do fechamento:** 2026-09-21  
**Task:** F2-T05 — Materializar o registro de decisão e a fila de próxima ação para um experimento já reconciliado  
**Champion:** João Paulo  
**SPEC de referência:** F2-003 — Decisão humana de continuar, ajustar ou interromper  
**Resultado:** CONCLUÍDA — validação humana aprovada, 3/3 testes aprovados + reteste do GREEN após correção do detector.

## Escopo entregue

A entrega ficou exatamente no recorte autorizado para a F2-T05:

- collection `decisoes_f2` criada pela migration `0020_f2_t05_decisoes` (única collection nova da task);
- estados `pendente`, `registrada` e `revogada`; decisões exclusivamente `continuar`, `ajustar` e `interromper` (sem `inconclusivo`);
- hook exclusivo `pocketbase/hooks/decisoes_f2.js` com invariantes de decisão humana (nascce pendente, clique isolado bloqueado, AJUSTAR exige nova versão, revogação exige motivo e preserva histórico);
- seção **Decisão de Marketing** no detalhe do experimento (`/experimentos/:id`);
- fila de decisões e próximas ações em `/decisoes-f2`;
- permissões: decisão/revogação restritas a Champion/Delegado F2; exclusão bloqueada;
- fixtures sintéticas: `DEC-F2-RED-001` (pendente), `DEC-F2-001` (ajustar), `DEC-F2-ROLLBACK-001` (continuar);
- associação ao relatório/lote da T04 apenas como referência explícita sintética/manual, sem atribuição real entre campanha e demanda.

Não houve Meta, RD Station, 1CRM, Omie, dado real, publicação, alteração de orçamento, execução automática de próxima ação, relação estrutural `demandas` ↔ `experimentos_f2`, identidade global, alteração em `demandas` ou na T04.

## Implementação técnica

- Migration: `0020_f2_t05_decisoes` (aplicada em 2026-09-17T23:12Z).
- Hook exclusivo: `pocketbase/hooks/decisoes_f2.js` (nenhum hook existente alterado).
- Serviço: `src/services/decisoesF2.ts`; regras: `src/lib/f2/t05/rules.ts`; tipos: `src/lib/f2/t05/types.ts`.
- Componentes: `src/components/f2/DecisaoMarketingSection.tsx`; páginas: `src/pages/DecisoesF2Page.tsx` (nova rota) e integração mínima em `src/pages/ExperimentosF2.tsx`.
- Skip funcional da entrega: **v0.0.78**, hash **`2a06902`** (versão corrente do projeto: v0.0.79, `d42864c`).
- QA oficial: setup, análise estática, build, integrações e testes passaram em todos os applies.

## Validação humana — 3/3 aprovados + reteste do GREEN

### Teste 1 — RED (18/09, aprovado)

Com `DEC-F2-RED-001` pendente e decisão `Continuar` selecionada, o sistema bloqueou o registro com a mensagem específica de que clique/impressão/abandono isolado não prova qualidade ou sucesso. Nada foi registrado; a decisão permaneceu pendente.

### Teste 2 — GREEN (18/09, aprovado)

Nova pendência criada no `EXP-F2-IN-001` e decisão `Ajustar` registrada com evidência de volume e qualidade, próxima ação apontando nova versão do briefing. Mensagem verde de confirmação; `DEC-F2-001` intacta.

### Teste 3 — Rollback (18/09, aprovado)

`DEC-F2-002` revogada com motivo, preservada no histórico sem exclusão; decisão subsequente criada pelo botão específico do card revogado.

### Reteste do GREEN (21/09, aprovado)

Após a segunda rodada de debug (detector), o Champion registrou `DEC-F2-004` com `Ajustar`, volume `12 cliques; 3 capturas sintéticas` e qualidade `1 lead qualificado sintético; 0 oportunidades`. Registro aceito sem bloqueio; backend confirmou `previous_decision_id = DEC-F2-002` e `DEC-F2-002` preservada como revogada.

## Prova de rollback (backend, 21/09)

- `DEC-F2-004`: `registrada` / `ajustar` / `previous_decision_id = DEC-F2-002`.
- `DEC-F2-002`: `revogada` / `ajustar`, com justificativa e revogação preservadas; nada apagado.
- `DEC-F2-003`: `pendente`, sem vínculo — criada pelo botão genérico durante o teste; permanece na massa sintética sem alteração (transparência registrada; nenhuma regra oficial determina remoção).
- `DEC-F2-RED-001`, `DEC-F2-001` e `DEC-F2-ROLLBACK-001`: fixtures intactas.

## Debugs registrados

1. `06_notas/debug/debug-2026-09-18-f2-t05-decisao-subsequente.md` — botão `Criar próxima decisão` ausente no card revogado (serviço existia; import/render condicional faltavam). Corrigido em v0.0.77/89a2614.
2. `06_notas/debug/debug-2026-09-18-f2-t05-detector-red-green.md` — detector tratava `0 oportunidades` como ausência de qualidade mesmo com `1 lead qualificado sintético`; TDD visível 4/6 na revalidação de fechamento. Corrigido em v0.0.78/2a06902 (bloqueio apenas sem evidência positiva de qualidade); TDD 6/6.

## Regressão e preservação

- Fase 1 preservada: painel `/` com 10 registros, fonte 10, diferença 0, reconciliação PASSOU.
- F2-T01/T02 preservadas: `EXP-F2-IN-001`/`EXP-F2-OUT-001` em `Aprovado para preparação`; `EXP-F2-RED-001` em `Rascunho`.
- F2-T03 preservada: fixtures ATR intactas em `demandas` (10 registros, sem `T04-*`).
- F2-T04 preservada: lote 17, pipeline 10, sem escrita em `demandas`.
- Migrations: única migration nova da task é a `0020`; nenhuma collection ou campo existente alterado.
- Nenhuma integração externa, publicação, orçamento ou automação.

## Evidências

- Fila de decisões: https://repositorio-adapta-cc556--preview.goskip.app/decisoes-f2
- Detalhe com seção de decisão: https://repositorio-adapta-cc556--preview.goskip.app/experimentos/EXP-F2-IN-001
- Painel de regressão: https://repositorio-adapta-cc556--preview.goskip.app/
- Versão funcional: Skip v0.0.78, hash `2a06902` (corrente v0.0.79, `d42864c`).
- Evidências humanas: capturas/PDFs anexados pelo Champion no canal da validação (RED 18/09, GREEN 18/09, rollback 18/09, reteste GREEN 21/09).
- Fonte de governança: `04_fase-atual/fase.md`, `STATUS.md`, `changelog.md`, matriz e estado persistente.

## Critério de fechamento

Todos os critérios observáveis da linha F2-T05 foram revalidados do zero (CA-2-07/08/09 cobertos pela entrega e provas; TDD 6/6; QA oficial aprovado; rollback provado no backend) e o Champion aprovou expressamente os 3 testes humanos e o reteste do GREEN. A F2-T05 está formalmente concluída.

Nenhuma task posterior foi iniciada. F2-T06 e F2-T07 permanecem elegíveis e aguardam autorização expressa.
