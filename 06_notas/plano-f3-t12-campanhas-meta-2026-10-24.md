# Plano de execução — F3-T12 (Campanhas Meta → Repositório Adapta) · SPEC F3-006

**Data:** 2026-10-24 · **Status:** PLANO — não implementado. Aguarda aprovação expressa do Champion.
**Autorização vigente:** somente análise e planejamento documental (ordem de 24/10 09:09). Nenhuma coleção criada, nenhum código alterado, nenhuma credencial movida.
**Ordem permanente:** o Hub 57113 permanece ATIVO durante todo o desenvolvimento e os testes, até autorização expressa do Champion para desligamento.

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

## 2. B3-META-LEITOR — definição e riscos

**O que é:** trava criada na 5ª call (22/10). Antes da F3-T12, é necessário que a conexão usada pela automação esteja alinhada ao princípio de menor privilégio. Duas opções:

| Opção | Como funciona | Riscos |
|---|---|---|
| **A. Leitor dedicado** (preferida) | Usuário nominal somente leitura na conta TalentGroup_01 (padrão já executado na F2-T09: Luiz Carlos Manni com "Ver desempenho"); ele conecta o OAuth no Maestro | Custo operacional de criar/gerenciar o usuário; exige aceite do usuário dedicado |
| **B. Principal atual com instrução** | Champion registra por escrito que aceita usar a conexão do principal João Paulo Oliveira com instrução estrita de somente leitura | O principal tem controle total — a instrução é de governança, não restrição técnica (risco registrado na F2-T09); qualquer desvio seria detectável no log da Meta |

**Riscos comuns:** a conexão herda as permissões de quem consente (AP-2026-09-23-1211); expiração de token é frequente na Meta — o design já trata (faixa + e-mail + reexecução); a agência externa (AYPLA) tem escrita na conta — não afeta a leitura, mas registra-se para rollback.

**Decisão pendente do Champion:** escolher A ou B. Sem essa decisão, a F3-T12 não inicia (trava formal da SPEC).

## 3. Procedimento seguro de autenticação (sem tokens no chat)

1. A conexão OAuth é feita pelo usuário escolhido na opção A/B, em tela de consentimento da Meta (padrão provado no Hub: consentimento → callback server-side → token gravado no backend do projeto).
2. O token fica em campo oculto do backend do 51414 (mesmo molde `meta_connections` do Hub 57113 — coleção com regras server-side). **Nunca** em chat, e-mail, changelog ou documento.
3. Se for preciso renovar manualmente (caso do token do MCP ETHOS hoje), o Champion executa a renovação na interface do sistema de conexão — não cola JSON no chat (condição da homologação da F3-T09).
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

**GREEN (caminho principal):** execução manual com conexão válida → snapshot gravado; números conferidos 1:1 com o Gerenciador de Anúncios na mesma data de referência (evidência: captura da tela × captura do Gerenciador).

**REGRESSÃO:** reexecutar 2x no mesmo dia → sem duplicação; abrir painel F1/F2 e demandas → intactos (10 registros preservados); log de transições intacto.

**Homologação:** teste humano do Champion (ler a tela, comparar com o Gerenciador, ver a faixa de saúde) + validação do consultor na primeira demonstração. A automação diária só entra em agendamento após a execução manual homologada.

## 7. Critérios para substituição do Hub 57113

O desligamento do Hub é decisão expressa do Champion e só se qualifica quando TODOS estiverem atendidos:

1. F3-T12 implementada e homologada (números iguais ao Gerenciador na data de referência);
2. F3-T13 concluída (falha de conexão gera faixa + e-mail sem apagar dados; reexecução não duplica; destino único; nenhuma escrita na Meta);
3. Automação diária rodando no 51414 com ao menos 3 dias consecutivos de snapshots sem falha;
4. Champion confirma que os relatórios diários que hoje recebe do Hub (11h, manni+jpaulo) estão cobertos pela nova tela/automação — ou define como ficará esse relatório;
5. Autorização expressa do Champion para desligar o Hub (ordem permanente de 23/10 e 24/10).

Enquanto isso, o Hub segue ativo e intocado (ordem reforçada hoje). O aproveitamento dos dados do Hub é histórico/consulta; a automação nova não lê nem escreve no Hub.

## 8. Plano de rollback

- **Automação:** desligar a automação no Maestro (1 clique) — nada mais é afetado.
- **Tela:** esconder a rota `campanhas` no app do 51414.
- **Coleções:** permanecem como histórico (nada é apagado); se necessário, rollback da migration remove apenas as duas coleções novas — `demandas`, `propostas`, `vagas` e o restante do projeto ficam intocados.
- **Meta:** nenhuma escrita é feita em nenhum cenário — não há o que reverter na Meta.
- **Falha de conexão:** o último snapshot bom permanece com a data; a próxima execução agendada tenta de novo (sem retry em sequência).

## 9. Critérios de aceite (das SPECs aprovadas — transcrição objetiva)

**F3-T12 · CA-3-16 (SPEC F3-006):** a tela Campanhas mostra as campanhas da conta com status, orçamento, gasto, impressões, cliques, resultados e hora da atualização, **iguais ao Gerenciador de Anúncios na mesma data de referência**, alimentada pela automação do Maestro que grava só no projeto oficial.

**F3-T13 · CA-3-16 + CA-3-17 (SPEC F3-006):** com a conexão inválida, a execução não grava snapshot novo, mantém o anterior, mostra a faixa de aviso e envia o e-mail; reexecutar com conexão válida não duplica linhas; **nenhuma escrita na Meta ocorre em nenhum cenário**.

---
*Plano preparado em 24/10/2026 pelo Maestro com autorização documental do Champion (somente planejamento). Nenhuma implementação iniciada. Aguarda aprovação para execução da F3-T12.*