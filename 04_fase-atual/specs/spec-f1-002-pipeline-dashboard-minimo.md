# SPEC-F1-002 — Pipeline mínimo e painel reproduzível de demanda

**Fase:** 1 — Sistema de baseline, dicionário e pipeline mínimo  
**Status:** planejada  
**Dono:** direção/comercial para taxonomia e aceite; marketing e grupo piloto de gerentes para operação; consultor para revisão  
**Origem no escopo:** C-03 mínimo, C-04 mínimo, C-05, RQ-002, RQ-003, RQ-004, RQ-008, RQ-010, DC-002, DC-004 e AC-004  
**Degrau da solução:** reuso — acrescentar somente campos, estados e visões mínimas no CRM operacional existente; se o CRM não for validado, usar a tabela controlada da SPEC-F1-001 e uma visão de painel derivada, sem integração externa.

## Contexto e decisões fechadas

- **Estado atual:** o CRM atual é operacional, mas não demonstra inteligência de pipeline; suspects permanecem em carteiras sem cobrança de ação, e leads são encaminhados ao comercial sem um pós-captura observável. Fonte: `02-Reuniao/Kickoff Call/02-Ata_reuniao.md`, linhas 48–50 e 54–62; `03-Projeto/requisitos.md`, RQ-003 e RQ-004.
- **Estado desejado:** cada registro da amostra tem origem, estado único, responsável, próxima ação e prazo ou motivo terminal; o painel reproduz as contagens da tabela e permite filtrar inbound/outbound, período, canal, campanha, serviço, responsável e origem.
- **Decisões já fechadas:** os funis inbound e outbound não são misturados; os estados mínimos são `suspect`, `prospect`, `lead qualificado`, `oportunidade`, `proposta`, `vaga aberta`, `ganho`, `perdido`, `sem timing` e `desqualificado`; vaga aberta não é fechamento; nenhum contato externo é automatizado nesta fase.
- **Bloqueios:** nome/schema/acesso do CRM não foram demonstrados. A taxonomia e os prazos podem ser aceitos pelo cliente ou permanecer bloqueados com motivo e dono; sem definição de lead qualificado, nenhuma transição para `lead qualificado` ou KPI de qualificação é válida.

## Resultado observável

Ao aceitar esta SPEC, a equipe demonstra uma visão mínima de CRM/pipeline e painel com:

1. um caso inbound e um caso outbound, usando os fixtures da SPEC-F1-001 ou dados reais autorizados;
2. estado único por registro, critérios de entrada/saída e motivo nos estados terminais;
3. dono, próxima ação e prazo para todo registro não terminal;
4. filtro e contagem por tipo de origem, período, canal, campanha, serviço, responsável e origem;
5. uma jornada de captura → qualificação possível → próxima ação → oportunidade ou encerramento, sem interpretação adicional.

## Limites e dependências

