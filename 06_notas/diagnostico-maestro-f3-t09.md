# Diagnóstico Maestro — F3-T09 (SPEC F3-006, CA-3-15)

**Data:** 2026-10-23 · **Executado por:** Maestro (ETHOS) · **Natureza:** somente leitura — nenhuma automação, integração, banco, campanha ou configuração foi alterada.
**Autorização:** Champion/owner em 23/10/2026 16:04 — "autorizo a execução documental da F3-T09, conforme o plano apresentado, exclusivamente para diagnóstico e registro das evidências".
**Ordem expressa registrada:** a automação do Hub 57113 **permanece ATIVA** até que exista solução substituta implementada, testada e expressamente aprovada pelo Champion (F3-T12/T13 + homologação).

## 1. Automações ativas e destinos

### 1.1 ETHOS (ambiente do assistente) — 4 agendamentos, nenhum grava em projeto Skip

| # | Automação (cron ETHOS) | Cadência | O que lê | O onde grava / entrega |
|---|---|---|---|---|
| 1 | Relatório semanal (Gmail) | sexta 08:00 | conteúdo do relatório | e-mail via Gmail (conta talentgroupepress) |
| 2 | Lembrete LinkedIn — convites B2B | dias úteis 09:00 | fila de convites pendentes | mensagem no chat |
| 3 | Maestro: checar avisos do watchdog | diária 12:00 | logs do Hub 57113 | mensagem no chat |
| 4 | Renovar tokens Meta (Hub + MCP) | one-time 01/12/2026 | — | lembrete no chat |

**Verificação:** `cron list` executado em 23/10/2026 — 4 jobs, todos de leitura/notificação; nenhum escreve em coleções de qualquer projeto Skip.

### 1.2 Hub de Gestão — projeto Skip 57113 (automations internas do projeto)

| Automação | Cadência | O que lê | Onde grava / entrega | Estado hoje |
|---|---|---|---|---|
| `maestro_daily` | diária 11:00 UTC (08:00 BRT) | Meta Ads (conta `act_1667348577717128`, TalentGroup_01) via token longo do Hub | coleções do próprio Hub (`maestro_runs`, `daily_metrics`, `maestro_recommendations`) + e-mail HTML aos destinatários (manni@ + jpaulo@) + post no chat do Genie | **ATIVA** — execução de hoje 11:00:14 status ok (13,4 s); 2 e-mails enviados 11:00 ("Maestro · Relatório de tráfego — 22/10/2026") |
| `maestro_watchdog` | a cada 15 min | recomendações pendentes no Hub | aviso no chat do Genie + e-mail 1x/dia | **ATIVA** — 20+ execuções hoje, todas status ok |

**Nota de escopo:** o Hub 57113 é infraestrutura separada do projeto oficial "repositório adapta" (51414). O `maestro_daily` grava somente nas coleções do próprio Hub — **não** grava em `demandas`/coleções do 51414 (verificado na auditoria de 20/10: zero referências cruzadas no código `meta_ads_sync.js` e `maestro_engine.js`).

### 1.3 Landing Panorama — projeto Skip 67634

| Automação | Gatilho | O que faz | Estado |
|---|---|---|---|
| hook `panorama_email.js` | novo registro na coleção `leads` | envia o Panorama TG 2026 por e-mail ao próprio lead | **ATIVA** — código lido hoje no projeto 67634 |

## 2. Estado da automação do Hub (pedido da call de 22/10: "parar")

**Fato verificado hoje (23/10):** a automação do Hub **NÃO está parada** — `maestro_daily` rodou às 11:00 com sucesso e o watchdog segue a cada 15 min.

**Decisão do Champion registrada em 23/10/2026 16:04:** a automação do Hub 57113 **permanece ativa até que exista uma solução substituta implementada, testada e expressamente aprovada por ele** (a substituta prevista é a automação da F3-T12, que gravará somente no projeto oficial "repositório adapta").

**Consequência para o CA-3-15:** o critério pede "confirma a parada da automação do Hub". O registro correto hoje é: **parada NÃO confirmada — por decisão expressa do Champion** (manter ativa até a substituta aprovada). A confirmação da parada fica condicionada à F3-T12/T13 e à homologação do Champion; o critério CA-3-15 fica **parcial** até lá, sem falha atribuída à task.

## 3. Destino do formulário da landing page (67634)

**Evidência técnica (código do hook `panorama_email.js`, lido hoje no projeto 67634):**

