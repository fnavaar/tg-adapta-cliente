# SPEC-F3-006 — Campanhas Meta Ads no Skip, alimentadas por automação no Maestro

**Fase:** 3
**Status:** planejada
**Criada em:** 2026-10-22 (evoluções EV-5C-02, EV-5C-03, EV-5C-05 e EV-5C-06; decisão P1)
**Dono:** marketing/Champion operam; direção lê; consultor valida a primeira demonstração
**Origem no escopo:** §12.2 C-04b; DC-003; G-009; F2-004 (leitura limitada provada na F2-T09)
**Degrau da solução:** dependência existente — usa o conector Meta Ads já conectado no Maestro e o conector Skip do Maestro; construção mínima de duas coleções e uma página de leitura.

## Em linguagem simples

**O que você vai ver:** primeiro, um **relatório curto** dizendo quais automações estão ligadas no
Maestro, para onde cada uma manda dados, para onde vão os leads da landing page e quais campanhas estão
ativas (F3-T09). Depois, uma tela **"Campanhas"** no Skip com cada campanha Meta: nome, se está ativa ou
pausada, orçamento por dia, quanto já gastou, impressões, cliques, resultados e a hora da última
atualização. Se a conexão com a Meta expirar, aparece uma **faixa de aviso** na tela e o Champion
recebe um **e-mail**; os números antigos continuam lá, marcados com a data.

**Onde executar:** Maestro. A automação é do Maestro (consome crédito do Maestro) e grava somente no
projeto Skip **"repositório adapta"**.

## Contexto e decisões fechadas