- **Inclui:** pipeline mínimo da Fase 1; estados e transições; campos de ação e evidência; visão de baseline; filtros mínimos; demonstração com uma amostra inbound/outbound; registro de bloqueios e recuperação manual.
- **Fora de escopo:** campanha ou publicação; integração Meta; automação de follow-up; enriquecimento externo; scraping; substituição de CRM/ERP/ATS; dashboard completo de performance; sinais do DHO; proposta, vaga ou fechamento reais como promessa desta fase.
- **Entradas e pré-condições:** SPEC-F1-001 aceita ou com bloqueio explícito; dicionário disponível; amostra autorizada; direção/comercial valida taxonomia ou registra pendência; dono do grupo piloto definido.
- **Saídas/artefatos:** configuração mínima no CRM aprovado ou tabela/painel de fallback; `03-Projeto/02-Plano_de_acao/01.Fase_1/02-Evidencias/pipeline-f1.md`; `03-Projeto/02-Plano_de_acao/01.Fase_1/02-Evidencias/painel-baseline-f1.md`; log de transições e exceções.
- **Dependências e responsáveis:** marketing fornece origem/campanha; comercial classifica e age; direção aprova estados/prazos e capacidade; operação devolve resultado quando houver; consultor valida a primeira demonstração.
- **Atores e permissões mínimas:** marketing cria/atualiza origem e campanha; comercial e gerentes atualizam estado, dono, próxima ação, prazo e resultado; direção lê e aprova; consultor lê e revisa; acesso por papel, sem dados sensíveis do DHO.
- **Superfícies/arquivos/configurações afetadas:** campos/visões não destrutivos no CRM validado ou a tabela/painel de fallback; nenhum conector, disparo, permissão global ou exclusão de histórico.
- **Risco e plano B:** classificação inconsistente, registro sem ação e pipeline inflado. Usar critérios escritos, rejeitar transição sem evidência e devolver para revisão; sem CRM validado, operar a amostra no fallback manual até a decisão do cliente.
- **Rollback ou reversão:** pausar a visão/piloto; preservar tabela, log e evidências; remover somente campos/visões de teste; devolver registros ao estado anterior quando a mudança não tiver evidência de aceite; não apagar histórico.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Tabela da SPEC-F1-001 → pipeline | Dicionário e lote aceito da Fase 1 | `record_id`, origem, canal, campanha, empresa, contato/ref, serviço, estado, responsável, próxima ação, prazo, resultado, evidência, qualidade | Escrita restrita aos papéis aprovados | Atualização idempotente por `record_id`; não duplicar linha em reprocessamento | Rejeitar mudança sem evidência mínima e registrar em log |
| Pipeline → painel de baseline | Mesma tabela/pipeline; sem cálculo independente | Contagem por período, tipo de origem, canal, campanha, serviço, responsável e origem; valores desconhecidos separados | Leitura para direção, consultor e grupo piloto | Recalcular a partir da fonte; não manter cópia divergente | Se filtro não tiver dado, mostrar zero somente quando a consulta for válida; mostrar `desconhecido` quando a origem faltar |
| Pipeline → handoff manual | Registro aceito pelo comercial/operação | Dono, próxima ação, prazo, canal permitido, resultado e evidência | Ação externa somente por pessoa autorizada | Não repetir handoff sem registro de tentativa; retry manual com novo evento | Falta de aceite ou canal indisponível mantém o estado atual, registra pendência e escala ao dono definido |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F1-006 — Estado único | Registro está ativo | Manter exatamente um estado atual e log de transição | Registro sem evidência suficiente mantém o estado anterior e recebe `qualidade=pendente de classificação`; não contar como oportunidade | C-03, RQ-003 |
| RN-F1-007 — Entrada/saída verificável | Transição solicitada | Exigir evidência mínima e atualizar o estado somente após validação | Sem evidência, manter estado anterior e abrir pendência | RQ-003 |
| RN-F1-008 — Ação obrigatória | Registro não terminal | Exigir dono, próxima ação e prazo; exibir no painel quando faltar um deles | Se não houver ação possível, escolher estado terminal com motivo aprovado | C-05, RQ-004 |
| RN-F1-009 — Terminal explicado | Registro encerrado | Usar `ganho`, `perdido`, `sem timing` ou `desqualificado` com motivo e evidência | Sem motivo, não aceitar o encerramento | C-03, RQ-003 |
| RN-F1-010 — Vaga não é fechamento | Estado `vaga aberta` | Contar como demanda aberta e manter resultado posterior separado | `ganho` exige evidência de decisão/fechamento definida pelo cliente | RQ-008 |
| RN-F1-011 — Qualificação condicionada | Gate de lead qualificado bloqueado | Não avançar para `lead qualificado`; mostrar pendência | Direção/consultor aprova definição em registro posterior | RQ-001, RQ-003 |
| RN-F1-012 — Sem ação externa automática | Qualquer mudança que abordaria cliente/contato | Exigir aprovação humana imediatamente anterior e registro da ação | Esta SPEC não autoriza disparo, publicação ou abordagem | DC-006, RQ-004, RQ-009 |

## Fluxo e regras

