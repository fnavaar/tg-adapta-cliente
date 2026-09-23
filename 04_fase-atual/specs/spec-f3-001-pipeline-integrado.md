# SPEC-F3-001 — Pipeline integrado de demanda (estados, motivação e jornada única)

**Fase:** 3
**Status:** planejada
**Dono:** comercial/gerentes de negócio operam; direção aprova taxonomia; consultor valida a primeira demonstração
**Origem no escopo:** Fase 3; C-03; DC-001; DC-004; RQ-003/RQ-004; G-002
**Degrau da solução:** reuso — evoluir o pipeline mínimo da F1 (`demandas`) para a jornada operacional completa com proposta/vaga e retorno; sem novo sistema, sem integração externa.

## Contexto e decisões fechadas

- **Estado atual:** a F1 entregou pipeline mínimo com estados `suspect`, `prospect`, `lead qualificado`, `oportunidade`, `proposta`, `vaga aberta`, `ganho`, `perdido`, `sem timing`, `desqualificado`, com estado único, dono, próxima ação e prazo (SPEC-F1-002, RN-F1-006..012; `demandas` com 10 registros preservados). A F2 ligou campanhas/experimentos à captura com atribuição de fonte única (F2-002) e decisão de experimento (F2-003). O pós-captura até proposta/vaga com SLA e retorno da operação não existe.
- **Estado desejado:** um caso inbound e um outbound percorrem o pipeline integrado até oportunidade ou encerramento; um caso de proposta/vaga retorna ao dashboard com origem e motivo; oportunidade parada tem prazo, escalonamento e estado terminal.
- **Decisões já fechadas:** estados e critérios de entrada/saída da F1 são a base (não reabrir taxonomia já aprovada); inbound e outbound não são misturados; vaga aberta não é fechamento (RN-F1-010); dado desconhecido nunca é completado por inferência; nenhuma ação externa automatizada (RN-F1-012).
- **Bloqueios:** B3-ID-01 — contrato de identidade por fonte para a ligação origem→oportunidade→vaga (identidade multi-fonte da F1-T06 segue pendente; usar `sistema_origem_tecnico + record_id` no escopo da fonte declarada; sem dedupe por inferência; sem relação estrutural automática `demandas`↔`experimentos_f2`). B3-MET-01 — definição de "lead qualificado" segue pendente de aprovação (G-001/F1): transição para `lead qualificado` e KPI de qualificação continuam condicionados (RN-F1-011).

## Resultado observável

1. Um caso inbound e um caso outbound, criados a partir de registros da F1/F2 (ou fixtures sintéticos quando não houver dado real autorizado), percorrem `suspect/prospect` → qualificação → `oportunidade` → `proposta`/`vaga aberta` → terminal (`ganho`/`perdido`/`sem timing`/`desqualificado`) com dono, próxima ação, prazo e motivo em cada transição.
2. Um caso de proposta/vaga devolve resultado da operação (R&S/Alocação/SOS) ao registro de origem com estado, prazo/capacidade e motivo — a origem permanece rastreável até o dashboard.
3. Oportunidade parada (sem próxima ação vencida ou sem resposta) tem prazo de escalonamento, estado de escalonamento e caminho para estado terminal com motivo.

## Limites e dependências

