# Fase 3 — Tasks gerais

**Plano:** TG Mais / `6b09d189` · **Run:** 20260923T1514Z-6b09d189-liberar-f3
**Estado:** Fase 3 liberada para execução controlada; nenhuma task iniciada. F3-T01 é a única task elegível; execute uma task por vez com autorização expressa do Champion e teste humano ao fim de cada uma.

## Tasks

| ID | Leva | Task | Dono | SPEC | Critério | Subseção exata da SPEC | Recorte da prova | Evidência esperada | Pré-condições | Ponto de parada | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| F3-T01 | 1 | Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética. | Comercial/gerentes | F3-001 | CA-3-01, CA-3-02 | Dados e integrações; Fluxo e regras; Checklist | Criar fixtures inbound/outbound; percorrer `PIPE-F3-IN-001` e `PIPE-F3-OUT-001` até proposta/vaga com retorno; escalonar `PIPE-F3-STUCK-001`. | Captura/export da jornada dupla com proposta/vaga, retorno e log de transições. | F2 9/9 aceita; fixtures sintéticos autorizados; pipeline F1/F2 preservado. | Parar se exigir dado real não autorizado, dedupe por inferência (B3-ID-01) ou integração externa. | Pendente |
| F3-T02 | 2 | Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas. | Comercial + operação + direção | F3-001 | CA-3-01, CA-3-02, CA-3-03 | Critérios de aceite; TDD da SPEC | RED sem evidência/duplicata; GREEN jornada dupla completa; REGRESSÃO replay + contagens pela fonte; bateria de equivalência com duas pessoas. | Bateria humana de equivalência + log de transições + comparação fonte×painel. | F3-T01 aceita por teste humano; matriz RACI nominal (B3-RACI-01). | Parar se a classificação divergir sem critério ou se faltar matriz nominal para o handoff. | Bloqueada (F3-T01) |
| F3-T03 | 3 | Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética. | Marketing/comercial | F3-002 | CA-3-04 | Dados e integrações; Fluxo e regras; Checklist | Visões por estado, gargalo captura→abordagem→proposta→vaga, tempos e retorno; KPI contra alvo bloqueado com pendência B3-MET-01 visível. | Captura/export das visões com contagens reproduzíveis da fonte. | F3-T01 aceita; núcleo de reconciliação preservado. | Parar se contagem não reproduzir a fonte ou se pedirem KPI sem alvo aprovado. | Bloqueada (F3-T01) |
| F3-T04 | 4 | Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens. | Direção + consultor | F3-002 | CA-3-04, CA-3-05 | Critérios de aceite; TDD da SPEC | RED com KPI sem G-001 e origem ausente como zero; GREEN leitura de gargalo completa; REGRESSÃO replay + painel F1/F2 intacto. | Bateria humana da leitura + comparação fonte×dashboard. | F3-T03 aceita por teste humano. | Parar se a leitura misturar volume com qualidade ou esconder lacuna. | Bloqueada (F3-T03) |
| F3-T05 | 3 | Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética. | Gerentes/comercial | F3-003 | CA-3-06 | Dados e integrações; Fluxo e regras; Checklist | Criar `HO-F3-001` com destinatário/SLA/estado; exercitar aceite, recusa e expiração com papéis provisórios registrados. | Captura/export do registro e estados de handoff. | F3-T01 aceita; papéis provisórios registrados como pendência (B3-RACI-01). | Parar se exigir disparo externo automático ou encerramento sem responsável. | Bloqueada (F3-T01) |
| F3-T06 | 5 | Provar aceite/recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal. | Gerentes + operação + direção | F3-003 | CA-3-06, CA-3-07, CA-3-08 | Critérios de aceite; TDD da SPEC | RED sem destinatário/SLA e aceite duplicado; GREEN aceite no SLA; REGRESSÃO SLA vencido, sem resposta, falha de acesso (estado seguro, sem retry) e recusa com motivo. | Bateria humana completa + matriz RACI anexa + log de eventos. | F3-T05 aceita por teste humano; B3-RACI-01 fechado. | Parar sem matriz nominal ou se alguém pedir retry automático de falha externa. | Bloqueada (F3-T05 + B3-RACI-01) |
| F3-T07 | 4 | Materializar objeto separado de sinal de conta do DHO com lista versionada e permissões (fail-closed). | DHO + direção | F3-004 | CA-3-09 | Dados e integrações; Fluxo e regras; Checklist | Criar objeto `sinal-de-conta` inativo com lista provisória de fixture; permissões server-side; prova negativa de leitura comercial. | Captura do objeto inativo + prova negativa de acesso + decisão de uso registrada. | F3-T01 aceita; decisão de usar/não usar C-06 registrada pela direção. | Parar se pedirem dado real sem política (B3-DHO-01) ou exposição ao comercial. | Bloqueada (F3-T01) |
| F3-T08 | 6 | Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política. | DHO + direção + consultor | F3-004 | CA-3-09, CA-3-10 | Critérios de aceite; TDD da SPEC | RED sinal fora da lista, leitura comercial e dado real sem política; GREEN sinal autorizado fixture + encaminhamento humano; REGRESSÃO duplicata, isolamento e rollback. | Bateria humana com prova negativa + lista versionada + decisão de uso. | F3-T07 aceita por teste humano. | Parar se o sinal aparecer em pipeline/dashboard comercial ou gerar ação sem decisor. | Bloqueada (F3-T07) |

## Ordem e independência

- **Leva 1:** F3-T01 (única elegível ao abrir a fase).
- **Leva 2:** F3-T02, após F3-T01.
- **Leva 3:** F3-T03 e F3-T05, após F3-T01 — independentes entre si.
- **Leva 4:** F3-T04 (após F3-T03) e F3-T07 (após F3-T01) — independentes entre si.
- **Leva 5:** F3-T06, após F3-T05 e B3-RACI-01.
- **Leva 6:** F3-T08, após F3-T07.
- **Execução:** uma task por vez, mediante autorização expressa do Champion e teste humano ao fim de cada uma.

## Bloqueios transversais (gates humanos nomeados)

- **B3-META-01:** nenhuma task da F3 lê Meta; regularização da conexão (Connect Link pelo leitor dedicado) é pré-requisito para qualquer emenda que queira leitura.
- **B3-ID-01:** identidade por fonte; sem dedupe por inferência; sem relação estrutural automática `demandas`↔`experimentos_f2`.
- **B3-MET-01:** G-001 (alvo/fórmula/período) e lead qualificado aprovados antes de qualquer KPI de resultado.
- **B3-RACI-01:** matriz nominal de handoffs antes da prova F3-T06 (task de materialização usa papéis provisórios registrados).
- **B3-DHO-01:** lista de sinais autorizados + política antes de dado real de sinal (F3-T07/T08 fail-closed com fixtures).
