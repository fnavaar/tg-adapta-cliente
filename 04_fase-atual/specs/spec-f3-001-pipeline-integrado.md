# SPEC-F3-001 — Pipeline integrado de demanda (estados, motivação e jornada única)

**Fase:** 3
**Status:** planejada
**Emendas vigentes:** E-F3-001-01 (2026-10-06) — hierarquia Demanda → Propostas → Vagas; E-F3-001-02 (2026-10-07) — prazos sem SLA autônomo
**Dono:** comercial/gerentes de negócio operam; direção aprova taxonomia; consultor valida a primeira demonstração
**Origem no escopo:** Fase 3; C-03; DC-001; DC-004; RQ-003/RQ-004; G-002
**Degrau da solução:** reuso — evoluir o pipeline mínimo da F1 (`demandas`) para a jornada operacional completa com proposta/vaga e retorno; sem novo sistema, sem integração externa.

## Contexto e decisões fechadas

- **Estado atual:** a F1 entregou pipeline mínimo com estados `suspect`, `prospect`, `lead qualificado`, `oportunidade`, `proposta`, `vaga aberta`, `ganho`, `perdido`, `sem timing`, `desqualificado`, com estado único, dono, próxima ação e prazo (SPEC-F1-002, RN-F1-006..012; `demandas` com 10 registros preservados). A F2 ligou campanhas/experimentos à captura com atribuição de fonte única (F2-002) e decisão de experimento (F2-003). O pós-captura até proposta/vaga com prazo aplicável e retorno da operação não existe.
- **Estado desejado:** um caso inbound e um outbound percorrem o pipeline integrado até oportunidade ou encerramento; um caso de proposta/vaga retorna ao dashboard com origem e motivo; oportunidade parada tem prazo, escalonamento e estado terminal.
- **Decisões já fechadas:** estados e critérios de entrada/saída da F1 são a base (não reabrir taxonomia já aprovada); inbound e outbound não são misturados; vaga aberta não é fechamento (RN-F1-010); dado desconhecido nunca é completado por inferência; nenhuma ação externa automatizada (RN-F1-012). **Decisão de produto da Talent Group (25/09, changelog):** a hierarquia da F3-T01 é **Demanda → várias propostas → várias vagas**, com a demanda como registro principal — formalizada na E-F3-001-01 abaixo.
- **Bloqueios:** B3-ID-01 — contrato de identidade por fonte para a ligação origem→oportunidade→vaga (identidade multi-fonte da F1-T06 segue pendente; usar `sistema_origem_tecnico + record_id` no escopo da fonte declarada; sem dedupe por inferência; sem relação estrutural automática `demandas`↔`experimentos_f2`). B3-MET-01 — definição de "lead qualificado" segue pendente de aprovação (G-001/F1): transição para `lead qualificado` e KPI de qualificação continuam condicionados (RN-F1-011).

## Resultado observável

1. Um caso inbound e um caso outbound, criados a partir de registros da F1/F2 (ou fixtures sintéticos quando não houver dado real autorizado), percorrem `suspect/prospect` → qualificação → `oportunidade` → `proposta`/`vaga aberta` → terminal (`ganho`/`perdido`/`sem timing`/`desqualificado`) com dono, próxima ação, prazo e motivo em cada transição.
2. Um caso de proposta/vaga devolve resultado da operação (R&S/Alocação/SOS) ao registro de origem com estado, prazo/capacidade e motivo — a origem permanece rastreável até o dashboard.
3. Oportunidade parada (sem próxima ação vencida ou sem resposta) tem prazo de escalonamento, estado de escalonamento e caminho para estado terminal com motivo.

## Limites e dependências

