# Fase 3 — Tarefas

<!-- fase-format:2 -->

**Plano:** TG Mais Serviços de Tecnologia e RH LTDA · `6b09d189`  
**Estado:** Fase 3 em execução; 1/13 tasks concluídas (F3-T09 em 24/10, homologada com ressalvas); F3-T01 em andamento (E2 concluída 23/10; etapas seguintes bloqueadas por D4/D5/D6 — emendas do consultor pendentes).  
**Champion:** João Paulo  
**Atualizado em:** 22/10/2026 pela consultoria (Ramon Pádua) — 5ª call.  
**Regra:** uma task por vez; cada conclusão exige as provas da SPEC e o teste humano do Champion.

## Esta fase em linguagem simples

Na Fase 3 o sistema passa a **mostrar** o caminho de cada demanda. Ao final, vocês vão ter no Skip (projeto **"repositório adapta"**):

- **Funil** — um quadro em colunas (Kanban): cada cartão é uma empresa/demanda e mostra de onde veio (inbound ou outbound, canal, campanha), o que ela quer (R&S ou TMO), quem é o dono e a próxima ação. Clicando, aparece a história completa.
- **Campanhas** — as campanhas Meta Ads (ativas ou pausadas, gasto, resultados), atualizadas todo dia por uma automação no Maestro, com aviso se a conexão cair.
- **Gargalos** — quantas demandas há em cada etapa e onde estão travando.
- **Passagens pendentes** — quando o comercial passa uma demanda para o R&S ou a alocação, para quem foi e se foi aceita.
- **Área do DHO** — separada, só para o DHO.

Enquanto a política de dados (LGPD) não for aprovada pela direção, as telas mostram **dados de teste**, marcados com o selo TESTE.

**Como o Maestro vai trabalhar com vocês:** antes de cada task ele explica o que vai criar, combina cada passo ("vamos criar isso no Skip agora"), pede para vocês darem uma olhada no Skip depois de cada passo e fecha com um resumo do que já dá para ver e qual é a próxima task.

## Ordem recomendada

F3-T01 → F3-T09 → F3-T10 → F3-T11 → F3-T12 → F3-T13 → F3-T02 → F3-T03 → F3-T04 → F3-T05 → F3-T06 → F3-T07 → F3-T08

## Jornada operacional

- [/] Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética @"João Paulo" #projeto
  > F3-T01 · SPEC F3-001 · CA-3-01/02/04 (E-F3-001-01). Criar fixtures inbound/outbound; percorrer o pipeline até proposta/vaga com retorno; exercitar escalonamento de oportunidade parada; demonstrar hierarquia Demanda→Propostas→Vagas; registrar captura/export e log de transições. Parar se exigir dado real, dedupe por inferência ou integração externa.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: cada demanda de teste ganha propostas, vagas, retorno da operação e aviso quando fica parada.
- [ ] Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas @"João Paulo" #projeto
  > F3-T02 · SPEC F3-001 · CA-3-01..04. Executar RED/GREEN/regressão, replay, contagens pela fonte, hierarquia Demanda→Propostas→Vagas e bateria de equivalência. Depende de F3-T01 aceita e da matriz RACI nominal para a prova de handoff.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: um roteiro em que duas pessoas classificam os mesmos casos e chegam à mesma etapa, com "passou / não passou" por caso.
- [ ] Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética @"João Paulo" #projeto
  > F3-T03 · SPEC F3-002 · CA-3-11 (E-F3-002-01). Criar visões por estado, gargalo, tempos e retorno; manter o KPI contra alvo bloqueado e a pendência B3-MET-01 visível. Depende de F3-T01 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: tela "Gargalos" com quantas demandas há em cada etapa, tempo entre etapas e quais estão paradas além do prazo.
- [ ] Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens @"João Paulo" #projeto
  > F3-T04 · SPEC F3-002 · CA-3-11/12 (E-F3-002-01). Provar leitura completa, contagens reproduzíveis, separação volume×qualidade e bloqueio sem G-001; regressão do painel F1/F2. Depende de F3-T03 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: a direção abre a tela e diz onde a demanda trava; números iguais ao Funil; meta como "pendente de decisão".