1. Carregar somente registros aceitos pela SPEC-F1-001.
2. Classificar novo registro como `suspect` ou `prospect` conforme a evidência disponível; sem evidência suficiente, manter pendência de classificação.
3. Aplicar a definição de lead qualificado somente se o gate estiver aprovado.
4. Avançar para `oportunidade` apenas com necessidade, empresa/contato, serviço ou contexto permitido, dono e próxima ação.
5. Avançar para `proposta` ou `vaga aberta` somente com evidência recebida do comercial/cliente; não inferir a partir de conversa ou clique.
6. Encerrar em estado terminal somente com motivo e evidência; registrar follow-up quando o estado for `sem timing`.
7. Recalcular o painel a partir do pipeline, aplicar filtros mínimos e comparar com a tabela de origem.
8. Demonstrar um caso inbound e um outbound, incluindo erro ou bloqueio, antes de aceitar a SPEC.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | `FIX-IN-001` e `FIX-OUT-001` têm origem, responsável e próximo passo | Painel mostra os dois tipos separados; registros têm estado e ação; contagens batem com a fonte | Divergência abre log e bloqueia o aceite até reconciliação |
| Limite | Registro sem origem, sem responsável ou sem prazo | Registro aparece como `desconhecido`/pendente e não é contado como oportunidade válida | Dono recebe pendência; se não houver ação, estado terminal com motivo aprovado |
| Falha | Comercial não aceita o handoff ou o canal autorizado está indisponível | Registro é preservado, tentativa é registrada e o estado anterior permanece com pendência visível | Escalar para o dono definido; não repetir contato automaticamente |
| Transição inválida | Solicitação para marcar `ganho` sem evidência de fechamento ou `lead qualificado` com gate bloqueado | Mudança recusada; estado anterior permanece; motivo aparece no log | Consultor/direção revisam o critério, sem corrigir silenciosamente |
| Rollback | Visão ou campo de teste causa contagem divergente | Pausar o piloto, conservar evidências e retornar à última visão aceita | Reconciliar a fonte antes de reabrir a demonstração |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** esta SPEC; SPEC-F1-001; `03-Projeto/02-Escopo-Definitivo.md` seção Fase 1; `03-Projeto/requisitos.md` RQ-003, RQ-004, RQ-008 e RQ-010; `02-Reuniao/Kickoff Call/02-Ata_reuniao.md` linhas 48–50 e 54–62.
2. **Alterar somente:** campos/visões não destrutivos do CRM validado ou o fallback manual e os dois artefatos de evidência desta SPEC.
3. **Não alterar:** taxonomia fora dos estados listados; permissões globais; registros de produção fora da amostra; campanhas; integrações; dados do DHO; qualquer ação externa sem aprovação.
4. **Executar nesta ordem:** validar gate da SPEC-F1-001 → confirmar taxonomia/prazos → carregar fixtures → testar transições → gerar painel → testar filtros e reconciliação → demonstrar erro/rollback → pedir aceite.
5. **Parar e pedir validação quando:** não houver acesso/schema; a definição de lead qualificado estiver ausente; alguém pedir um novo estado, SLA ou integração; o registro tiver dado sensível; houver tentativa de publicação, abordagem, disparo ou alteração irreversível.
6. **Estado válido ao parar:** fonte e log preservados; cada registro mantém estado anterior em caso de erro; painel identifica bloqueios; nenhuma ação externa foi executada por inferência.

## Checklist de execução

- [ ] Gate da SPEC-F1-001 e superfície de registro foram conferidos.
- [ ] Taxonomia, critérios de entrada/saída, motivos terminais e prazos foram aprovados ou bloqueados com dono e próximo passo.
- [ ] Existe uma amostra inbound e uma outbound com origem, estado, responsável e próxima ação.
- [ ] Painel reproduz as contagens da fonte e permite os seis filtros mínimos definidos.
- [ ] Foram exercitados estado inválido, falta de aceite/canal, duplicidade e rollback sem ação externa.

## Critérios de aceite