- **Inclui:** transições operacionais do pipeline; campos de proposta/vaga (número, serviço, área, prazo operacional [exclusivo da vaga — E-F3-001-02], capacidade, resultado, motivo); **coleções relacionadas `propostas` e `vagas` conforme E-F3-001-01**; retorno da operação; escalonamento de oportunidade parada; log de transição append-only; filtros por tipo de origem (inbound/outbound).
- **Fora de escopo:** integração com CRM/ERP/ATS externo; scraping de vagas; automação de contato; substituição do ERP; Customer Success completo; decisão comercial sem pessoa responsável; KPI de resultado contra alvo (bloqueado por B3-MET-01); **qualquer estrutura além das coleções relacionadas `propostas`/`vagas` (ex.: empresa como registro separado, pipeline de vagas, estado em proposta/vaga) — ver E-F3-001-01**.
- **Entradas e pré-condições:** F1/F2 aceitas (estados, dicionário, atribuição); registros de amostra autorizados ou fixtures sintéticos; matriz de papéis/handoffs (B3-RACI-01) para a prova de retorno — a task de configuração pode avançar com papéis provisórios registrados, mas a prova de handoff exige a matriz nominal.
- **Saídas/artefatos:** superfície de pipeline integrado (extensão do painel existente); campos/estados de proposta/vaga; coleções relacionadas `propostas`/`vagas`; log de transições; evidência `pipeline-f3.md` na pasta de entregas da fase.
- **Dependências e responsáveis:** comercial classifica e age; R&S/Alocação/SOS devolve estado/prazo/resultado; direção aprova prazos/escalonamento; consultor revisa.
- **Atores e permissões mínimas:** comercial/gerentes escrevem estado, dono, próxima ação, prazo, resultado; operação escreve somente o retorno de proposta/vaga; direção lê; acesso por papel server-side, sem dado sensível.
- **Superfícies/arquivos/configurações afetadas:** coleção `demandas` (campos novos não destrutivos), **coleções relacionadas `propostas` e `vagas` (novas, criadas por E-F3-001-01)** e superfície de painel; nenhuma migration destrutiva; nenhum hook de escrita externa.
- **Risco e plano B:** classificação inconsistente entre pessoas → critérios escritos por estado + prova de equivalência (critério binário da fase); pipeline inflado → exigir próxima ação/prazo e motivo terminal; retorno da operação não vier → pendência visível com dono, sem inferir resultado.
- **Rollback ou reversão:** suspender novas transições na superfície integrada, preservar registros e log, retornar ao registro manual; não apagar histórico.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Pipeline F1 (`demandas`) → pipeline integrado | Registro existente + dicionário F1 | `record_id`, origem, tipo (inbound/outbound), canal, campanha, serviço, estado, dono, próxima ação, prazo, proposta/vaga {nº, serviço, área, prazo operacional (vaga), capacidade}, resultado, motivo, evidência | Escrita por papel server-side | Transição idempotente por `record_id` + versão de estado; reprocessar não duplica | Transição sem evidência mínima é rejeitada e registrada (RN-F1-007) |
| Campanha/experimento F2 → origem da demanda | Atribuição F2-002 (fonte única declarada) | `sistema_origem_tecnico`, `record_id` da fonte, campanha/experimento_id | Leitura | Ligação por identidade explícita da fonte; sem dedupe por inferência (B3-ID-01) | Fonte ausente → origem `desconhecida` visível, nunca inventada |
| Operação (R&S/Alocação/SOS) → retorno | Registro de proposta/vaga | estado do retorno, prazo, capacidade, resultado, motivo | Escrita do papel operação | Retorno idempotente por proposta/vaga; novo evento = novo registro | Sem retorno no prazo → pendência com dono e escalonamento (RN-F3-004) |
| Propostas/vagas relacionadas → demanda (E-F3-001-01) | Coleções novas `propostas`/`vagas` | `demanda_id` (= `record_id` da demanda), `proposta_id` (na vaga), nº, serviço, área, prazo operacional (vaga; proposta sem prazo próprio — E-F3-001-02), resultado, motivo, evidência | Escrita por papel server-side | Criação idempotente por (`demanda_id`, nº); reprocessar não duplica | Filho sem demanda válida → rejeitado; empresa em filho → rejeitado |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-001 — Jornada única | Registro ativo | Estado único + log append-only de transições (estende RN-F1-006) | Sem evidência: mantém estado anterior + pendência | C-03 |
| RN-F3-002 — Proposta/vaga rastreável | Estado `proposta` ou `vaga aberta` | Exigir nº/serviço/área + prazo operacional (vaga) + dono do retorno; proposta não tem prazo próprio; origem permanece visível | Vaga sem número/serviço → pendência, não avança | §Fase 3, C-03 |
| RN-F3-003 — Vaga não é fechamento | `vaga aberta` | Contar como demanda aberta; resultado posterior separado | `ganho` exige evidência de decisão (RN-F1-010) | RQ-008 |
| RN-F3-004 — Oportunidade parada | Sem próxima ação vencida ou sem resposta no prazo aplicável (vaga: prazo operacional; ação comercial: prazo da próxima ação — E-F3-001-02) | Escalonar com prazo e dono; caminho para terminal com motivo | Sem matriz RACI (B3-RACI-01): registrar pendência com dono provisório | §Fase 3 regras |
| RN-F3-005 — Sem inferência de origem | Origem/campanha ausente | Exibir `desconhecido`; nunca completar por suposição | — | C-01, §Fase 1 |
| RN-F3-006 — Contagem pela fonte | Qualquer contagem/painel | Recalcular a partir da fonte via núcleo de reconciliação compartilhado; sem cópia divergente | Divergência fonte×painel → pendência com dono | EV-05, F1 |
| RN-F3-007 — Hierarquia única (E-F3-001-01) | Registro de proposta/vaga | Persistir como registro relacionado (`demanda_id`); demanda é o registro principal; empresa permanece campo único da demanda | Empresa duplicada em proposta/vaga → rejeitado | Decisão Champion 25/09 |
| RN-F3-008 — Sem pipeline paralelo (E-F3-001-01) | Proposta/vaga | Sem estado de pipeline próprio; vaga tem prazo operacional próprio (distinto do prazo da próxima ação da demanda); proposta não tem prazo operacional próprio | Estado de pipeline em filho → rejeitado | Decisão Champion 25/09; harmonização 06/10 |
| RN-F3-009 — Sem agregação automática (E-F3-001-01) | Registro filho | Estado da demanda muda somente por ação do Comercial com evidência (RN-F1-007); filho nunca altera o estado do pai | Filho alterando pai → rejeitado e registrado no log | Decisão Champion 25/09 |

