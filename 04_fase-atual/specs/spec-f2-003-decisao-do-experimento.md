# SPEC-F2-003 — Decisão humana de continuar, ajustar ou interromper

**Fase:** 2  
**Status:** liberada para execução — F2-T05 e F2-T06 concluídas e validadas em 2026-09-21; decisor: João Paulo (Champion/direção)  
**Dono:** direção/marketing decide; consultor valida o primeiro ciclo  
**Origem no escopo:** Fase 2, C-02, C-04, DC-007, G-001, G-006  
**Degrau da solução:** reuso dos dados atribuídos pela F2-002 e registro mínimo de decisão — não automatiza otimização nem muda orçamento.

## Contexto e decisões fechadas

- **Estado atual:** o escopo exige decisão baseada em qualidade, não clique/abandono isolado; meta/capacidade não podem ser inferidas.
- **Estado desejado:** cada experimento encerrado recebe uma decisão humana, sua evidência e próxima ação, preservando a hipótese/versão avaliada.
- **Decisões já fechadas:** opções são continuar, ajustar ou interromper; o agente não decide, publica ou muda orçamento.
- **Decisor (registrado em 2026-09-17):** João Paulo, Champion/direção — confirmado pelo Champion após a regularização documental.
- **Critério de decisão:** conforme RN-F2-008, é definido no briefing de cada experimento — na prova sintética da T05, o briefing sintético; decisão real de experimento real continua exigindo critério real definido no briefing.
- **Bloqueios:** ausência de critério de decisão definido antes da execução impede encerrar o experimento como sucesso/fracasso.

## Resultado observável

Um `DEC-F2-###` vincula experimento, período, evidência de volume e qualidade, leitura do responsável, decisão, dono, próxima ação e data. Um resultado vazio, insuficiente ou divergente resulta em `pendente de decisão`, não em conclusão positiva.

## Limites e dependências

- **Inclui:** formulário/registro de decisão, ligação ao relatório F2-002, regra contra decisão por clique isolado e roteiro de revisão.
- **Fora de escopo:** recomendação/pontuação automática, mudança de orçamento, publicação, meta numérica inferida ou avaliação de capacidade.
- **Entradas e pré-condições:** F2-001 e F2-002 com ID, período e critério de decisão; decisor identificado.
- **Saídas/artefatos:** decisão assinada/registrada e fila de próxima ação ou pendência.
- **Atores e permissões mínimas:** marketing propõe leitura; direção aprova decisão que envolva gasto/canal; consultor revisa primeiro ciclo.
- **Superfícies afetadas:** registro/relatório interno; sem conector externo.
- **Risco e plano B:** dado insuficiente não interrompe/continua automaticamente; registrar pendência e nova janela ou coleta manual aprovada.
- **Rollback:** reabrir decisão como `revogada`, preservar versão anterior e motivo; não apagar o resultado.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| relatório F2-002 → decisão | relatório reconciliado ou lacuna registrada | experimento_id, período, volume, qualidade, divergências, critério | leitura marketing/direção | mesmo `DEC-F2` atualiza versão com motivo | fonte ausente mantém pendente |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F2-008 | decisão sem critério prévio ou evidência | bloquear fechamento | registrar pendência com owner | Fase 2 |
| RN-F2-009 | evidência contém só clique/abandono | não permite declarar qualidade/sucesso | pode ser anexada como atividade | Fase 2 regras |
| RN-F2-010 | decisor escolhe ajustar/interromper | registrar próxima ação e estado anterior | nova execução requer novo briefing/versão | DC-007 |

## Fluxo e regras

