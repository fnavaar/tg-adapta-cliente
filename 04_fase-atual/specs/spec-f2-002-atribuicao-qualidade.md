# SPEC-F2-002 — Atribuição de origem e qualidade do experimento

**Fase:** 2  
**Status:** liberada para execução — F2-T03 e F2-T04 concluídas e validadas (2026-09-14 / 2026-09-17)  
**Dono:** marketing registra origem/custo; comercial devolve qualidade e oportunidade  
**Origem no escopo:** Fase 2, C-01, C-04, DC-004, G-001, G-009  
**Degrau da solução:** reuso da collection/painel de demandas da Fase 1 com campos mínimos de experimento — não agrega automaticamente fontes nem cria conector.

## Contexto e decisões fechadas

- **Estado atual:** F1 declarou filtros por origem, canal, campanha e estado. A estratégia de identidade entre múltiplas fontes (`record_id` global ou composto) está pendente.
- **Estado desejado:** o resultado de um experimento é atribuído a uma origem única e ligado aos registros do pipeline sem misturar inbound e outbound ou tratar dados ausentes como zero.
- **Decisões já fechadas:** volume e qualidade são métricas separadas; dados ausentes são `desconhecido`; Meta pode permanecer manual.
- **Bloqueios:** a agregação/integração de duas fontes técnicas fica bloqueada até decisão de identidade e prova de campos/formato.

## Resultado observável

Para cada `EXP-F2-###`, uma visão/relatório reproduz contagens por tipo, origem, canal e versão, distinguindo captura, lead qualificado, oportunidade e motivo de perda quando disponíveis; cada linha pode ser rastreada ao registro F1 ou é marcada como não vinculada/desconhecida.

## Limites e dependências

- **Inclui:** contrato de atribuição, ligação manual por `experimento_id`, métricas de volume/qualidade e reconciliação com a fonte disponível.
- **Fora de escopo:** deduplicação multi-fonte automática, cobrança/custo calculado sem fonte, atribuição por clique isolado, dados DHO e integração não aprovada.
- **Entradas e pré-condições:** SPEC-F2-001 aceita; origem/canal/versão registrados; fonte do resultado identificada; decisão de chave caso entre segunda fonte técnica.
- **Saídas/artefatos:** relatório de atribuição, lista de desconhecidos/não vinculados e registro de reconciliação.
- **Atores e permissões mínimas:** marketing edita dados de campanha; comercial devolve qualidade; consulta ampla não expõe dados pessoais desnecessários.
- **Superfícies afetadas:** collection/painel da F1 ou fallback manual; sem alterar hooks/migrations não previstos.
- **Risco e plano B:** sem acesso à fonte ou ID estável, importar/registrar manualmente e marcar lacuna, sem deduplicar.
- **Rollback:** remover somente a visão/ligação criada e preservar o registro de origem e a decisão de qualidade.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| briefing → demanda F1 | briefing F2-001 e registro operacional | `experimento_id`, `tipo_origem`, canal, campanha, criativo_versao, `record_id`, estado, qualidade | marketing/comercial autorizados | mesma chave só atualiza vínculo documentado | ausência de chave vira `não_vinculado` |
| fonte de métricas → relatório | export/painel autorizado ou lançamento manual | período, unidade, impressão, clique, custo, captura | leitura autorizada; Meta condicional | importação manual identifica lote/data | fonte indisponível mantém campos `desconhecido` |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F2-004 | origem/canal não comprovados | classificar `desconhecido`; não somar a canal conhecido | nenhuma | C-01 |
| RN-F2-005 | registro tem `experimento_id` e chave F1 válida | incluir na atribuição daquele experimento | chave ausente = não vinculado | Fase 2 |
| RN-F2-006 | há múltiplas fontes técnicas | não deduplicar/agregar até chave aprovada | fallback manual por lote | pendência F1/STATUS |
| RN-F2-007 | só há clique/abandono | exibir como atividade, não como qualidade/sucesso | nenhuma | Fase 2 regras |

## Fluxo e regras

