# Atendimento e fechamento — F2-T05

**Data do fechamento:** 2026-09-21  
**Task:** F2-T05 — Materializar o registro de decisão e a fila de próxima ação para um experimento já reconciliado  
**Champion:** João Paulo  
**SPEC de referência:** F2-003 — Decisão humana de continuar, ajustar ou interromper  
**Resultado:** CONCLUÍDA — validação humana aprovada (3/3 testes + reteste GREEN pós-correção).

## Escopo entregue

A entrega ficou exatamente no recorte autorizado para a F2-T05:

- collection `decisoes_f2` (migration `0020_f2_t05_decisoes`): `decision_id` único, `experiment_id`, `briefing_version`, período, snapshot do critério, evidências (referência, modo, snapshot, volume, qualidade, divergências), leitura do responsável, decisão (`continuar`/`ajustar`/`interromper`), status (`pendente`/`registrada`/`revogada`), justificativa, decisor (label, relação e data), dono/próxima ação/responsável/prazo/status/evidência da ação, `previous_decision_id`, revogação (motivo, por, data) e `synthetic_only`;
- índices: `decision_id` único, (experimento, status) e (status da ação, prazo);
- regras de acesso: leitura autenticada; criação somente como `pendente`; atualização restrita a Champion/Delegado F2; exclusão bloqueada;
- hook exclusivo `pocketbase/hooks/decisoes_f2.js` com os invariantes de transição (pendente sem decisão final; registrada exige decisão válida, campos obrigatórios, qualidade positiva e AJUSTAR apontando nova versão; revogada somente a partir de registrada e com motivo; revogada não reabre);
- seção **Decisão de Marketing** em `/experimentos/:id` (cards por decisão, formulário com rolagem automática, revogação com motivo obrigatório, botão "Criar próxima decisão" no card revogado);
- fila `/decisoes-f2` (contadores por status, filtros, ações atrasadas e TDD determinístico visível);
- fixtures sintéticas: `DEC-F2-RED-001` (pendente), `DEC-F2-001` (registrada/ajustar) e `DEC-F2-ROLLBACK-001` (registrada/continuar);
- serviço `src/services/decisoesF2.ts`, regras `src/lib/f2/t05/rules.ts` e tipos `src/lib/f2/t05/types.ts`.

Não houve: relação com `demandas`, identidade global, Meta, RD Station, 1CRM ou Omie, publicação, alteração de orçamento, execução automática de próxima ação, decisão "inconclusivo", clique tratado como qualidade, alteração na T04 ou nas telas homologadas (apenas acréscimos de rota, navegação e seção).

## Implementação técnica

- Skip funcional: **v0.0.78**, hash **`2a06902`**.
- QA oficial: setup, análise estática, build, integrações e testes passaram.
- Migrations: somente a `0020`; nenhuma collection existente foi alterada.
- Hook: apenas para `decisoes_f2`; hooks existentes intactos.
- Histórico de versões da task: v0.0.70 (build falho por import), v0.0.71 (QA verde; migration não reenviada), v0.0.72 (migration 0020 aplicada), v0.0.73 (navegação da fila), v0.0.74 (criação de decisão subsequente), v0.0.75 (bloqueio RED explícito), v0.0.76 (rolagem automática), v0.0.77 (botão de próxima decisão), v0.0.78 (detector de qualidade positiva).

## TDD determinístico — 6/6 aprovadas (v0.0.78)

1. RED clique isolado permanece pendente.
2. GREEN com volume e qualidade permite AJUSTAR.
3. Somente continuar, ajustar e interromper são aceitas.
4. AJUSTAR aponta nova versão do briefing.
5. Revogação preserva a decisão anterior.
6. Decisão subsequente aponta para a anterior.

## Validação humana — 3/3 aprovados + reteste do GREEN

### Teste 1 — RED (18/09, 10:38)

Aprovado pelo Champion. Com `Continuar` selecionado e evidência somente de clique/atividade, o registro foi bloqueado com a mensagem específica de que clique/impressão/abandono isolado não prova qualidade; `DEC-F2-RED-001` permaneceu pendente e nada foi registrado.

### Teste 2 — GREEN (18/09, 10:47)

Aprovado pelo Champion. Pendência criada em `EXP-F2-IN-001` e decisão `Ajustar` registrada com evidência de volume e qualidade; mensagem "Decisão registrada." exibida; `DEC-F2-002` confirmada como Registrada/Ajustar no backend, com próxima ação apontando nova versão do briefing.

### Teste 3 — Rollback (18/09, 11:35)

Aprovado pelo Champion. `DEC-F2-002` revogada com motivo, preservada sem exclusão; o botão específico criou `DEC-F2-004` pendente com `previous_decision_id = DEC-F2-002` e próxima ação "Registrar nova leitura humana após revisão." — confirmado no backend.

