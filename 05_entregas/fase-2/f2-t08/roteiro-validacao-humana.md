# F2-T08 — roteiro de validação humana

**Preview:** https://repositorio-adapta-cc556--preview.goskip.app/atribuicao-t04  
**Importante:** executar um teste por vez. Não concluir a task automaticamente e não iniciar a F2-T09.

## Teste 1 — T04 preservada e pipeline sem mutação

1. Abrir o preview e aguardar o carregamento do pipeline.
2. Na seção **F2-T04 · Atribuição**, clicar em **Executar lote sintético**.
3. Conferir a caixa **Verificações determinísticas**.
4. Confirmar os sete itens com ✓ e a mensagem **PASSOU — todas as verificações determinísticas da T04**.
5. Confirmar `pipeline vivo preservado em 10 registros` e `criações no replay 0`.

**Resultado esperado:** T04 continua 7/7; pipeline consultado permanece em 10; nenhuma ação é executada contra `demandas`.

**Como reconhecer falha:** qualquer check vermelho; pipeline diferente de 10; criação efetiva; ausência da mensagem de proteção de escopo.

Pare e informe o resultado do Teste 1. Só depois será apresentado o Teste 2.

## Teste 2 — lote manual e classificações

Após o Teste 1 aprovado:

1. Rolar até **F2-T08 · prova sintética do fallback manual**.
2. Clicar em **Executar prova T08**.
3. Confirmar `META-F2-MANUAL-001`, `source_mode: manual_export`, 5 linhas e ausência de dados pessoais.
4. Conferir as cinco classificações: Vinculado, Não vinculado, Desconhecido, Divergente e Inválido.
5. Confirmar **PASSOU — TDD sintético da F2-T08**.

**Resultado esperado:** lote processado em memória, sem Meta e sem escrita em `demandas`.

## Teste 3 — replay e conflito

Após o Teste 2 aprovado:

1. Conferir `Replay idêntico: replay_skip` e zero novas ações.
2. Conferir o bloco de mesmo `batch_id` com payload diferente.
3. Confirmar `payload_conflict`, estado `bloqueada` e “decisão humana necessária”.

## Teste 4 — falhas simuladas

Após o Teste 3 aprovado:

1. Conferir os cinco blocos 401, 403, 429, timeout e payload inválido.
2. Confirmar que cada bloco contém `SIMULADO · sem chamada externa · sem retry automático`.
3. Confirmar `fallback_manual` em 401/403/429/timeout e `bloqueada` em payload inválido.

## Teste 5 — regressão final e proteção de escopo

Após o Teste 4 aprovado:

1. Voltar ao painel ou atualizar a rota.
2. Confirmar que `demandas` continua com 10 registros.
3. Confirmar que T04 continua 7/7.
4. Confirmar que não apareceu Meta integrada, token/OAuth, dado real, lead ou contato.
5. Confirmar que F2-T01–T07 continuam preservadas.

Depois dos cinco testes, o Champion deve declarar explicitamente se aprovou a F2-T08 ou apontar a falha para o ciclo de correção. Até lá, a task permanece aberta.
