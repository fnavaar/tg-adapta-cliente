# SPEC-F3-002 — Dashboard operacional de conversão e gargalos

**Fase:** 3
**Status:** planejada
**Dono:** direção consome; marketing/comercial alimentam; consultor valida a primeira leitura
**Origem no escopo:** Fase 3; C-04; DC-002; DC-004; RQ-001/RQ-006/RQ-007; G-001; G-005
**Degrau da solução:** reuso — evoluir o painel reproduzível da F1 para o dashboard operacional da F3 sobre o pipeline integrado; núcleo de reconciliação compartilhado para contagens; sem fonte nova.

## Contexto e decisões fechadas

- **Estado atual:** a F1 entregou painel de baseline reproduzível com filtros por período/tipo/canal/campanha/serviço/responsável/origem e marcação de lacunas (SPEC-F1-002); a F2 acrescentou volume×qualidade separados e decisão de experimento. Não existe visão de gargalo entre captura→abordagem→proposta→vaga, nem visão única inbound×outbound na camada de CRM/pipeline.
- **Estado desejado:** o dashboard mostra onde a demanda parou (por estado, dono e prazo), tempos entre etapas, retorno de proposta/vaga com origem e motivo, e permite identificar gargalo entre captura, abordagem, proposta e vaga.
- **Decisões já fechadas:** contagens sempre recalculadas da fonte via núcleo compartilhado (EV-05); valores desconhecidos aparecem como `desconhecido`; atividade (cliques/volume) nunca é apresentada como qualidade; adoção dos gerentes é medida separadamente e baixa adesão não é sucesso (G-005).
- **Bloqueios:** B3-MET-01 — sem meta/fórmula/período aprovados (G-001) e sem definição de lead qualificado, o dashboard exibe distribuição, tempos e gargalos, mas NENHUM KPI de resultado (conversão contra alvo, % de meta) pode ser declarado; a exibição de KPI contra alvo é bloqueada até a direção registrar alvo/fórmula/período.

## Resultado observável

1. Visão única inbound×outbound por estado do pipeline com contagem, dono e idade do registro.
2. Gargalo identificável entre captura, abordagem, proposta e vaga: contagem por estado + tempo mediano entre transições + registros parados além do SLA.
3. Retorno de proposta/vaga com origem e motivo visível (consome CA-3-02).
4. Filtros herdados da F1 (período, tipo, canal, campanha, serviço, responsável, origem) + filtro por estado e por pendência.
5. Bloco de pendências de governança/métrica visível (B3-MET-01, B3-ID-01) — lacunas aparecem como lacunas.

## Limites e dependências

- **Inclui:** visões de pipeline/gargalo/tempos/retorno; filtros; exportação/captura para reunião de ciclo; bloco de pendências.
- **Fora de escopo:** KPI contra alvo (B3-MET-01); dados de custo por campanha além do já autorizado na F2; integração externa nova; scraping; substituição de CRM/ERP/ATS; automação de contato.
- **Entradas e pré-condições:** SPEC-F3-001 aceita (pipeline integrado com log de transições); núcleo de reconciliação compartilhado; amostra/fixtures.
- **Saídas/artefatos:** dashboard na superfície existente; evidência `dashboard-f3.md`; capturas da leitura de gargalo.
- **Dependências e responsáveis:** comercial/marketing mantêm dados; direção lê e valida a primeira leitura; consultor revisa.
- **Atores e permissões mínimas:** leitura por papel; direção vê tudo; gerentes veem seus registros; sem dado sensível do DHO.
- **Superfícies/arquivos/configurações afetadas:** superfície de painel (extensão); nenhuma coleção nova além do que a F3-001 criar; sem conector.
- **Risco e plano B:** dado insuficiente na amostra → exibir `desconhecido`/vazio com nota, não inventar; adoção baixa → medir uso separadamente e reportar, não declarar sucesso.
- **Rollback ou reversão:** desativar visões novas, preservar painel F1/F2 e dados; nada é apagado.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Pipeline integrado (F3-001) → dashboard | `demandas` + log de transições | contagem por estado/tipo/origem; tempo entre transições; parados > SLA; retorno com motivo | Leitura por papel | Recalcular da fonte (núcleo compartilhado); sem cópia materializada divergente | Divergência → pendência com dono (RN-F3-006) |
| Campanha/experimento F2 → contexto de origem | Atribuição F2-002 | campanha/experimento_id, canal, tipo inbound/outbound | Leitura | Ligação por identidade da fonte (B3-ID-01) | Origem ausente → `desconhecido` |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-007 — Gargalo visível | Qualquer leitura | Exibir contagem por estado + tempo mediano entre etapas + parados > SLA | Sem SLA definido para a etapa → exibir sem SLA e registrar pendência | §Fase 3 checklist |
| RN-F3-008 — Atividade ≠ qualidade | Métricas de volume (cliques, impressões) | Exibir sempre separadas de conversão/qualidade | — | F2, §1 escopo |
| RN-F3-009 — Sem KPI sem alvo | G-001 aberto | Bloquear exibição de KPI contra alvo; exibir pendência B3-MET-01 | Direção aprovar alvo/fórmula/período → nova versão libera o bloco | G-001, EV-06 |
| RN-F3-010 — Desconhecido visível | Origem/dado ausente | Exibir `desconhecido`; nunca zero falso nem inferência | Consulta válida sem registros → zero legítimo | C-01, RN-F1-005 |