## Fluxo e regras

1. Carregar somente registros aceitos (F1/F2) ou fixtures sintéticos autorizados.
2. Classificar percorrendo estados com evidência mínima por transição (RN-F1-007).
3. Ao virar `oportunidade`, registrar proposta/vaga como **registros relacionados** à demanda (E-F3-001-01) com nº/serviço/área/prazo operacional (vaga) e dono do retorno.
4. Operação devolve estado/prazo/capacidade/resultado/motivo; o registro origem é atualizado sem perder rastreabilidade.
5. Oportunidade parada escalona por prazo; terminal exige motivo (RN-F1-009).

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | caso inbound + caso outbound completos | jornada até terminal ou oportunidade ativa com dono/próxima ação/prazo | falha de transição → log + pendência |
| Limite | proposta/vaga sem retorno no prazo aplicável (vaga: prazo operacional) | pendência visível com dono + escalonamento | sem RACI nominal → dono provisório + pendência |
| Falha | transição sem evidência / retorno duplicado / filho sem demanda válida | rejeitada/idempotente; registro em log | reprocessar não duplica; revisar manualmente |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** SPEC-F1-002 (estados/RN-F1-006..012), SPEC-F2-002 (atribuição), escopo §5 C-03 e §7 Fase 3; `05_entregas/fase-1/specs/` e o painel existente; **E-F3-001-01 (emendas desta SPEC)**.
2. **Alterar somente:** coleção `demandas` (campos não destrutivos), **coleções relacionadas `propostas` e `vagas` (novas, criadas conforme E-F3-001-01)**, superfície de pipeline/painel, log de transições.
3. **Não alterar:** estados/taxonomia aprovados da F1; atribuição F2; `experimentos_f2`; qualquer conector Meta; permissões globais; histórico; **criar qualquer estrutura além de `propostas`/`vagas` relacionadas (E-F3-001-01)**.
4. **Executar nesta ordem:** fixtures → coleções relacionadas `propostas`/`vagas` → campos de proposta/vaga → transições com evidência → retorno da operação → escalonamento → prova de equivalência entre duas pessoas.
5. **Parar e pedir validação quando:** faltar matriz RACI nominal para a prova de handoff; alguém pedir dedupe por inferência, integração externa ou KPI contra alvo (B3-MET-01); qualquer escrita externa; **qualquer necessidade de estrutura fora da hierarquia Demanda→Propostas→Vagas (E-F3-001-01)**.
6. **Estado válido ao parar:** pipeline F1/F2 preservado; novos campos inertes; provas parciais registradas.