- [ ] Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética @"João Paulo" #projeto
  > F3-T05 · SPEC F3-003 · CA-3-06. Criar HO-F3-001 com destinatário, SLA e estado; exercitar aceite, recusa e expiração com papéis provisórios registrados. Depende de F3-T01 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: lista "Passagens pendentes" — para quem a demanda foi passada, prazo para aceitar e se foi aceita, recusada ou venceu.
- [ ] Provar aceite, recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal @"João Paulo" #projeto
  > F3-T06 · SPEC F3-003 · CA-3-06..08. Executar bateria humana completa, incluindo falha segura sem retry automático, matriz RACI e log de eventos. Depende de F3-T05 aceita e B3-RACI-01 fechado.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: o teste com os nomes reais da matriz, cada situação mostrando o que aconteceu na tela.
- [ ] Materializar objeto separado de sinal de conta do DHO com lista versionada e permissões fail-closed @"João Paulo" #projeto
  > F3-T07 · SPEC F3-004 · CA-3-09. Criar objeto inativo com fixture, permissões server-side e prova negativa de leitura comercial; registrar decisão C-06. Depende de F3-T01 aceita; dado real permanece bloqueado por B3-DHO-01.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: área separada, só do DHO, com um sinal da conta em dado de teste; o comercial não vê essa área.
- [ ] Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política @"João Paulo" #projeto
  > F3-T08 · SPEC F3-004 · CA-3-09/10. Provar sinal autorizado em fixture, isolamento, duplicata, rollback e encaminhamento humano; nenhum sinal fora da lista ou dado real. Depende de F3-T07 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: a prova de que o comercial não vê o sinal e que o sinal vira encaminhamento para uma pessoa.
- [x] Diagnosticar no Maestro as automações ativas, o destino dos leads da landing page e as campanhas Meta, sem alterar nada @"João Paulo" [interno] #projeto
  > F3-T09 · SPEC F3-006 · CA-3-15. Somente leitura: listar automações e destinos, confirmar a parada da automação do "Hub de gestão Meta Ads", achar para onde vai o formulário da landing page e listar as campanhas. Parar e chamar o consultor se os leads estiverem indo para fora do projeto oficial.
  > Onde executar: Maestro (somente leitura). O que você vai ver: um relatório curto dizendo quais automações estão ligadas, para onde cada uma manda dados, para onde vão os leads do formulário e quais campanhas estão ativas.
- [ ] Construir a tela Funil (Kanban) com cartões, origem, filtros e Jornada usando os dados de teste @"João Paulo" [interno] #projeto
  > F3-T10 · SPEC F3-005 · CA-3-13. Colunas por etapa, cartão com origem/canal/campanha/serviço/área/dono/próxima ação, selo TESTE, filtros e Jornada do cartão. Depende de F3-T01 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: tela "Funil" em colunas por etapa; cada cartão mostra de onde a demanda veio, o serviço, o dono e a próxima ação; clicando, a história completa.
- [ ] Provar o Funil: origem desconhecida, arrastar sem evidência, contagens e regressão do painel @"João Paulo" [interno] #projeto
  > F3-T11 · SPEC F3-005 · CA-3-13/14. RED/GREEN/regressão da SPEC. Depende de F3-T10 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: a prova de que o Funil mostra "desconhecido" quando falta origem, recusa mover cartão sem evidência e tem as mesmas contagens da fonte.
- [ ] Criar a tela Campanhas e a automação diária do Maestro que lê a Meta e grava só no projeto oficial @"João Paulo" [interno] #projeto
  > F3-T12 · SPEC F3-006 · CA-3-16. Coleções campanhas_meta/conexao_meta, página Campanhas, ficha da automação e execução manual conferida com o Gerenciador de Anúncios. Depende de F3-T09 aceita e B3-META-LEITOR resolvido.
  > Onde executar: Maestro (automação agendada) → Skip "repositório adapta". O que você vai ver: tela "Campanhas" com cada campanha Meta — ativa ou pausada, orçamento, gasto, impressões, cliques, resultados e hora da atualização.