- **Inclui:** transições operacionais do pipeline; campos de proposta/vaga (número, serviço, área, SLA, capacidade, resultado, motivo); retorno da operação; escalonamento de oportunidade parada; log de transição append-only; filtros por tipo de origem (inbound/outbound).
- **Fora de escopo:** integração com CRM/ERP/ATS externo; scraping de vagas; automação de contato; substituição do ERP; Customer Success completo; decisão comercial sem pessoa responsável; KPI de resultado contra alvo (bloqueado por B3-MET-01).
- **Entradas e pré-condições:** F1/F2 aceitas (estados, dicionário, atribuição); registros de amostra autorizados ou fixtures sintéticos; matriz de papéis/handoffs (B3-RACI-01) para a prova de retorno — a task de configuração pode avançar com papéis provisórios registrados, mas a prova de handoff exige a matriz nominal.
- **Saídas/artefatos:** superfície de pipeline integrado (extensão do painel existente); campos/estados de proposta/vaga; log de transições; evidência `pipeline-f3.md` na pasta de entregas da fase.
- **Dependências e responsáveis:** comercial classifica e age; R&S/Alocação/SOS devolve estado/prazo/resultado; direção aprova SLA/escalonamento; consultor revisa.
- **Atores e permissões mínimas:** comercial/gerentes escrevem estado, dono, próxima ação, prazo, resultado; operação escreve somente o retorno de proposta/vaga; direção lê; acesso por papel server-side, sem dado sensível.
- **Superfícies/arquivos/configurações afetadas:** coleção `demandas` (campos novos não destrutivos) e superfície de painel; nenhuma migration destrutiva; nenhum hook de escrita externa.
- **Risco e plano B:** classificação inconsistente entre pessoas → critérios escritos por estado + prova de equivalência (critério binário da fase); pipeline inflado → exigir próxima ação/prazo e motivo terminal; retorno da operação não vier → pendência visível com dono, sem inferir resultado.
- **Rollback ou reversão:** suspender novas transições na superfície integrada, preservar registros e log, retornar ao registro manual; não apagar histórico.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Pipeline F1 (`demandas`) → pipeline integrado | Registro existente + dicionário F1 | `record_id`, origem, tipo (inbound/outbound), canal, campanha, serviço, estado, dono, próxima ação, prazo, proposta/vaga {nº, serviço, área, SLA, capacidade}, resultado, motivo, evidência | Escrita por papel server-side | Transição idempotente por `record_id` + versão de estado; reprocessar não duplica | Transição sem evidência mínima é rejeitada e registrada (RN-F1-007) |
| Campanha/experimento F2 → origem da demanda | Atribuição F2-002 (fonte única declarada) | `sistema_origem_tecnico`, `record_id` da fonte, campanha/experimento_id | Leitura | Ligação por identidade explícita da fonte; sem dedupe por inferência (B3-ID-01) | Fonte ausente → origem `desconhecida` visível, nunca inventada |
| Operação (R&S/Alocação/SOS) → retorno | Registro de proposta/vaga | estado do retorno, prazo, capacidade, resultado, motivo | Escrita do papel operação | Retorno idempotente por proposta/vaga; novo evento = novo registro | Sem retorno no prazo → pendência com dono e escalonamento (RN-F3-004) |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-001 — Jornada única | Registro ativo | Estado único + log append-only de transições (estende RN-F1-006) | Sem evidência: mantém estado anterior + pendência | C-03 |
| RN-F3-002 — Proposta/vaga rastreável | Estado `proposta` ou `vaga aberta` | Exigir nº/serviço/área + SLA + dono do retorno; origem permanece visível | Vaga sem número/serviço → pendência, não avança | §Fase 3, C-03 |
| RN-F3-003 — Vaga não é fechamento | `vaga aberta` | Contar como demanda aberta; resultado posterior separado | `ganho` exige evidência de decisão (RN-F1-010) | RQ-008 |
| RN-F3-004 — Oportunidade parada | Sem próxima ação vencida ou sem resposta no SLA | Escalonar com prazo e dono; caminho para terminal com motivo | Sem matriz RACI (B3-RACI-01): registrar pendência com dono provisório | §Fase 3 regras |
| RN-F3-005 — Sem inferência de origem | Origem/campanha ausente | Exibir `desconhecido`; nunca completar por suposição | — | C-01, §Fase 1 |
| RN-F3-006 — Contagem pela fonte | Qualquer contagem/painel | Recalcular a partir da fonte via núcleo de reconciliação compartilhado; sem cópia divergente | Divergência fonte×painel → pendência com dono | EV-05, F1 |

## Fluxo e regras