1. Marketing fornece resultado por período para o ID do experimento.
2. O sistema/tabela valida origem, canal e vínculo com a demanda F1.
3. Comercial devolve estado de qualidade disponível sem reclassificar por inferência.
4. O relatório compara IDs e contagens contra a fonte e lista lacunas.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | dois registros vinculados, um inbound e um outbound | métricas separadas e rastreáveis | seguir SPEC-F2-003 |
| Limite | registro sem origem ou chave | visível como desconhecido/não vinculado | owner completa ou mantém pendência |
| Falha | importação repete chave de fonte | não criar segunda contagem | rejeitar/revisar lote e preservar origem |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** F1-T06 e sua pendência de identidade; escopo §5 C-01/C-04, §7 F2 e G-009.
2. **Alterar somente:** campos/vista de atribuição autorizados e dados sintéticos.
3. **Não alterar:** regras de estágio/handoff F1, fonte original, Meta, custos/valores sem origem, dados DHO.
4. **Executar nesta ordem:** aprovar contrato de chave → criar fixtures → reconciliar IDs → demonstrar relatório.
5. **Parar e pedir validação quando:** uma segunda fonte técnica, chave nova, campo pessoal ou divergência de contagem for necessária.
6. **Estado válido ao parar:** registros F1 preservados e relatório explicita a lacuna.

## Checklist de execução

- [ ] Contrato de origem única e `desconhecido` demonstrado.
- [ ] Métricas de atividade e qualidade separadas.
- [ ] Reconciliação compara contagem e IDs, não só totais.
- [ ] Multi-fonte sem chave aprovada está bloqueada.

## Critérios de aceite

- [ ] **CA-2-04:** um caso inbound e um outbound do mesmo período aparecem separados por origem/canal/versão e apontam ao experimento.
- [ ] **CA-2-05:** um registro sem origem ou sem chave aparece como desconhecido/não vinculado e não infla conversão.
- [ ] **CA-2-06:** o relatório reconcilia quantidade e identidade com a fonte declarada, ou registra a divergência/lacuna com dono.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | importar `ATR-F2-RED-001` sem origem e repetir `record_id` | registrar via superfície autorizada | desconhecido e duplicata não aumentam métrica | captura/export + log |
| GREEN | criar `ATR-F2-IN-001` e `ATR-F2-OUT-001` ligados a `EXP-F2-*` | gerar relatório filtrado | dois tipos separados, IDs coincidentes | relatório e comparação fonte |
| REFACTOR/REGRESSÃO | reexecutar o mesmo lote | reconciliar IDs/contagens | sem duplicação; F1 preservada | comparação antes/depois |

**Dados/fixtures:** `ATR-F2-IN-001`, `ATR-F2-OUT-001`, `ATR-F2-UNK-001`, sem contatos reais.  
**Caminhos de erro obrigatórios:** origem ausente, chave repetida, fonte indisponível, divergência de contagem.  
**Evidência exigida:** export/consulta equivalente, lista de IDs, relatório e aceite do owner.

## Handoff e operação

- **Como demonstrar:** filtrar o mesmo período para inbound/outbound e confrontar os IDs com a fonte.
- **Como operar depois:** marketing atualiza resultado por experimento; comercial devolve qualidade; consultor revisa a primeira reconciliação.
- **Como monitorar:** taxa de não vinculados/desconhecidos e divergências de contagem.
- **Pendência conhecida:** definição de chave multi-fonte antes de qualquer integração agregada.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F2-T03 | Configurar/registrar contrato de atribuição de fonte única e fixtures de qualidade, sem agregação multi-fonte. | Marketing + comercial | F2-002 | RN-F2-004, RN-F2-005, RN-F2-006 | Dados e integrações; Fluxo e regras; Checklist | Mapa de campos/chave, fixtures e registro de pendência. | F2-T02 aceita; fonte única declarada; dono da qualidade definido. | Concluída e validada em 2026-09-14 |
| F2-T04 | Provar atribuição, desconhecido, duplicidade e reconciliação por IDs contra a fonte declarada. | Marketing + comercial | F2-002 | CA-2-04, CA-2-05, CA-2-06 | Critérios de aceite; TDD da SPEC | Relatório, lista de IDs, comparação fonte×relatório e lista de lacunas com dono. | F2-T03 aceita por teste humano; fonte acessível ou lacuna formal aceita. | Concluída e validada em 2026-09-17 |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
| | | | |