- [ ] Provar conexão expirada, reexecução sem duplicar, destino único e nenhuma escrita na Meta @"João Paulo" [interno] #projeto
  > F3-T13 · SPEC F3-006 · CA-3-16/17. RED/GREEN/regressão da SPEC. Depende de F3-T12 aceita.
  > Onde executar: Maestro → Skip "repositório adapta". O que você vai ver: a prova de que, se a conexão cair, aparece um aviso na tela e chega um e-mail, sem apagar os números de antes; e que nada é escrito na Meta.

## Tasks

| ID | Leva | Task | Onde executar | O que você vai ver | Dono | SPEC | Critério | Subseção exata da SPEC | Recorte da prova | Evidência esperada | Pré-condições | Ponto de parada | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| F3-T01 | 1 | Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética. | Maestro → Skip "repositório adapta" | Cada demanda de teste ganha propostas, vagas, retorno da operação e aviso quando fica parada. | João Paulo | F3-001 | CA-3-01, CA-3-02, CA-3-04 (E-F3-001-01) | Dados e integrações; Fluxo e regras; Checklist | Fixtures inbound/outbound, proposta/vaga, retorno e escalonamento; hierarquia Demanda→Propostas→Vagas. | Captura/export da jornada e log de transições. | F2 9/9 aceita; fixtures sintéticos; pipeline F1/F2 preservado; E-F3-001-01 vigente. | Parar se exigir dado real, dedupe por inferência ou integração externa. | EM ANDAMENTO — E0/E1 concluídas; E2 concluída 23/10 (teste humano aprovado); E2-coleções/E5/E6 aguardam D4/D5/D6 |
| F3-T09 | 1 | Diagnosticar no Maestro as automações ativas, o destino dos leads da landing page e as campanhas Meta, sem alterar nada. | Maestro (somente leitura) | Um relatório curto: quais automações estão ligadas, para onde cada uma manda dados, para onde vão os leads do formulário e quais campanhas estão ativas. | João Paulo | F3-006 | CA-3-15 | Fluxo e regras (passos 1–2); Checklist | Perguntas ao Maestro e conferência no Skip; nenhuma criação ou alteração. | `diagnostico-maestro-f3-t09.md` com automações, destinos, landing page e campanhas. | Conectores Meta e Skip ativos no Maestro. | Parar se encontrar destino de leads fora do projeto oficial ou desconhecido (BLOQUEIO ao consultor). | CONCLUÍDA 24/10 — homologação com ressalvas (CA-3-15 parcial: parada do Hub condicionada à F3-T12/T13 por ordem do Champion; leads 67634 sem integração com o funil = pendência operacional) |
| F3-T10 | 2 | Construir a tela Funil (Kanban) com cartões, origem, filtros e Jornada usando os dados de teste. | Maestro → Skip "repositório adapta" | Tela "Funil" em colunas por etapa; cada cartão mostra de onde a demanda veio, o serviço, o dono e a próxima ação; clicando, a história completa. | João Paulo | F3-005 | CA-3-13 | Dados e integrações; Fluxo e regras; Checklist | Colunas, cartões, filtros e Jornada com os fixtures da F3-T01. | Capturas do Funil e da Jornada + comparação fonte×tela. | F3-T01 aceita por teste humano. | Parar se precisar de campo inexistente, regra automática de qualificação ou dado de contato real. | BLOQUEADA (F3-T01) |
| F3-T11 | 3 | Provar o Funil: origem desconhecida, arrastar sem evidência, contagens e regressão do painel. | Maestro → Skip "repositório adapta" | A prova de que o Funil mostra "desconhecido" quando falta origem, recusa mover cartão sem evidência e tem as mesmas contagens da fonte. | João Paulo | F3-005 | CA-3-13, CA-3-14 | Critérios de aceite; TDD da SPEC | RED/GREEN/regressão da SPEC-F3-005. | Bateria humana + log de transições + comparação fonte×tela. | F3-T10 aceita por teste humano. | Parar se o cartão mover sem evidência ou a contagem divergir da fonte. | BLOQUEADA (F3-T10) |
| F3-T12 | 2 | Criar a tela Campanhas e a automação diária do Maestro que lê a Meta e grava só no projeto oficial. | Maestro (automação agendada) → Skip "repositório adapta" | Tela "Campanhas" com cada campanha Meta: ativa ou pausada, orçamento, gasto, impressões, cliques, resultados e hora da atualização. | João Paulo | F3-006 | CA-3-16 | Dados e integrações; Fluxo e regras (passo 3); Checklist | Coleções `campanhas_meta`/`conexao_meta`, página e ficha da automação; execução manual conferida com o Gerenciador. | Ficha da automação + capturas tela × Gerenciador de Anúncios. | F3-T09 aceita; B3-META-LEITOR resolvido. | Parar se a ação exigir escrita na Meta, segredo no chat ou outro projeto de destino. | BLOQUEADA (F3-T09, B3-META-LEITOR) |
| F3-T13 | 3 | Provar conexão expirada, reexecução sem duplicar, destino único e nenhuma escrita na Meta. | Maestro → Skip "repositório adapta" | A prova de que, se a conexão cair, aparece um aviso na tela e chega um e-mail, sem apagar os números de antes; e que nada é escrito na Meta. | João Paulo | F3-006 | CA-3-16, CA-3-17 | Critérios de aceite; TDD da SPEC | RED/GREEN/regressão da SPEC-F3-006. | Log das execuções + e-mail recebido + bateria humana. | F3-T12 aceita por teste humano. | Parar se houver escrita na Meta, duplicação ou gravação fora do projeto oficial. | BLOQUEADA (F3-T12) |
| F3-T02 | 2 | Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas. | Maestro → Skip "repositório adapta" | Um roteiro em que duas pessoas classificam os mesmos casos e chegam à mesma etapa, com "passou / não passou" por caso. | João Paulo | F3-001 | CA-3-01..04 | Critérios de aceite; TDD | RED/GREEN/regressão, replay e bateria de equivalência. | Bateria humana + log + comparação fonte×painel. | F3-T01 aceita; B3-RACI-01 para a prova de handoff. | Parar sem critério de classificação ou matriz nominal. | BLOQUEADA (F3-T01, B3-RACI-01) |
| F3-T03 | 3 | Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética. | Maestro → Skip "repositório adapta" | Tela "Gargalos": quantas demandas há em cada etapa, quanto tempo levam entre etapas e quais estão paradas além do prazo. | João Paulo | F3-002 | CA-3-11 (E-F3-002-01) | Dados e integrações; Fluxo e regras; Checklist | Visões por estado, gargalo, tempos e retorno; KPI contra alvo bloqueado. | Captura/export com contagens reproduzíveis. | F3-T01 aceita. | Parar se a contagem não reproduzir a fonte ou se pedirem KPI sem alvo. | BLOQUEADA (F3-T01) |
| F3-T04 | 4 | Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens. | Maestro → Skip "repositório adapta" | A direção abre a tela e diz onde a demanda trava; números iguais ao Funil; meta como "pendente de decisão". | João Paulo | F3-002 | CA-3-11/12 (E-F3-002-01) | Critérios de aceite; TDD | Leitura completa, volume×qualidade, pendência G-001 e regressão F1/F2. | Bateria humana + comparação fonte×dashboard. | F3-T03 aceita. | Parar se esconder lacuna ou misturar volume com qualidade. | BLOQUEADA (F3-T03) |
| F3-T05 | 3 | Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética. | Maestro → Skip "repositório adapta" | Lista "Passagens pendentes": para quem a demanda foi passada, prazo para aceitar e se foi aceita, recusada ou venceu. | João Paulo | F3-003 | CA-3-06 | Dados e integrações; Fluxo e regras; Checklist | HO-F3-001 com destinatário, prazo de aceite, aceite, recusa e expiração. | Captura/export do registro e estados. | F3-T01 aceita; papéis provisórios registrados. | Parar se exigir disparo externo ou encerramento sem responsável. | BLOQUEADA (F3-T01) |
| F3-T06 | 5 | Provar aceite, recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal. | Maestro → Skip "repositório adapta" | O teste com os nomes reais da matriz: cada situação (aceite, recusa, vencido, sem resposta, falha) mostrando o que aconteceu na tela. | João Paulo | F3-003 | CA-3-06..08 | Critérios de aceite; TDD | Bateria humana completa e falha segura sem retry automático. | Matriz RACI + log de eventos + evidências. | F3-T05 aceita; B3-RACI-01 fechado. | Parar sem matriz nominal ou se pedirem retry automático. | BLOQUEADA (F3-T05, B3-RACI-01) |
| F3-T07 | 4 | Materializar objeto separado de sinal de conta do DHO com lista versionada e permissões fail-closed. | Maestro → Skip "repositório adapta" | Área separada, só do DHO, com um sinal da conta em dado de teste; o comercial não vê essa área. | João Paulo | F3-004 | CA-3-09 | Dados e integrações; Fluxo e regras; Checklist | Objeto inativo com fixture, permissões server-side e prova negativa. | Captura do objeto + prova negativa + decisão C-06. | F3-T01 aceita; decisão C-06 registrada. | Parar se pedirem dado real sem política ou exposição ao comercial. | BLOQUEADA (F3-T01, C-06) |
| F3-T08 | 6 | Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política. | Maestro → Skip "repositório adapta" | A prova de que o comercial não vê o sinal, só sinais da lista entram e o sinal vira encaminhamento para uma pessoa. | João Paulo | F3-004 | CA-3-09/10 | Critérios de aceite; TDD | Sinal em fixture, isolamento, duplicata, rollback e encaminhamento humano. | Bateria humana + lista versionada + decisão de uso. | F3-T07 aceita. | Parar se gerar ação sem decisor ou aparecer no pipeline comercial. | BLOQUEADA (F3-T07) |