1. Marketing apresenta o resultado reconciliado e critério definido no briefing.
2. Direção/owner registra continuar, ajustar, interromper ou pendente.
3. Ajustar exige nova versão na F2-001; interromper pausa somente o experimento; continuar não publica nem altera orçamento por si.
4. Decisão e evidência ficam disponíveis para o próximo ciclo.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | qualidade e volume reconciliados | decisão registrada, com próxima ação | ciclo posterior usa nova versão quando aplicável |
| Limite | amostra insuficiente | pendente, dono e data de revisão | não inferir sucesso |
| Falha | pedido de otimização automática | bloqueado | encaminhar à direção para decisão humana |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** escopo §1 indicadores, §7 F2, §8 e G-001/G-006; briefing F2-001 e relatório F2-002.
2. **Alterar somente:** registro de decisão e fila de próxima ação.
3. **Não alterar:** orçamento, publicação, Meta, estágio de pipeline ou critérios de qualidade já aprovados.
4. **Executar nesta ordem:** criar fixture → testar bloqueio → registrar decisão humana → demonstrar rollback/revogação.
5. **Parar e pedir validação quando:** o critério estiver ausente, houver gasto/canal novo ou alguém pedir decisão automática.
6. **Estado válido ao parar:** experimento continua pausado/pendente e evidência fica preservada.

## Checklist de execução

- [ ] Decisão sempre aponta para briefing, período e evidência.
- [ ] Clique isolado não encerra hipótese como sucesso.
- [ ] Ajuste cria versão nova; interrupção preserva histórico.
- [ ] Dono e próxima ação ficam visíveis.

## Critérios de aceite

- [ ] **CA-2-07:** um experimento possui decisão humana de continuar, ajustar ou interromper vinculada a evidência de qualidade e volume.
- [ ] **CA-2-08:** resultado incompleto ou só de clique fica pendente e não é apresentado como êxito.
- [ ] **CA-2-09:** ajuste ou revogação preserva a decisão/versão anterior e aponta a próxima ação.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | `DEC-F2-RED-001` com clique e sem critério | tentar concluir | bloqueado/pendente | captura/log |
| GREEN | `DEC-F2-001` com relatório F2-002 reconciliado | decisor registra ajustar | decisão, owner e nova ação visíveis | registro + demonstração |
| REFACTOR/REGRESSÃO | revogar decisão e criar versão subsequente | consultar histórico | decisão anterior preservada; sem publicar | comparação/histórico |

**Dados/fixtures:** decisões sintéticas sem contatos reais.  
**Caminhos de erro obrigatórios:** amostra insuficiente, métrica ausente, divergência, pedido automático.  
**Evidência exigida:** decisão humana registrada, relatório referenciado e roteiro demonstrado.

## Handoff e operação

- **Como demonstrar:** abrir uma decisão válida e uma pendente, comprovando que clique não é qualidade.
- **Como operar depois:** marketing prepara leitura; direção decide; comercial devolve qualidade quando disponível.
- **Como monitorar:** decisões sem evidência, experimentos sem decisão e prazo de revisão vencido.
- **Pendência conhecida:** meta e capacidade seguem sujeitas aos gates do escopo.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F2-T05 | Materializar o registro de decisão e a fila de próxima ação para um experimento já reconciliado. | Direção/marketing | F2-003 | RN-F2-008, RN-F2-010 | Dados e integrações; Fluxo e regras; Checklist | Captura/export do registro e permissões de decisão. | F2-T04 aceita; decisor identificado. | Concluída e validada em 2026-09-21 |
| F2-T06 | Provar decisão baseada em qualidade e o histórico de ajuste/revogação. | Direção/marketing | F2-003 | CA-2-07, CA-2-08, CA-2-09 | Critérios de aceite; TDD da SPEC | Decisão humana, relatório referenciado e histórico de revogação/versão. | F2-T05 aceita por teste humano. | Concluída e validada em 2026-09-21 — revalidação somente leitura; critérios aprovados sem alteração funcional |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
| 2026-09-17 | Champion (João Paulo) — confirmação positiva pós-regularização | F2-T05 | Registrar decisor e liberar a execução da task |
| 2026-09-21 | Champion (João Paulo) — autorização expressa para prova, revalidação somente leitura e fechamento documental | F2-T06 | Fechar CA-2-07/08/09 com as evidências homologadas da F2-T05, sem nova implementação |