1. Carregar somente registros aceitos (F1/F2) ou fixtures sintéticos autorizados.
2. Classificar percorrendo estados com evidência mínima por transição (RN-F1-007).
3. Ao virar `oportunidade`, registrar proposta/vaga com nº/serviço/área/SLA e dono do retorno.
4. Operação devolve estado/prazo/capacidade/resultado/motivo; o registro origem é atualizado sem perder rastreabilidade.
5. Oportunidade parada escalona por prazo; terminal exige motivo (RN-F1-009).

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | caso inbound + caso outbound completos | jornada até terminal ou oportunidade ativa com dono/próxima ação/prazo | falha de transição → log + pendência |
| Limite | proposta/vaga sem retorno no SLA | pendência visível com dono + escalonamento | sem RACI nominal → dono provisório + pendência |
| Falha | transição sem evidência / retorno duplicado | rejeitada/idempotente; registro em log | reprocessar não duplica; revisar manualmente |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** SPEC-F1-002 (estados/RN-F1-006..012), SPEC-F2-002 (atribuição), escopo §5 C-03 e §7 Fase 3; `05_entregas/fase-1/specs/` e o painel existente.
2. **Alterar somente:** coleção `demandas` (campos não destrutivos), superfície de pipeline/painel, log de transições.
3. **Não alterar:** estados/taxonomia aprovados da F1; atribuição F2; `experimentos_f2`; qualquer conector Meta; permissões globais; histórico.
4. **Executar nesta ordem:** fixtures → campos de proposta/vaga → transições com evidência → retorno da operação → escalonamento → prova de equivalência entre duas pessoas.
5. **Parar e pedir validação quando:** faltar matriz RACI nominal para a prova de handoff; alguém pedir dedupe por inferência, integração externa ou KPI contra alvo (B3-MET-01); qualquer escrita externa.
6. **Estado válido ao parar:** pipeline F1/F2 preservado; novos campos inertes; provas parciais registradas.

## Checklist de execução

- [ ] Caso inbound e outbound completos com dono, próxima ação, prazo e motivo em cada transição.
- [ ] Proposta/vaga com nº/serviço/área/SLA e dono do retorno.
- [ ] Retorno da operação registrado com origem rastreável.
- [ ] Oportunidade parada escalona e tem caminho terminal com motivo.
- [ ] Caminhos principal, limite e falha exercitados; evidência anexada; log append-only íntegro.

## Critérios de aceite

- [ ] **CA-3-01:** um caso inbound e um outbound percorrem o pipeline integrado até oportunidade ou encerramento com dono, próxima ação/prazo (ou motivo terminal) e log de transição.
- [ ] **CA-3-02:** um caso de proposta/vaga retorna ao registro de origem com estado, prazo/capacidade, resultado e motivo, preservando a origem até o dashboard.
- [ ] **CA-3-03:** oportunidade parada sem resposta no SLA gera escalonamento com prazo e dono, e caminho para estado terminal com motivo — nunca permanece invisível.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | transição sem evidência; retorno duplicado; vaga sem nº/serviço | tentar operar no pipeline | rejeição/pendência registrada; idempotência (não duplica) | log/captura |
| GREEN | caso inbound + outbound completos com proposta/vaga e retorno | percorrer jornada na superfície | CA-3-01 e CA-3-02 demonstráveis | registro + captura |
| REFACTOR/REGRESSÃO | reprocessar lote; verificar contagens pelo núcleo de reconciliação; escalonar oportunidade parada | replay + consulta | sem duplicação; contagens = fonte; escalonamento visível | comparação + log |

**Dados/fixtures:** fixtures sintéticos inbound/outbound (sem contatos reais); registros da amostra F1/F2 somente se autorizados.
**Caminhos de erro obrigatórios:** transição sem evidência; retorno duplicado; SLA vencido sem retorno; origem ausente.
**Evidência exigida:** log de transições, capturas da jornada, comparação fonte×painel, bateria humana (prova de equivalência entre duas pessoas — EV-08).

## Handoff e operação

- **Como demonstrar:** percorrer os dois casos na superfície até terminal/oportunidade; mostrar o retorno da operação e o escalonamento; duas pessoas classificam o mesmo caso de forma equivalente.
- **Como operar depois:** comercial mantém estados/próxima ação; operação devolve retornos; direção revisa pendências semanais.
- **Como monitorar:** registros sem próxima ação; SLAs vencidos; terminais sem motivo; divergência fonte×painel.
- **Pendência conhecida:** B3-ID-01 (identidade por fonte) e B3-MET-01 (lead qualificado/alvo) seguem abertos e nomeados.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T01 | Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética | Comercial/gerentes | F3-001 | CA-3-01, CA-3-02 | Dados e integrações; Fluxo e regras; Checklist | Captura/export da jornada dupla com proposta/vaga e retorno | F2 aceita; fixtures autorizados | ☐ |
| F3-T02 | Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas | Comercial + operação + direção | F3-001 | CA-3-01, CA-3-02, CA-3-03 | Critérios de aceite; TDD da SPEC | Bateria humana de equivalência + log de transições | F3-T01 aceita por teste humano; matriz RACI nominal (B3-RACI-01) | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