## Automações do Maestro neste projeto

| Automação | Task | Lê | Grava | Nunca faz | Aviso de falha | Estado |
|---|---|---|---|---|---|---|
| Diária de Meta Ads → "Hub de gestão Meta Ads" | — (sem task) | Meta Ads | projeto Skip paralelo | — | — | **Parar** (pedido na call de 22/10); confirmar na F3-T09 |
| Campanhas Meta → "repositório adapta" | F3-T12/F3-T13 | métricas de campanha da conta `act_1667348577717128` | `campanhas_meta`, `conexao_meta` | escrever na Meta; ler dado pessoal; gravar em outro projeto | faixa na tela + e-mail ao Champion | a criar na F3-T12 |

## Bloqueios transversais

- **B3-META-01 (alterado 22/10):** a F3 só lê métricas de campanha Meta pela automação da SPEC-F3-006; sem dado pessoal e sem escrita na Meta.
- **B3-META-LEITOR (novo 22/10):** antes da F3-T12, leitor dedicado somente leitura conectado ou aceite do Champion registrado para o principal atual com instrução somente leitura.
- **B3-LGPD-01 (formalizado 22/10):** dado real de contato só aparece após política aprovada pela direção; até lá, selo TESTE.
- **B3-ID-01:** identidade por fonte; sem dedupe por inferência.
- **B3-MET-01:** alvo, fórmula, período e lead qualificado antes de KPI de resultado.
- **B3-RACI-01:** matriz nominal antes da prova F3-T06 e da prova de handoff da F3-T02.
- **B3-DHO-01:** lista de sinais e política antes de dado real de sinal; F3-004 permanece fail-closed com fixtures.
- **D4/D5/D6 (pacote de 08/10):** emendas do consultor pendentes; bloqueiam as etapas E2 (coleções), E5 e E6 da F3-T01.