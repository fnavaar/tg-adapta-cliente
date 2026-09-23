# Fase 3 — Tasks gerais

**Plano:** TG Mais Serviços de Tecnologia e RH LTDA · `6b09d189`  
**Estado:** Fase 3 liberada para execução controlada; 0/8 tasks concluídas.  
**Champion:** João Paulo  
**Prazo de referência:** 30/09/2026 (proposto para o ciclo; ajustável pelo Champion).  
**Elegível:** F3-T01 é a única task elegível; F3-T02..T08 permanecem bloqueadas por dependências.  
**Regra:** uma task por vez, com evidências da SPEC e teste humano antes da seguinte.

## Tasks

| ID | Leva | Task | Dono | SPEC | Critério | Subseção exata da SPEC | Recorte da prova | Evidência esperada | Pré-condições | Ponto de parada | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| F3-T01 | 1 | Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética. | João Paulo | F3-001 | CA-3-01, CA-3-02 | Dados e integrações; Fluxo e regras; Checklist | Fixtures inbound/outbound, proposta/vaga, retorno e escalonamento. | Captura/export da jornada e log de transições. | F2 9/9 aceita; fixtures sintéticos; pipeline F1/F2 preservado. | Parar se exigir dado real, dedupe por inferência ou integração externa. | ELEGÍVEL |
| F3-T02 | 2 | Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas. | João Paulo | F3-001 | CA-3-01..03 | Critérios de aceite; TDD | RED/GREEN/regressão, replay e bateria de equivalência. | Bateria humana + log + comparação fonte×painel. | F3-T01 aceita; B3-RACI-01 para a prova de handoff. | Parar sem critério de classificação ou matriz nominal. | BLOQUEADA |
| F3-T03 | 3 | Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética. | João Paulo | F3-002 | CA-3-04 | Dados e integrações; Fluxo e regras; Checklist | Visões por estado, gargalo, tempos e retorno; KPI contra alvo bloqueado. | Captura/export com contagens reproduzíveis. | F3-T01 aceita. | Parar se a contagem não reproduzir a fonte ou se pedirem KPI sem alvo. | BLOQUEADA |
| F3-T04 | 4 | Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens. | João Paulo | F3-002 | CA-3-04/05 | Critérios de aceite; TDD | Leitura completa, volume×qualidade, pendência G-001 e regressão F1/F2. | Bateria humana + comparação fonte×dashboard. | F3-T03 aceita. | Parar se esconder lacuna ou misturar volume com qualidade. | BLOQUEADA |
| F3-T05 | 3 | Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética. | João Paulo | F3-003 | CA-3-06 | Dados e integrações; Fluxo e regras; Checklist | HO-F3-001 com destinatário, SLA, aceite, recusa e expiração. | Captura/export do registro e estados. | F3-T01 aceita; papéis provisórios registrados. | Parar se exigir disparo externo ou encerramento sem responsável. | BLOQUEADA |
| F3-T06 | 5 | Provar aceite, recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal. | João Paulo | F3-003 | CA-3-06..08 | Critérios de aceite; TDD | Bateria humana completa e falha segura sem retry automático. | Matriz RACI + log de eventos + evidências. | F3-T05 aceita; B3-RACI-01 fechado. | Parar sem matriz nominal ou se pedirem retry automático. | BLOQUEADA |
| F3-T07 | 4 | Materializar objeto separado de sinal de conta do DHO com lista versionada e permissões fail-closed. | João Paulo | F3-004 | CA-3-09 | Dados e integrações; Fluxo e regras; Checklist | Objeto inativo com fixture, permissões server-side e prova negativa. | Captura do objeto + prova negativa + decisão C-06. | F3-T01 aceita; decisão C-06 registrada. | Parar se pedirem dado real sem política ou exposição ao comercial. | BLOQUEADA |
| F3-T08 | 6 | Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política. | João Paulo | F3-004 | CA-3-09/10 | Critérios de aceite; TDD | Sinal em fixture, isolamento, duplicata, rollback e encaminhamento humano. | Bateria humana + lista versionada + decisão de uso. | F3-T07 aceita. | Parar se gerar ação sem decisor ou aparecer no pipeline comercial. | BLOQUEADA |

## Bloqueios transversais

- **B3-META-01:** nenhuma task da F3 lê Meta.
- **B3-ID-01:** identidade por fonte; sem dedupe por inferência.
- **B3-MET-01:** alvo, fórmula, período e lead qualificado antes de KPI de resultado.
- **B3-RACI-01:** matriz nominal antes da prova F3-T06.
- **B3-DHO-01:** lista de sinais e política antes de dado real de sinal; F3-004 permanece fail-closed com fixtures.