## Checklist de execução

- [ ] Caso inbound e outbound completos com dono, próxima ação, prazo e motivo em cada transição.
- [ ] Proposta/vaga com nº/serviço/área e dono do retorno; vaga com prazo operacional (proposta sem prazo próprio — E-F3-001-02).
- [ ] Propostas e vagas persistidas como registros relacionados à demanda (E-F3-001-01), sem empresa duplicada e sem estado de pipeline próprio.
- [ ] Retorno da operação registrado com origem rastreável.
- [ ] Oportunidade parada escalona e tem caminho terminal com motivo.
- [ ] Caminhos principal, limite e falha exercitados; evidência anexada; log append-only íntegro.

## Critérios de aceite

- [ ] **CA-3-01:** um caso inbound e um outbound percorrem o pipeline integrado até oportunidade ou encerramento com dono, próxima ação/prazo (ou motivo terminal) e log de transição.
- [ ] **CA-3-02:** um caso de proposta/vaga retorna ao registro de origem com estado, prazo/capacidade, resultado e motivo, preservando a origem até o dashboard.
- [ ] **CA-3-03:** oportunidade parada sem resposta no prazo aplicável (vaga: prazo operacional; ação comercial: prazo da próxima ação — E-F3-001-02) gera escalonamento com prazo e dono, e caminho para estado terminal com motivo — nunca permanece invisível.
- [ ] **CA-3-04 (E-F3-001-01):** propostas e vagas existem como registros relacionados à demanda (sem empresa duplicada, sem estado de pipeline próprio, vaga com prazo operacional próprio) e nenhuma operação em filho altera o estado da demanda.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | transição sem evidência; retorno duplicado; vaga sem nº/serviço; filho sem demanda válida; filho tentando alterar estado do pai | tentar operar no pipeline | rejeição/pendência registrada; idempotência (não duplica) | log/captura |
| GREEN | caso inbound + outbound completos com proposta/vaga e retorno | percorrer jornada na superfície | CA-3-01 e CA-3-02 demonstráveis | registro + captura |
| REFACTOR/REGRESSÃO | reprocessar lote; verificar contagens pelo núcleo de reconciliação; escalonar oportunidade parada; verificar hierarquia e não-agregação | replay + consulta | sem duplicação; contagens = fonte; escalonamento visível; CA-3-04 demonstrável | comparação + log |