- [ ] **CA-1-06:** cada registro da amostra tem um estado único; uma transição inválida é recusada e deixa evidência do motivo.
- [ ] **CA-1-07:** cada registro não terminal tem dono, próxima ação e prazo; ausência de qualquer campo aparece como pendência visível e não como sucesso.
- [ ] **CA-1-08:** um caso inbound e um outbound percorrem captura → classificação possível → próxima ação → oportunidade ou encerramento, com a origem preservada.
- [ ] **CA-1-09:** o painel reproduz a fonte e filtra por período, tipo de origem, canal, campanha, serviço, responsável e origem, separando `desconhecido`.
- [ ] **CA-1-10:** vaga aberta não é contada como ganho; terminal sem motivo, lead qualificado sem gate e handoff sem aceite não passam.
- [ ] **CA-1-11:** rollback da visão/campo de teste preserva a fonte e retorna o piloto à última configuração aceita sem apagar histórico.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | Inserir `FIX-IN-001` sem dono e tentar avançar para `oportunidade`; inserir `FIX-OUT-001` como `ganho` sem evidência | Executar as transições na superfície aprovada e atualizar o painel | Mudanças são recusadas; pendências aparecem; contagem de oportunidades/ganhos não infla | Log de transições recusadas e captura do painel |
| GREEN | Corrigir os fixtures com dono, próxima ação, prazo e evidência mínima; manter `lead qualificado` bloqueado se o gate não estiver aprovado | Executar captura → `suspect`/`prospect` → próxima ação → `oportunidade` ou `sem timing` | Passa CA-1-06 a CA-1-10; painel bate com a fonte e preserva inbound/outbound | `pipeline-f1.md`, `painel-baseline-f1.md`, log e demonstração do grupo piloto |
| REFACTOR/REGRESSÃO | Aplicar filtros, reprocessar o mesmo `record_id`, simular canal indisponível e reverter uma visão de teste | Recalcular o painel e executar rollback controlado | Sem duplicidade, contagens estáveis, erro visível, fonte intacta e configuração anterior restaurada | Comparação antes/depois e log de rollback |

**Dados/fixtures:** usar `FIX-IN-001`, `FIX-OUT-001`, `FIX-UNK-001` e `FIX-DUP-001` da SPEC-F1-001; acrescentar estado terminal com motivo sintético e um handoff sem aceite. Dados reais só entram com autorização e referência de origem.
**Caminhos de erro obrigatórios:** estado inválido; falta de dono/próxima ação/prazo; origem desconhecida; lead qualificado sem gate; terminal sem motivo; handoff sem aceite; canal indisponível; reprocessamento duplicado; rollback.
**Evidência exigida:** artefatos do pipeline e painel, fixture usado, log de transições, prova dos filtros, rejeições, rollback e aceite humano da demonstração.

## Handoff e operação

- **Como demonstrar:** selecionar um caso inbound e um outbound, mostrar o estado, dono, próxima ação e filtro de origem; tentar uma transição inválida; mostrar o motivo da rejeição e o retorno ao painel.
- **Como operar depois:** marketing registra origem/campanha; comercial atualiza classificação e ação; gerentes devolvem resultado; direção revisa gargalos e capacidade; consultor valida a primeira demonstração.
- **Como monitorar:** revisão periódica de registros sem próxima ação, estados parados, origem desconhecida, rejeições e divergência entre fonte e painel.
- **Pendência conhecida:** nome/schema/acesso do CRM, prazos finais e definição de lead qualificado devem ser aprovados ou permanecer explicitamente bloqueados antes de ampliar a amostra.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F1-T04 | Configurar taxonomia e regras do pipeline | Gerente comercial piloto | SPEC-F1-002 | CA-1-06, CA-1-07, CA-1-10 | RED de transição inválida + GREEN de estado/ação | configuração + log de transição | F1-T01; superfície e taxonomia validadas | planejada |
| F1-T05 | Executar jornada e handoff controlado | Gerente comercial piloto | SPEC-F1-002 | CA-1-08, CA-1-10 | GREEN com inbound/outbound e falha de canal | pipeline + logs + demonstração | F1-T02 e F1-T04; grupo piloto | planejada |
| F1-T06 | Reconciliar painel e rollback | Consultor Adapta | SPEC-F1-002 | CA-1-09, CA-1-11 | REFACTOR/REGRESSÃO com filtros, reprocessamento e rollback | painel + comparação + log de rollback | F1-T03 e F1-T05 | planejada |

## Emendas

<!-- Append-only (D19): mudanças aprovadas depois da geração. A história não é reescrita. -->

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