## Fluxo e regras

1. Consumir somente o pipeline integrado e a atribuição existentes.
2. Renderizar visões por estado, gargalo, tempos e retorno com filtros herdados.
3. Exibir bloco de pendências (métrica/identidade) com dono.
4. Exportar/capturar a leitura para a reunião de ciclo.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | amostra com jornada completa | gargalo identificável entre as 4 etapas; retorno com origem/motivo | divergência → pendência |
| Limite | amostra pequena/origem ausente | `desconhecido`/nota; sem invenção | registrar lacuna |
| Falha | fonte indisponível/contagem divergente | dashboard não exibe número sem fonte; pendência com dono | recalcular da fonte |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** SPEC-F1-002 (painel/filtros), SPEC-F3-001, escopo §5 C-04 e §7 Fase 3; núcleo `reconciliation/core.ts`.
2. **Alterar somente:** superfície de dashboard/visões; consultas de leitura.
3. **Não alterar:** pipeline/estados (F3-001); atribuição F2; conectores; permissões; KPI bloqueado (RN-F3-009).
4. **Executar nesta ordem:** visão por estado → gargalo/tempos → retorno → pendências → captura da leitura.
5. **Parar e pedir validação quando:** pedirem KPI contra alvo sem G-001 fechado; pedirem fonte externa nova; contagem não reproduzir a fonte.
6. **Estado válido ao parar:** painel F1/F2 intacto; visões novas desativáveis; capturas salvas.

## Checklist de execução

- [ ] Visão única inbound×outbound por estado com dono e idade.
- [ ] Gargalo entre captura/abordagem/proposta/vaga identificável (contagem + tempo + parados).
- [ ] Retorno de proposta/vaga com origem e motivo visível.
- [ ] Filtros herdados funcionando; `desconhecido` visível; KPI contra alvo bloqueado com pendência.
- [ ] Leitura exportável; bateria humana da leitura registrada.

## Critérios de aceite

- [ ] **CA-3-04:** o dashboard identifica, a partir da amostra, onde a demanda parou (estado, dono, prazo) e o gargalo entre captura, abordagem, proposta e vaga, com contagens reproduzíveis da fonte.
- [ ] **CA-3-05:** a leitura separa volume de qualidade, exibe `desconhecido` para dado ausente e mantém bloqueado qualquer KPI contra alvo enquanto G-001 não for aprovado (pendência visível com dono).

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | KPI contra alvo sem G-001; contagem divergente da fonte; origem ausente renderizada como zero | consultar dashboard | bloqueio/pendência; recusa de número sem fonte | captura/log |
| GREEN | amostra com jornada completa | ler gargalo + retorno | CA-3-04 demonstrável; contagens = fonte | captura + comparação |
| REFACTOR/REGRESSÃO | reprocessar lote; refiltrar; verificar painel F1/F2 intacto | replay + filtros | sem regressão; contagens idempotentes | comparação + captura |

**Dados/fixtures:** mesmos fixtures/amostra da F3-001; sem dado pessoal.
**Caminhos de erro obrigatórios:** fonte indisponível; contagem divergente; filtro sem dado; KPI sem alvo.
**Evidência exigida:** capturas da leitura, comparação fonte×dashboard, bateria humana (EV-08).

## Handoff e operação

- **Como demonstrar:** abrir o dashboard, apontar o gargalo e o retorno com origem; mostrar o bloco de pendências.
- **Como operar depois:** direção lê semanalmente; comercial mantém estados; pendências com dono.
- **Como monitorar:** divergência fonte×painel; registros sem estado/dono; adoção (separada).
- **Pendência conhecida:** B3-MET-01 governa o bloqueio de KPI; liberação exige decisão da direção.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T03 | Materializar visões de gargalo, tempos e retorno no dashboard com massa sintética | Marketing/comercial | F3-002 | CA-3-04 | Dados e integrações; Fluxo e regras; Checklist | Captura/export das visões com contagens da fonte | F3-T01 aceita | ☐ |
| F3-T04 | Provar leitura de gargalo, bloqueio de KPI sem alvo e reprodução das contagens | Direção + consultor | F3-002 | CA-3-04, CA-3-05 | Critérios de aceite; TDD da SPEC | Bateria humana da leitura + comparação fonte×painel | F3-T03 aceita por teste humano | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