**Dados/fixtures:** fixtures sintéticos inbound/outbound (sem contatos reais); registros da amostra F1/F2 somente se autorizados.
**Caminhos de erro obrigatórios:** transição sem evidência; retorno duplicado; prazo aplicável vencido sem retorno (prazo operacional da vaga ou prazo da próxima ação — E-F3-001-02); origem ausente; filho sem demanda válida; filho alterando pai.
**Evidência exigida:** log de transições, capturas da jornada, comparação fonte×painel, bateria humana (prova de equivalência entre duas pessoas — EV-08).

## Handoff e operação

- **Como demonstrar:** percorrer os dois casos na superfície até terminal/oportunidade; mostrar o retorno da operação e o escalonamento; duas pessoas classificam o mesmo caso de forma equivalente.
- **Como operar depois:** comercial mantém estados/próxima ação; operação devolve retornos; direção revisa pendências semanais.
- **Como monitorar:** registros sem próxima ação; prazos vencidos (prazo operacional de vaga; prazo da próxima ação); terminais sem motivo; divergência fonte×painel.
- **Pendência conhecida:** B3-ID-01 (identidade por fonte) e B3-MET-01 (lead qualificado/alvo) seguem abertos e nomeados.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T01 | Materializar campos de proposta/vaga, retorno e escalonamento no pipeline com massa sintética | Comercial/gerentes | F3-001 | CA-3-01, CA-3-02, CA-3-04 | Dados e integrações; Fluxo e regras; Checklist | Captura/export da jornada dupla com proposta/vaga e retorno; hierarquia Demanda→Propostas→Vagas demonstrada | F2 aceita; fixtures autorizados; E-F3-001-01 vigente | ☐ |
| F3-T02 | Provar jornada dupla, retorno da operação, escalonamento e equivalência entre duas pessoas | Comercial + operação + direção | F3-001 | CA-3-01, CA-3-02, CA-3-03, CA-3-04 | Critérios de aceite; TDD da SPEC | Bateria humana de equivalência + log de transições | F3-T01 aceita por teste humano; matriz RACI nominal (B3-RACI-01) | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
| 2026-10-06 | DÚVIDA do Champion registrada no changelog em 2026-09-25 | E-F3-001-01 | Formalizar a hierarquia Demanda → Propostas → Vagas decidida pela Talent Group e os limites de alteração da F3-T01 |
| 2026-10-07 | DÚVIDA do Champion registrada no changelog em 2026-10-06 (SLA/prazo) | E-F3-001-02 | Eliminar o SLA autônomo: prazo operacional exclusivo da vaga; demanda usa o prazo da próxima ação; proposta sem prazo próprio |

### E-F3-001-01 — Hierarquia Demanda → Propostas → Vagas (2026-10-06)

**Origem:** DÚVIDA registrada no changelog em 2026-09-25 pelo Champion (João Paulo) — a decisão de produto sobre a hierarquia da F3-T01 não estava autorizada explicitamente pela SPEC (as superfícies afetadas listavam apenas `demandas`, painel e log).

**Decisão de produto (Talent Group, 25/09):** a hierarquia da F3-T01 é **Demanda → várias propostas → várias vagas**, mantendo a demanda como registro principal, sem duplicar a empresa por proposta/vaga e sem criar outro pipeline.

**O que esta emenda autoriza (para a F3-T01 e demais tasks desta SPEC):**

1. **Coleções relacionadas `propostas` e `vagas`** (novas, criadas nesta fase), cada registro vinculado à demanda de origem por `demanda_id` (= `record_id` da `demandas`); cada vaga vincula também `proposta_id`. Proposta → 1..N vagas.
2. **Sem duplicação de empresa:** a empresa permanece campo único da demanda; propostas e vagas não carregam campo de empresa próprio — referenciam a demanda.
3. **Prazo operacional próprio da vaga:** campo de prazo operacional na vaga, distinto do ciclo de estados da demanda — e exclusivo da vaga: **proposta e demanda não possuem prazo operacional global próprio** (na demanda, o prazo citado é sempre o da próxima ação, taxonomia F1 RN-F1-006..012).
4. **Estado permanece único na demanda:** propostas e vagas NÃO têm estado de pipeline próprio (não é novo pipeline); o ciclo de estados RN-F1-006..012 continua exclusivamente na demanda, controlado pelo Comercial.

