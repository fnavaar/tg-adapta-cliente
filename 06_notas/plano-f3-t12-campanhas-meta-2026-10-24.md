# Plano de execução — F3-T12 (Campanhas Meta → Repositório Adapta) · SPEC F3-006

**Data:** 2026-10-24 · **Versão:** v2 (final) · **Status:** PLANO — não implementado. Arquitetura APROVADA CONCEITUALMENTE pelo Champion (24/10); B3-META-LEITOR decidido (Opção A); aguarda autorização específica de execução.
**Autorização vigente:** somente análise e planejamento documental. Nenhuma coleção criada, nenhum código alterado, nenhuma credencial movida.
**Ordem permanente:** o Hub 57113 permanece ATIVO e não pode ser desligado, modificado ou substituído sem aprovação expressa do Champion.

## 1. Arquitetura da integração Meta → Repositório Adapta

```
Meta Ads API (conta act_1667348577717128 — TalentGroup_01)
        │  leitura (somente métricas de campanha; B3-META-01)
        ▼
Automação agendada no Maestro (cron diário + execução manual sob demanda)
        │  1 tentativa por execução · timeout 60s · sem retry em sequência
        ▼
Projeto Skip 51414 "repositório adapta" — coleções campanhas_meta (snapshot diário) e conexao_meta (saúde)
        │  leitura por papéis
        ▼
Página "Campanhas" no app do 51414 (tela + faixa de saúde da conexão)
```

- **Fonte de verdade:** API Meta, lida pelo conector OAuth do Maestro (mesmo padrão do Google/Meta no Hub 57113 — OAuth server-side, token em campo oculto do backend, nunca no chat).
- **Destino único (RN-F3-026):** gravação exclusiva em `campanhas_meta`/`conexao_meta` do projeto oficial 51414. Nenhum outro projeto recebe dados.
- **Somente leitura na Meta (RN-F3-025):** qualquer pedido de escrita (ativar, pausar, orçamento, criativo) é recusado e registrado.
- **Sem dado pessoal (RN-F3-028):** campos de lead/contato na resposta são descartados e registrados (padrão RN-F2-012 provado na F2-T09).
- **Último dado bom preservado (RN-F3-027):** execução com falha não sobrescreve snapshot; a tela mostra a data do último dado.

**Campos por campanha (contrato da SPEC):** `campaign_id`, nome, status efetivo, objetivo, orçamento diário, início/fim, gasto, impressões, cliques, resultados, data de referência + `snapshot_em` e `execucao_id`.

## 2. B3-META-LEITOR — decisão do Champion e viabilidade

**Decisão (Champion, 24/10):** OPÇÃO A — leitor dedicado com permissões mínimas, exclusivamente de leitura.

**Viabilidade técnica: CONFIRMADA**, com base em três provas já executadas no projeto:
1. O padrão OAuth server-side está provado no ecossistema (google_auth/callback no Hub 57113 e conexão Meta server-side do Hub — sync funcionando em 23/10);
2. A F2-T09 provou que um leitor dedicado com permissão mínima "Ver desempenho" lê a conta TalentGroup_01 (gates 1–5 validados; leitura real executada em 23/09 com HTTP 200);
3. A coleção `conexao_meta` replica o molde `meta_connections` do Hub (token em campo oculto, regras server-side).

**Dependência operacional (ação humana, fora do sistema):** criação do usuário leitor dedicado na conta TalentGroup_01 e aceite do convite — ação do admin da conta (João Paulo/Champion). Sem isso, a conexão não pode ser estabelecida.

**Procedimento seguro de configuração (6 passos):**
1. Admin da conta cria o leitor dedicado com permissão mínima "Ver desempenho" (gerenciar campanhas e acesso total desligados);
2. Leitor aceita o convite da Meta;
3. Leitor executa o consentimento OAuth na tela do sistema — sem tokens no chat;
4. Callback server-side grava o token no campo oculto do backend do 51414;
5. Teste de leitura com os campos do contrato (campanhas + métricas) e conferência na tela;
6. Registro em `conexao_meta` (status ok, desde, ultima_execucao).

**Riscos residuais:** expiração do token (~60 dias) — tratada pela política da §12; o leitor dedicado herda as permissões que lhe forem concedidas (AP-2026-09-23-1211) — por isso a permissão mínima é verificada no passo 1; a agência externa (AYPLA) mantém escrita na conta — não afeta a leitura, registrado para rollback.

## 3. Procedimento seguro de autenticação (sem tokens no chat)

1. A conexão OAuth é feita pelo leitor dedicado (Opção A), em tela de consentimento da Meta (padrão provado no Hub: consentimento → callback server-side → token gravado no backend do projeto).
2. O token fica em campo oculto do backend do 51414 (mesmo molde `meta_connections` do Hub 57113 — coleção com regras server-side). **Nunca** em chat, e-mail, changelog ou documento.
3. Se for preciso renovar manualmente, o leitor dedicado refaz o consentimento na interface do sistema — não cola JSON no chat (condição da homologação da F3-T09).
4. O plano nunca lê, exibe ou transporta credenciais; hooks e automações acessam o token server-side.

## 4. Coleções e indicadores previstos

