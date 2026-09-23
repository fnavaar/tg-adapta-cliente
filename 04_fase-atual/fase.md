# Fase 3 — Tarefas

<!-- fase-format:2 -->

**Plano:** TG Mais Serviços de Tecnologia e RH LTDA · `6b09d189`  
**Estado:** Fase 3 liberada para execução controlada; nenhuma task iniciada.  
**Champion:** João Paulo  
**Prazo de referência:** 30/09/2026 (proposto para o ciclo; pode ser ajustado pelo Champion).  
**Regra:** uma task por vez; F3-T01 é a única elegível na abertura. Cada conclusão exige provas da SPEC e teste humano do Champion.

## Jornada operacional

- [ ] Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética @"João Paulo" !30/09/2026 #projeto
  > F3-T01 · SPEC F3-001 · CA-3-01/02. Criar fixtures inbound/outbound; percorrer o pipeline até proposta/vaga com retorno; exercitar escalonamento de oportunidade parada; registrar captura/export e log de transições. Parar se exigir dado real, dedupe por inferência ou integração externa.
- [ ] Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas @"João Paulo" !30/09/2026 #projeto
  > F3-T02 · SPEC F3-001 · CA-3-01..03. Executar RED/GREEN/regressão, replay, contagens pela fonte e bateria de equivalência. Depende de F3-T01 aceita e da matriz RACI nominal para a prova de handoff.
- [ ] Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética @"João Paulo" !30/09/2026 #projeto
  > F3-T03 · SPEC F3-002 · CA-3-04. Criar visões por estado, gargalo, tempos e retorno; manter o KPI contra alvo bloqueado e a pendência B3-MET-01 visível. Depende de F3-T01 aceita.
- [ ] Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens @"João Paulo" !30/09/2026 #projeto
  > F3-T04 · SPEC F3-002 · CA-3-04/05. Provar leitura completa, contagens reproduzíveis, separação volume×qualidade e bloqueio sem G-001; regressão do painel F1/F2. Depende de F3-T03 aceita.
- [ ] Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética @"João Paulo" !30/09/2026 #projeto
  > F3-T05 · SPEC F3-003 · CA-3-06. Criar HO-F3-001 com destinatário, SLA e estado; exercitar aceite, recusa e expiração com papéis provisórios registrados. Depende de F3-T01 aceita.
- [ ] Provar aceite, recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal @"João Paulo" !30/09/2026 #projeto
  > F3-T06 · SPEC F3-003 · CA-3-06..08. Executar bateria humana completa, incluindo falha segura sem retry automático, matriz RACI e log de eventos. Depende de F3-T05 aceita e B3-RACI-01 fechado.
- [ ] Materializar objeto separado de sinal de conta do DHO com lista versionada e permissões fail-closed @"João Paulo" !30/09/2026 #projeto
  > F3-T07 · SPEC F3-004 · CA-3-09. Criar objeto inativo com fixture, permissões server-side e prova negativa de leitura comercial; registrar decisão C-06. Depende de F3-T01 aceita; dado real permanece bloqueado por B3-DHO-01.
- [ ] Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política @"João Paulo" !30/09/2026 #projeto
  > F3-T08 · SPEC F3-004 · CA-3-09/10. Provar sinal autorizado em fixture, isolamento, duplicata, rollback e encaminhamento humano; nenhum sinal fora da lista ou dado real. Depende de F3-T07 aceita.

## Tasks