**Limites de alteração (não autorizado por esta emenda):**

- Nenhuma agregação automática: o estado da demanda só muda por ação do Comercial com evidência (RN-F1-007); registros filhos nunca alteram o estado do pai (RN-F3-009).
- Nenhum outro pipeline, coleção, campo de estado em proposta/vaga ou dedupe por inferência.
- Nenhuma migration destrutiva em `demandas` ou nas coleções novas; nenhum hook de escrita externa.
- Fora desta emenda: qualquer estrutura além de `propostas`/`vagas` relacionadas (ex.: empresa como registro separado, pipeline de vagas, hierarquia alternativa).

**Harmonização (06/10, devolutiva do Champion):** o prazo operacional pertence exclusivamente à vaga; proposta e demanda não têm prazo operacional global próprio — o prazo da demanda é o da próxima ação (taxonomia F1). Referência cruzada: E-F3-002-01 (renumeração CA-3-11/12 na F3-002).

**Vigência:** vale para a F3-T01 e demais tasks desta SPEC. Decisões de produto adicionais pertencem à Talent Group; emendas documentais são responsabilidade da consultoria conforme a Constituição do projeto.


### E-F3-001-02 — Prazos sem SLA autônomo (2026-10-07)

**Origem:** DÚVIDA do Champion registrada no changelog em 2026-10-06 — a SPEC ainda usava "SLA da proposta", "SLA vencido", "sem retorno no SLA" e equivalentes, implicando um segundo prazo autônomo concorrendo com o prazo operacional.

**Decisão de produto (Talent Group, 06/10):** não existe prazo denominado SLA concorrendo com o prazo operacional. Cada vaga tem seu **prazo operacional** próprio; **proposta e demanda não têm prazo operacional global** — na demanda, o prazo é sempre o da **próxima ação comercial** (taxonomia F1, RN-F1-006..012). Não se cria conceito de SLA nem regra de prazo não definida pelo negócio nesta task.

**Harmonização aplicada (varredura desta SPEC):**

1. O campo "SLA" de proposta está **removido do contrato**: proposta carrega nº/serviço/área/dono do retorno/resultado/motivo/evidência e **não tem prazo próprio**; a vaga carrega **prazo operacional** (campo único de prazo da vaga).
2. "sem retorno no SLA" → **sem retorno dentro do prazo aplicável** (vaga: prazo operacional da vaga; ação comercial/demanda: prazo da próxima ação).
3. "SLA vencido" → **prazo aplicável vencido** (prazo operacional da vaga ou prazo da próxima ação, conforme o contexto).
4. RN-F3-002, RN-F3-004, fluxo, cenários, checklist, CA-3-03 e TDD passam a referenciar exclusivamente "prazo operacional (vaga)" e "prazo da próxima ação (demanda)".
5. O escalonamento continua valendo: vencido o prazo aplicável sem retorno/resposta, escala com prazo e dono (RN-F3-004) — usando o mesmo prazo aplicável, nunca um SLA separado.

**Delimitação (varredura preventiva das 4 SPECs F3):** o **"SLA de aceite" do handoff** (SPEC-F3-003) é conceito distinto — prazo de resposta/aceite da passagem de guarda, com valores definidos pela matriz RACI nominal (B3-RACI-01) — e permanece válido (ver E-F3-003-01). Na F3-002, a harmonização equivalente já consta da E-F3-002-01 ("prazo aplicável à etapa").

**Vigência:** vale para a F3-T01, F3-T02 e demais tasks desta SPEC. Decisões de produto adicionais pertencem à Talent Group; emendas documentais são responsabilidade da consultoria conforme a Constituição do projeto.