- **Estado atual:** o Maestro tem o conector Meta Ads (via Composio) conectado na conta
  `act_1667348577717128` (TalentGroup_01); a F2-T09 provou leitura limitada sem escrita. Na 5ª call
  descobriu-se uma automação diária do Maestro alimentando um projeto Skip paralelo ("Hub de gestão Meta
  Ads"); foi pedido ao Maestro que a parasse. Há uma campanha ativa (~R$ 20/dia) com landing page criada
  pelo Maestro, e não se sabe para onde vão os envios do formulário. A conexão expira com frequência.
- **Estado desejado:** um único caminho, conhecido e documentado: Maestro lê a Meta (somente leitura) →
  grava no projeto oficial → tela Campanhas mostra os dados ou um aviso de falha.
- **Decisões já fechadas:** nenhuma escrita na Meta (ativar, pausar, criar, mudar orçamento ou criativo);
  nenhum dado pessoal de lead lido da Meta; nenhum outro projeto Skip recebe dados; volume (impressões,
  cliques) aparece separado de resultado (RN-F3-008 da SPEC-F3-002); falha nunca apaga o último dado bom.
- **Bloqueios:** B3-META-01 alterado em 22/10 (somente métricas de campanha por esta SPEC);
  B3-LGPD-01 (envios do formulário da landing page com dado de contato só entram no funil após política
  aprovada); **B3-META-LEITOR** — a conexão atual está no principal João Paulo Oliveira, com controle
  total (AP-2026-09-23-1211); antes da F3-T12, o leitor dedicado somente leitura deve concluir o Connect
  Link **ou** o Champion registra por escrito que aceita usar o principal atual com instrução estrita de
  somente leitura.

## Resultado observável

1. Relatório `diagnostico-maestro-f3-t09.md`: automações ativas no Maestro (nome, cadência, o que lê,
   onde grava), confirmação de que a automação do "Hub de gestão Meta Ads" está parada, destino atual do
   formulário da landing page e lista das campanhas Meta com status.
2. Tela Campanhas no projeto "repositório adapta" com as campanhas da conta, atualizada uma vez por dia e
   por execução manual sob demanda.
3. Faixa de saúde da conexão (ok / expirada / erro, desde quando) e e-mail ao Champion na falha.
4. Para cada campanha, contador de demandas no Funil (F3-005) cuja atribuição aponta para ela; sem
   ligação → "sem ligação no funil".

## Limites e dependências

- **Inclui:** diagnóstico somente leitura; coleções `campanhas_meta` (snapshot diário) e `conexao_meta`
  (saúde); página Campanhas; automação agendada no Maestro; aviso por e-mail.
- **Fora de escopo:** qualquer escrita na Meta; leitura de lead forms/dado pessoal da Meta; LinkedIn e
  Google (Fase 4); RD Station; mover a automação para o Skip; corrigir sozinho o destino da landing page
  (se o diagnóstico achar destino errado ou desconhecido, vira BLOQUEIO para o consultor).
- **Entradas e pré-condições:** conector Meta Ads e conector Skip do Maestro conectados; projeto
  "repositório adapta" confirmado; B3-META-LEITOR resolvido antes da F3-T12.
- **Saídas/artefatos:** relatório da F3-T09; coleções e página; ficha da automação (nome, cadência,
  fonte, destino, campos, o que nunca faz, como avisa falha); evidência `campanhas-f3.md`.
- **Dependências e responsáveis:** Champion executa no Maestro; marketing confere os números com o
  Gerenciador de Anúncios; consultor revisa.
- **Atores e permissões mínimas:** a automação lê a conta de anúncios e grava apenas nas duas coleções;
  direção, marketing e comercial leem a tela; ninguém edita os dados pela tela.
- **Superfícies/arquivos/configurações afetadas:** coleções novas `campanhas_meta` e `conexao_meta`
  (migration não destrutiva); página `campanhas`; uma automação agendada no Maestro; nenhuma alteração
  em `demandas`, `propostas`, `vagas` ou atribuição.
- **Risco e plano B:** token expira → faixa + e-mail, dados antigos preservados, próxima execução tenta
  de novo (sem retry em sequência); números divergentes do Gerenciador → pendência com dono, não
  "corrigir" na mão; conector com permissão de escrita → instrução somente leitura + B3-META-LEITOR.
- **Rollback ou reversão:** desligar a automação no Maestro e esconder a página; coleções ficam como
  histórico; nada é apagado.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Meta Ads (conta `act_1667348577717128`) → Maestro | API Meta via conector Composio do Maestro | por campanha: `campaign_id`, nome, status efetivo, objetivo, orçamento diário, início/fim, gasto, impressões, cliques, resultados, data de referência | OAuth do conector; somente ações de leitura | 1 tentativa por execução; timeout 60 s; sem retry em sequência | 401/403/expirado → `conexao_meta = expirada`; 429/timeout → `erro`; campo fora do contrato descartado e registrado (RN-F2-012) |
| Maestro → Skip `campanhas_meta` | conector Skip do Maestro, projeto "repositório adapta" | campos acima + `snapshot_em`, `execucao_id` | escrita só nesta coleção | upsert por (`campaign_id`, data de referência); reexecutar não duplica | falha de gravação → não altera snapshot anterior; registra em `conexao_meta` |
| Maestro → Skip `conexao_meta` | resultado da execução | `status` (ok/expirada/erro), `desde`, `ultima_execucao`, `mensagem` curta | escrita só nesta coleção | 1 registro por execução | — |
| Maestro → e-mail do Champion | resultado da execução | assunto "Conexão Meta: <status>", hora, o que fazer | e-mail do Champion | só quando o status muda de ok para falha | falha do e-mail → registrada em `conexao_meta` |
| `campanhas_meta` × atribuição F2 → contador no funil | `campaign_id` × campanha_id da atribuição | contagem de demandas por campanha | leitura | contagem pela fonte | sem ligação → "sem ligação no funil" |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-025 — Somente leitura na Meta | qualquer execução | apenas ações de leitura do conector | pedido de escrita → recusar e parar | P1, B3-META-01 |
| RN-F3-026 — Destino único | qualquer gravação | grava só em `campanhas_meta`/`conexao_meta` do projeto "repositório adapta" | destino diferente → recusar e parar | P1, EV-5C-03 |
| RN-F3-027 — Último dado bom preservado | execução com falha | não sobrescreve snapshot; tela mostra a data do último dado | — | EV-5C-06 |
| RN-F3-028 — Sem dado pessoal | resposta com campo de lead/contato | descartar e registrar | — | RN-F2-012, B3-LGPD-01 |
| RN-F3-029 — Automação é task | qualquer automação do projeto no Maestro | existe ficha e task correspondente | automação sem task → desligar e reportar | §12.1 do escopo |

## Fluxo e regras

1. **F3-T09 (diagnóstico, só leitura):** perguntar ao Maestro e registrar: automações ativas e destinos;
   estado da automação do Hub; destino do formulário da landing page; campanhas da conta e status. Nada
   é criado ou alterado.
2. Se o diagnóstico mostrar destino de leads desconhecido ou fora do projeto oficial, registrar BLOQUEIO
   para o consultor e seguir apenas com métricas de campanha.
3. **F3-T12:** criar as duas coleções e a página; criar a automação agendada no Maestro com a ficha;
   rodar uma execução manual e conferir com o Gerenciador de Anúncios.
4. **F3-T13:** provar falhas, idempotência, destino único e ausência de escrita.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | conexão válida, campanha ativa | tela mostra campanha com números do dia e "conexão ok" | número divergente → pendência |
| Limite | campanha sem entrega no período | linha com zeros legítimos e data | — |
| Falha | token expirado / 403 / 429 / timeout | faixa de aviso + e-mail; snapshot anterior intacto | próxima execução agendada; Champion reconecta |
| Falha | automação apontando para outro projeto | execução recusada e reportada | corrigir destino na ficha |

## Instruções de execução para o Maestro (antigo Ethos)

1. **Ler antes de alterar:** SPEC-F2-004 e relatório da F2-T09; esta SPEC; §12 do escopo; ata da 5ª call.
2. **Alterar somente:** coleções `campanhas_meta` e `conexao_meta`, página `campanhas` e a automação
   descrita na ficha, no projeto "repositório adapta".
3. **Não alterar:** campanhas, orçamentos ou criativos na Meta; outros projetos Skip; `demandas`,
   `propostas`, `vagas`, atribuição; outras automações (exceto confirmar a parada da do Hub).
4. **Executar nesta ordem:** diagnóstico (T09) → teste humano → coleções e página → automação e
   execução manual (T12) → teste humano → provas de falha (T13).
5. **Explicar antes de começar:** dizer ao Champion, em linguagem simples, o que a etapa vai mostrar.
6. **Parar e pedir validação quando:** a ação exigir escrita na Meta; o conector pedir novo consentimento
   ou segredo no chat; o destino dos leads estiver fora do projeto oficial; aparecer dado pessoal; não
   houver conector de e-mail validado no Maestro (nesse caso, entregar só a faixa na tela e registrar o
   e-mail como pendência — o CA-3-17 fica parcial até lá).
7. **Estado válido ao parar:** automação desligada ou rodando só com leitura; snapshot anterior intacto.

## Checklist de execução

- [ ] Relatório de diagnóstico com automações, destinos, landing page e campanhas.
- [ ] Automação do Hub confirmada como parada.
- [ ] Coleções e página criadas no projeto oficial.
- [ ] Automação agendada com ficha completa; execução manual conferida com o Gerenciador.
- [ ] Falha de conexão gera faixa + e-mail sem apagar dados.
- [ ] Reexecução não duplica; nenhuma escrita na Meta; nenhum dado em outro projeto.

## Critérios de aceite

- [ ] **CA-3-15:** existe relatório de diagnóstico que lista cada automação ativa do Maestro com destino,
  confirma a parada da automação do Hub, informa o destino do formulário da landing page (ou registra
  BLOQUEIO) e lista as campanhas da conta com status.
- [ ] **CA-3-16:** a tela Campanhas mostra as campanhas da conta com status, orçamento, gasto, impressões,
  cliques, resultados e hora da atualização, iguais ao Gerenciador de Anúncios na mesma data de
  referência, alimentada pela automação do Maestro que grava só no projeto oficial.
- [ ] **CA-3-17:** com a conexão inválida, a execução não grava snapshot novo, mantém o anterior, mostra a
  faixa de aviso e envia o e-mail; reexecutar com conexão válida não duplica linhas; nenhuma escrita na
  Meta ocorre em nenhum cenário.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | automação gravando em outro projeto; execução com token inválido; pedido "pause a campanha" | executar a automação nesses cenários | recusa/parada; faixa + e-mail; nenhuma escrita | log da execução + captura |
| GREEN | conexão válida, conta TalentGroup_01 | execução manual | CA-3-16 demonstrável | captura da tela + captura do Gerenciador |
| REFACTOR/REGRESSÃO | reexecutar duas vezes no mesmo dia; abrir Funil e painel F1/F2 | replay | sem duplicação; telas anteriores intactas | comparação de contagens |

**Dados/fixtures:** métricas reais de campanha (sem dado pessoal); token inválido simulado pelo conector
desconectado em ambiente de teste ou pelo próprio vencimento.
**Caminhos de erro obrigatórios:** expirado/401; 403; 429; timeout; destino errado; campo pessoal na
resposta; pedido de escrita.
**Evidência exigida:** relatório T09, ficha da automação, capturas da tela e do Gerenciador, log das
execuções, e-mail recebido, teste humano do Champion.

## Handoff e operação

- **Como demonstrar:** abrir Campanhas, comparar uma campanha com o Gerenciador, mostrar a faixa de saúde
  e o e-mail de uma falha.
- **Como operar depois:** Champion reconecta a Meta quando chegar o e-mail; marketing confere a tela na
  reunião semanal.
- **Como monitorar:** `conexao_meta` (status e "desde"); dias sem snapshot; campanhas "sem ligação no
  funil".
- **Pendência conhecida:** token de longa duração (consultor); B3-META-LEITOR; B3-LGPD-01 para os envios
  do formulário.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T09 | Diagnosticar no Maestro as automações ativas, o destino dos leads da landing page e as campanhas Meta, sem alterar nada | João Paulo | F3-006 | CA-3-15 | Fluxo e regras (passos 1–2); Checklist | `diagnostico-maestro-f3-t09.md` | conectores Meta e Skip ativos no Maestro | ☐ |
| F3-T12 | Criar a tela Campanhas e a automação diária do Maestro que lê a Meta e grava só no projeto oficial | João Paulo | F3-006 | CA-3-16 | Dados e integrações; Fluxo e regras (passo 3); Checklist | Ficha da automação + capturas tela × Gerenciador | F3-T09 aceita; B3-META-LEITOR resolvido | ☐ |
| F3-T13 | Provar conexão expirada, reexecução sem duplicar, destino único e nenhuma escrita na Meta | João Paulo | F3-006 | CA-3-16, CA-3-17 | Critérios de aceite; TDD da SPEC | Log das execuções + e-mail + bateria humana | F3-T12 aceita por teste humano | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