**`campanhas_meta`** (nova, migration não destrutiva): snapshot diário por campanha — `campaign_id` (chave de upsert com a data de referência), nome, status efetivo, objetivo, orçamento diário, início/fim, gasto, impressões, cliques, resultados, data de referência, `snapshot_em`, `execucao_id`. **Índice único** (`campaign_id` + data de referência) — lição direta das 163 duplicatas do Hub.

**`conexao_meta`** (nova, migration não destrutiva): saúde da conexão — `status` {ok, expirada, erro}, `desde`, `ultima_execucao`, `mensagem` curta. 1 registro por execução.

**Indicadores na tela Campanhas:** por campanha — status, orçamento, gasto, impressões, cliques, resultados, hora da atualização; contador de demandas no Funil cuja atribuição aponta para a campanha (quando o Funil existir — até lá, "sem ligação no funil"); faixa de saúde da conexão no topo.

**Volume × resultado separado (RN-F3-008 da SPEC-F3-002):** impressões/cliques aparecem como volume; "resultados" como resultado — nunca somados num único número.

## 5. Como evitar duplicidade de registros

- **Upsert por chave composta** (`campaign_id` + data de referência): reexecutar no mesmo dia atualiza a linha, não cria nova.
- **Índice único no banco** como garantia estrutural (não apenas lógica no hook).
- **`execucao_id`** em cada snapshot: rastreabilidade de qual execução gerou o dado.
- **Replay idempotente:** segunda execução com conexão válida no mesmo dia = 0 linhas novas (prova obrigatória da F3-T13).
- **Contraexemplo documentado:** `daily_metrics` do Hub tem `indexes: []` — sem índice único, acumulou 163 duplicatas em 204 registros. O plano replica o padrão de upsert da F2-T04/T08 (batch_id + replay idêntico skip), que passou nas homologações.

## 6. Estratégia de testes e homologação

**RED (falhas obrigatórias):** token inválido/expirado → faixa + e-mail, snapshot anterior intacto, sem gravação; destino errado simulado → execução recusada e reportada; campo pessoal na resposta → descartado e registrado; pedido de escrita na Meta → recusado e parado.

**GREEN (caminho principal):** execução manual com conexão válida → snapshot gravado; números conferidos 1:1 com o Gerenciador de Anúncios na mesma data de referência (evidência: captura da tela × captura do Gerenciador), conforme as regras de conciliação da §11.

**REGRESSÃO:** reexecutar 2x no mesmo dia → sem duplicação; abrir painel F1/F2 e demandas → intactos (10 registros preservados); log de transições intacto.

**Homologação:** teste humano do Champion (ler a tela, comparar com o Gerenciador, ver a faixa de saúde) + validação do consultor na primeira demonstração. A automação diária só entra em agendamento após a execução manual homologada.

## 7. Critérios para substituição do Hub 57113

O desligamento do Hub é decisão expressa do Champion e só se qualifica quando TODOS estiverem atendidos:

1. F3-T12 implementada e homologada (números iguais ao Gerenciador na data de referência, conforme §11);
2. F3-T13 concluída (falha de conexão gera faixa + e-mail sem apagar dados; reexecução não duplica; destino único; nenhuma escrita na Meta);
3. Automação diária rodando no 51414 com ao menos 3 dias consecutivos de snapshots sem falha — critérios objetivos na §13;
4. Champion confirma que as funcionalidades do Hub listadas na §10 (relatório diário, alertas) estão cobertas pela nova tela/automação — ou define como ficarão;
5. Autorização expressa do Champion para desligar o Hub (ordem permanente).

Enquanto isso, o Hub segue ativo e intocado (ordem reforçada). O aproveitamento dos dados do Hub é histórico/consulta; a automação nova não lê nem escreve no Hub.

## 8. Plano de rollback

- **Automação:** desligar a automação no Maestro (1 clique) — nada mais é afetado.
- **Tela:** esconder a rota `campanhas` no app do 51414.
- **Coleções:** permanecem como histórico (nada é apagado); se necessário, rollback da migration remove apenas as duas coleções novas — `demandas`, `propostas`, `vagas` e o restante do projeto ficam intocados.
- **Meta:** nenhuma escrita é feita em nenhum cenário — não há o que reverter na Meta.
- **Falha de conexão:** o último snapshot bom permanece com a data; a próxima execução agendada tenta de novo (sem retry em sequência).
- **Histórico do Hub:** preservação integral — detalhado na §14.

## 9. Critérios de aceite (das SPECs aprovadas — transcrição objetiva)

**F3-T12 · CA-3-16 (SPEC F3-006):** a tela Campanhas mostra as campanhas da conta com status, orçamento, gasto, impressões, cliques, resultados e hora da atualização, **iguais ao Gerenciador de Anúncios na mesma data de referência**, alimentada pela automação do Maestro que grava só no projeto oficial.

**F3-T13 · CA-3-16 + CA-3-17 (SPEC F3-006):** com a conexão inválida, a execução não grava snapshot novo, mantém o anterior, mostra a faixa de aviso e envia o e-mail; reexecutar com conexão válida não duplica linhas; **nenhuma escrita na Meta ocorre em nenhum cenário**.

---
**Continuação:** as seções 10–14 (inventário do Hub, conciliação, credenciais, 3 dias sem falha, rollback/histórico) estão no arquivo complementar: 06_notas/plano-f3-t12-complemento-v2-2026-10-24.md