1. Todo envio do formulário grava um registro na **coleção `leads` do próprio projeto 67634** (campos de lead + 4 campos UTM capturados na landing — migration 0004, homologada em v0.0.29/0.0.30).
2. O hook dispara o e-mail automático do Panorama **exclusivamente ao próprio lead** (SMTP talentgroupepress@gmail.com).
3. **Nenhuma integração com o funil comercial:** o lead não chega às coleções `demandas`/`propostas`/`vagas` do projeto oficial 51414, não há notificação interna ao time e não há encaminhamento automático.
4. **Sem destino externo:** não há envio do dado para fora do ecossistema Skip (nada vai para RD Station, 1CRM ou terceiros).

**Registro exigido pelo Champion (ordem de 23/10 16:04):** o armazenamento dos leads na coleção do projeto 67634 **não equivale à integração com o funil comercial**. Embora o destino técnico esteja identificado, a **ausência de notificação interna e de encaminhamento automático continua sendo pendência operacional** — será resolvida pela etapa E4 (ponte landing → demandas, com UTM→atribuição), que depende de decisão de LGPD (B3-LGPD-01) antes de mover dado real de contato.

**Veredito do critério de parada:** destino de leads **conhecido e dentro do ecossistema oficial** — **não há BLOQUEIO ao consultor** (o gatilho de bloqueio da SPEC é destino desconhecido ou fora do projeto oficial).

## 4. Campanhas Meta da conta TalentGroup_01 (act_1667348577717128)

**Estado da conexão em 23/10:**

- **Hub 57113: conexão VÁLIDA** — o `maestro_daily` de hoje leu a conta TalentGroup_01 sem erro (execução ok às 11:00; e-mails do relatório enviados).
- **Conector MCP (ETHOS): token EXPIRADO** — leitura direta retornou erro 401 ("Session has expired on Monday, 19-Oct-26"); limitação registrada, não bloqueia o diagnóstico (a leitura válida está no Hub).

**Lista de campanhas (via leitura do Hub de hoje; confirmação nominal pendente de renovação do token MCP):**

| Campanha | ID | Status (conhecido) | Observação |
|---|---|---|---|
| [TG] [R&S] [LEADS] [16/10/2026] | 120256095953380628 | encerrada 19/10 (anúncio reprovado 17/10 — categoria "Anúncios de cadastro") | sync do Hub ainda a lê como ACTIVE → gera recomendação falsa-positiva diária (rejeitada 2x no Dashboard) |
| [TG] [TESTE] [PANORAMA] | 120256141741190628 | ativa (adset reativado pelo JP em 20/10) | teste de tráfego R$20/dia → landing Panorama; avaliação 26/10 |

**Limitação registrada:** a lista nominal com status efetivo atual de cada campanha exige o token do MCP renovado (o Luiz cola o JSON `{"access_token":...}` no chat) ou a execução manual da leitura pelo Hub. O relatório registra a limitação sem inventar dados.

## 5. Pendências operacionais apontadas pelo diagnóstico

1. **Leads sem integração com o funil** (67634 → 51414): pendência operacional declarada pelo Champion — ponte E4 + decisão LGPD (B3-LGPD-01).
2. **Automação do Hub ativa por decisão** — substituição na F3-T12/T13 com homologação do Champion; CA-3-15 parcial até lá.
3. **Token MCP da Meta expirado desde 19/10** — renovação pelo Champion (colar o JSON no chat); lembrete one-time de 01/12 cobre o token longo do Hub.
4. **Duplicatas em `daily_metrics` do Hub (163)** — conhecidas, fora do escopo da T09; correção pedida ao sistema.
5. **Recomendação falsa-positiva da campanha LEADS encerrada** — recorre diariamente; arquivar a campanha na Meta via painel mata o falso positivo (ação na Meta, fora do escopo da T09).

## 6. Evidências coletadas (23/10/2026)

- `cron list` (ETHOS): 4 jobs — relatório semanal sexta 8h; lembrete LinkedIn dias úteis 9h; checagem Maestro diária 12h; renovação tokens one-time 01/12.
- Logs do Hub 57113 (source=crons): `maestro_daily` finished ok 23/10 11:00:14 (13.438 ms); `maestro_watchdog` ok a cada 15 min (última 14:45:12).
- E-mails do Hub (source=emails): 2 envios 23/10 11:00 "Maestro · Relatório de tráfego — 22/10/2026" + 1 aviso watchdog 12:00.
- Código `pocketbase/hooks/panorama_email.js` (projeto 67634): gravação na coleção `leads` + e-mail só ao lead; sem ponte para 51414.
- Erro 401 do MCP metaads: "Session has expired on Monday, 19-Oct-26 10:00:00 PDT" (limitação registrada).
- Auditoria de 20/10 (06_notas): zero referências cruzadas Hub × 51414 no código dos hooks do Hub.

---
*Relatório gerado em 23/10/2026 · F3-T09 · somente leitura confirmada — nenhuma alteração em automações, integrações, bancos, campanhas ou configurações.*