| ID | Leva | Task | Dono | SPEC | Critério | Subseção exata da SPEC | Recorte da prova | Evidência esperada | Pré-condições | Ponto de parada | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| F3-T01 | 1 | Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética. | João Paulo | F3-001 | CA-3-01, CA-3-02 | Dados e integrações; Fluxo e regras; Checklist | Criar fixtures inbound/outbound; percorrer `PIPE-F3-IN-001` e `PIPE-F3-OUT-001` até proposta/vaga com retorno; escalonar `PIPE-F3-STUCK-001`. | Captura/export da jornada dupla com proposta/vaga, retorno e log de transições. | F2 9/9 aceita; fixtures sintéticos autorizados; pipeline F1/F2 preservado. | Parar se exigir dado real não autorizado, dedupe por inferência (B3-ID-01) ou integração externa. | ELEGÍVEL |
| F3-T02 | 2 | Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas. | João Paulo | F3-001 | CA-3-01, CA-3-02, CA-3-03 | Critérios de aceite; TDD da SPEC | RED sem evidência/duplicata; GREEN jornada dupla completa; REGRESSÃO replay + contagens pela fonte; bateria de equivalência com duas pessoas. | Bateria humana de equivalência + log de transições + comparação fonte×painel. | F3-T01 aceita por teste humano; matriz RACI nominal (B3-RACI-01). | Parar se a classificação divergir sem critério ou se faltar matriz nominal para o handoff. | BLOQUEADA (F3-T01) |
| F3-T03 | 3 | Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética. | João Paulo | F3-002 | CA-3-04 | Dados e integrações; Fluxo e regras; Checklist | Visões por estado, gargalo captura→abordagem→proposta→vaga, tempos e retorno; KPI contra alvo bloqueado com pendência B3-MET-01 visível. | Captura/export das visões com contagens reproduzíveis da fonte. | F3-T01 aceita; núcleo de reconciliação preservado. | Parar se contagem não reproduzir a fonte ou se pedirem KPI sem alvo aprovado. | BLOQUEADA (F3-T01) |
| F3-T04 | 4 | Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens. | João Paulo | F3-002 | CA-3-04, CA-3-05 | Critérios de aceite; TDD da SPEC | RED com KPI sem G-001 e origem ausente como zero; GREEN leitura de gargalo completa; REGRESSÃO replay + painel F1/F2 intacto. | Bateria humana da leitura + comparação fonte×dashboard. | F3-T03 aceita por teste humano. | Parar se a leitura misturar volume com qualidade ou esconder lacuna. | BLOQUEADA (F3-T03) |
| F3-T05 | 3 | Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética. | João Paulo | F3-003 | CA-3-06 | Dados e integrações; Fluxo e regras; Checklist | Criar `HO-F3-001` com destinatário/SLA/estado; exercitar aceite, recusa e expiração com papéis provisórios registrados. | Captura/export do registro e estados de handoff. | F3-T01 aceita; papéis provisórios registrados como pendência (B3-RACI-01). | Parar se exigir disparo externo automático ou encerramento sem responsável. | BLOQUEADA (F3-T01) |
| F3-T06 | 5 | Provar aceite, recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal. | João Paulo | F3-003 | CA-3-06, CA-3-07, CA-3-08 | Critérios de aceite; TDD da SPEC | RED sem destinatário/SLA e aceite duplicado; GREEN aceite no SLA; REGRESSÃO SLA vencido, sem resposta, falha de acesso e recusa com motivo. | Bateria humana completa + matriz RACI anexa + log de eventos. | F3-T05 aceita por teste humano; B3-RACI-01 fechado. | Parar sem matriz nominal ou se alguém pedir retry automático de falha externa. | BLOQUEADA (F3-T05 + B3-RACI-01) |
| F3-T07 | 4 | Materializar objeto separado de sinal de conta do DHO com lista versionada e permissões fail-closed. | João Paulo | F3-004 | CA-3-09 | Dados e integrações; Fluxo e regras; Checklist | Criar objeto `sinal-de-conta` inativo com lista provisória de fixture; permissões server-side; prova negativa de leitura comercial. | Captura do objeto inativo + prova negativa de acesso + decisão de uso registrada. | F3-T01 aceita; decisão de usar/não usar C-06 registrada pela direção. | Parar se pedirem dado real sem política (B3-DHO-01) ou exposição ao comercial. | BLOQUEADA (F3-T01) |
| F3-T08 | 6 | Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política. | João Paulo | F3-004 | CA-3-09, CA-3-10 | Critérios de aceite; TDD da SPEC | RED sinal fora da lista, leitura comercial e dado real sem política; GREEN sinal autorizado em fixture + encaminhamento humano; REGRESSÃO duplicata, isolamento e rollback. | Bateria humana com prova negativa + lista versionada + decisão de uso. | F3-T07 aceita por teste humano. | Parar se o sinal aparecer em pipeline/dashboard comercial ou gerar ação sem decisor. | BLOQUEADA (F3-T07) |

## Ordem e bloqueios

- **Leva 1:** F3-T01 é a única elegível.
- **Leva 2:** F3-T02 após F3-T01.
- **Leva 3:** F3-T03 e F3-T05 após F3-T01; continuam uma por vez.
- **Leva 4:** F3-T04 após F3-T03; F3-T07 após F3-T01.
- **Leva 5:** F3-T06 após F3-T05 e B3-RACI-01.
- **Leva 6:** F3-T08 após F3-T07.
- **Bloqueios transversais:** B3-META-01 (nenhuma leitura Meta na F3), B3-ID-01 (identidade por fonte), B3-MET-01 (G-001 antes de KPI), B3-RACI-01 (matriz nominal antes da prova de handoff) e B3-DHO-01 (lista/política antes de dado real).