### Reteste do GREEN (21/09)

Após a correção do detector (v0.0.78), o Champion registrou `DEC-F2-004` como `Ajustar` com evidência "1 lead qualificado sintético; 0 oportunidades" — aceita corretamente, sem o falso bloqueio. Confirmado no backend: `DEC-F2-004` registrada/ajustar com vínculo `DEC-F2-002` preservado.

## Correções durante a validação (debug)

1. **v0.0.76** — o formulário de decisão abria abaixo da dobra; adicionada rolagem automática até o formulário.
2. **v0.0.77** — o botão "Criar próxima decisão" não renderizava no card revogado (import e bloco condicional ausentes no componente).
3. **v0.0.78** — o detector tratava "0 oportunidades" como ausência total de qualidade mesmo com "1 lead qualificado sintético"; corrigido para exigir ausência de evidência positiva (lead qualificado, oportunidade, proposta, conversão, cliente) antes de bloquear.

Todas com QA completo aprovado. Notas em `06_notas/debug/debug-2026-09-18-f2-t05-*.md`.

## Transparência — DEC-F2-003

`DEC-F2-003` foi criada durante o Teste 3 pelo botão genérico "Criar pendência de decisão", sem `previous_decision_id` e com próxima ação padrão. Ela permanece na massa sintética como pendente, **sem exclusão ou alteração** — nenhuma regra oficial determina sua remoção e a preservação mantém a trilha de auditoria honesta.

## Regressão e preservação (revalidação de fechamento, 21/09)

- Fase 1 preservada: painel `/` com 10 registros, fonte 10, diferença 0, PASSOU.
- F2-T01/T02 preservadas: `EXP-F2-IN-001` e `EXP-F2-OUT-001` "Aprovado para preparação"; `EXP-F2-RED-001` "Rascunho".
- F2-T03 preservada: fixtures ATR visíveis no painel.
- F2-T04 preservada: lote 17, pipeline 10, sem escrita em `demandas`; superfície intacta.
- Collection `demandas`: 10 registros; nenhum `T04-*` ou `T05-*` gravado.
- Collection `decisoes_f2`: 6 registros vivos; cadeia `DEC-F2-004 → DEC-F2-002` íntegra.
- Nenhuma integração externa; nenhuma publicação; nenhum orçamento alterado; nenhuma atribuição sintética apresentada como real.

## Pendências preservadas

1. A pendência arquitetural de identidade técnica/multi-fonte permanece para tasks posteriores.
2. `record_id` continua restrito à fonte declarada.
3. O `.skip.config.json` preexistente (`deployment.lastDevBuildRef`) segue como metadado de build, sem efeito funcional.
4. O critério real de decisão (RN-F2-008) permanece exigido para experimentos reais — a T05 provou o mecanismo com briefing sintético.
5. `DEC-F2-003` permanece na massa sintética sem vínculo, por transparência.

## Evidências

- Preview funcional: https://repositorio-adapta-cc556--preview.goskip.app/decisoes-f2
- Detalhe com decisão: https://repositorio-adapta-cc556--preview.goskip.app/experimentos/EXP-F2-IN-001
- Painel de regressão: https://repositorio-adapta-cc556--preview.goskip.app/
- Versão funcional: Skip v0.0.78, hash `2a06902`; migration `0020` aplicada em 2026-09-17T23:12Z.
- Evidências humanas: capturas/PDFs anexados pelo Champion no canal (RED, GREEN, rollback e reteste GREEN).
- Backend: 6 decisões confirmadas via API autenticada durante a revalidação.
- Fonte de governança: `04_fase-atual/fase.md`, `STATUS.md`, `changelog.md`, matriz e estado persistente.

## Critério de fechamento

- **CA-2-07:** decisão humana de continuar/ajustar/interromper vinculada a evidência de volume e qualidade — atendido (DEC-F2-002 e DEC-F2-004 registradas com evidências).
- **CA-2-08:** resultado incompleto ou só de clique fica pendente e não é apresentado como êxito — atendido (RED bloqueado; pendências preservadas).
- **CA-2-09:** ajuste ou revogação preserva a decisão/versão anterior e aponta a próxima ação — atendido (rollback provado com vínculo no backend).

Todos os critérios observáveis foram revalidados do zero, o QA oficial passou, o TDD determinístico está 6/6 e o Champion aprovou expressamente os testes humanos, incluindo o reteste do GREEN após a correção. A F2-T05 está formalmente concluída.

Nenhuma task posterior foi iniciada. F2-T06 e F2-T07 permanecem elegíveis, aguardando autorização expressa.
