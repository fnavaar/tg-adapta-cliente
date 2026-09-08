# SPEC-F1-001 — Dicionário de demanda e baseline reproduzível

**Fase:** 1 — Sistema de baseline, dicionário e pipeline mínimo  
**Status:** planejada  
**Dono:** direção/consultor para decisões; marketing, comercial e operação para fornecimento dos dados  
**Origem no escopo:** C-01, RQ-001, RQ-002, RQ-009, DC-001, DC-004 e G-001  
**Degrau da solução:** reuso — usar o CRM operacional existente como fonte quando seus campos e permissões forem demonstrados; manter uma tabela manual controlada como fallback reversível, sem substituir CRM/ERP.

## Contexto e decisões fechadas

- **Estado atual:** o CRM é descrito como operacional, sem inteligência de pipeline; campanhas, contatos, contas e vagas estão distribuídos em fontes parciais. O kickoff relata 37 vagas abertas e aproximadamente 1–3 leads por mês, mas não há série histórica consolidada nem definição única de período, lead qualificado ou alvo. Fonte: `02-Reuniao/Kickoff Call/02-Ata_reuniao.md`, linhas 39–50; `03-Projeto/requisitos.md`, RQ-001.
- **Estado desejado:** existe um dicionário aprovado, uma tabela de registros com origem e qualidade explícitas e um relatório de baseline que outra pessoa consegue reproduzir sem completar lacunas por inferência.
- **Decisões já fechadas:** inbound e outbound permanecem separados; 37 é valor relatado, não meta; dados desconhecidos permanecem `desconhecido`; nenhuma integração externa é presumida; o fallback manual é permitido; sinais sensíveis do DHO não entram nesta fase.
- **Bloqueios:** o nome, acesso e schema do CRM não foram demonstrados nos artefatos disponíveis. A execução deve parar para validar esses itens ou usar o fallback manual definido nesta SPEC. Alvo, fórmula, período e definição de lead qualificado podem permanecer como gate impeditivo, desde que o bloqueio seja registrado em `gate-alvo-f1.md`.

## Resultado observável

Ao aceitar esta SPEC, a equipe demonstra três artefatos da Fase 1:

1. `03-Projeto/02-Plano_de_acao/01.Fase_1/02-Evidencias/dicionario-demanda-f1.csv`, ou a mesma estrutura no CRM aprovado, com campos, tipos, valores permitidos, obrigatoriedade, fonte e regra para desconhecido.
2. `03-Projeto/02-Plano_de_acao/01.Fase_1/02-Evidencias/baseline-demanda-f1.md`, com valores, período, fórmula, fonte, qualidade e lacunas.
3. `03-Projeto/02-Plano_de_acao/01.Fase_1/02-Evidencias/gate-alvo-f1.md`, com decisão `APROVADO` ou `BLOQUEADO` para alvo, fórmula, período e lead qualificado; o executor não escolhe o alvo.

## Limites e dependências

- **Inclui:** dicionário mínimo de demanda; normalização de inbound/outbound; registro de origem e qualidade; baseline relatado; decisão ou bloqueio explícito para alvo/fórmula/período; amostra sintética para prova.
- **Fora de escopo:** escolher meta em nome da direção; prometer 60–70 vagas; integração Meta ou outra API; disparo; scraping; dados sensíveis do DHO; substituição de CRM/ERP/ATS; dashboard completo de performance.
- **Entradas e pré-condições:** aprovação do check de escopo; exportação, amostra ou transcrição autorizada das fontes; responsável de marketing/comercial disponível; definição da superfície de registro ou autorização do fallback manual.
- **Saídas/artefatos:** os três artefatos listados em Resultado observável; log de rejeições/correções; referência às fontes usadas.
- **Dependências e responsáveis:** direção/consultor aprovam decisões; marketing fornece campanhas e origem; comercial fornece classificação e responsável; operação fornece dados de vagas; cliente fornece acesso ou confirma o fallback.
- **Atores e permissões mínimas:** direção leitura e aprovação; consultor leitura e revisão; marketing/comercial/operacao escrita somente nos campos de sua responsabilidade; nenhum acesso a sinal sensível do DHO nesta SPEC.
- **Superfícies/arquivos/configurações afetadas:** CRM operacional somente em campos não destrutivos, se acesso e schema forem confirmados; ou a tabela manual controlada e os três arquivos de evidência listados; nenhum conector externo.
- **Risco e plano B:** fonte incompleta, duplicidade ou origem ausente pode distorcer o baseline. Marcar qualidade e `desconhecido`; não descartar registro. Se o CRM não puder ser validado, usar o fallback manual e registrar a limitação.
- **Rollback ou reversão:** preservar exports originais; remover somente campos de teste criados na superfície aprovada; não apagar histórico; arquivar a tabela de prova e marcar o baseline como inválido se a fonte for revogada.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| CRM operacional ou exportação autorizada | Sistema atual demonstrado pelo cliente | `record_id`, empresa, contato/ref, origem, canal, campanha, oferta/serviço, segmento, data, responsável, estado, próxima ação, prazo, resultado, evidência, qualidade | Acesso concedido pelo cliente; somente campos autorizados | Importação manual idempotente por `record_id`; sem retry automático | Rejeitar linha sem identificação mínima, registrar motivo e manter a fonte intacta |
| Campanhas, contatos, contas e vagas informados pelo cliente | Exportação ou documento de origem entregue | Valor, unidade, período, fonte e referência do registro | Leitura autorizada; não consultar plataforma externa por inferência | Não aplicável a documento; não duplicar fonte | Marcar ausência como `desconhecido` e registrar a lacuna |
| `02-Reuniao/Kickoff Call/02-Ata_reuniao.md` e `03-Projeto/02-Escopo-Definitivo.md` | Fontes de decisão do plano | 37 vagas relatadas; 1–3 leads/mês relatados; regra de não inferência | Leitura local | Não aplicável | Informar que os valores não formam série histórica nem meta |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F1-001 — Origem separada | Registro inbound ou outbound | Preencher `tipo_origem` com um único valor e manter canal/campanha separados | Se não houver origem, usar `desconhecido` e abrir pendência | C-01, RQ-002 |
| RN-F1-002 — Lacuna visível | Campo não comprovado pela fonte | Gravar `desconhecido`, `não informado` ou `não aplicável` conforme o caso; nunca deixar vazio por decisão implícita | Campo sensível não permitido fica `restrito`, sem copiar conteúdo | C-01, RQ-009 |
| RN-F1-003 — Valores relatados não são meta | Fonte informa 37, 60–70 ou 1–3/mês sem período/fórmula aprovados | Mostrar valor, fonte e status `relatado`; não calcular alvo nem sucesso | Direção pode aprovar em `gate-alvo-f1.md` | RQ-001, G-001 |
| RN-F1-004 — Deduplificação conservadora | Existe identificador estável igual | Manter um registro canônico e registrar referências de origem | Sem identificador estável, marcar `possível duplicidade`; não mesclar automaticamente | RQ-002, RQ-009 |
| RN-F1-005 — Lead qualificado condicionado | Definição mínima ainda não aprovada | Bloquear a métrica de lead qualificado e manter registros em estado anterior | A aprovação humana libera a transição em SPEC-F1-002 | RQ-001, RQ-003 |

## Fluxo e regras

1. Ler as fontes autorizadas e registrar a referência de cada lote.
2. Confirmar a superfície: CRM demonstrado ou fallback manual controlado.
3. Criar o dicionário com tipos, valores permitidos e regra de ausência antes de importar qualquer registro.
4. Mapear a amostra, separando inbound e outbound e preservando a origem.
5. Executar a checagem de identificação, duplicidade, estado, responsável, próxima ação e evidência.
6. Calcular somente métricas cuja unidade, período, numerador e denominador estejam explícitos.
7. Gerar baseline com qualidade e lacunas; anexar o gate de alvo/fórmula/período/lead qualificado.
8. Parar para decisão humana quando o gate estiver sem aprovação; não converter bloqueio em valor estimado.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | Lote autorizado com registros inbound e outbound e fonte identificável | Dicionário preenchido; baseline separa os tipos de origem e cada valor aponta para a fonte | Registro que falhar na validação fica em rejeições com motivo e pode ser corrigido sem apagar o lote |
| Limite | 37 vagas e 1–3 leads/mês sem período ou fórmula oficial | Relatório mostra os valores como relatados e `gate-alvo-f1.md` como `BLOQUEADO`; nenhum alvo é calculado | Direção/consultor decide em registro posterior; até lá, o painel não declara sucesso |
| Falha | Acesso ao CRM não concedido ou campo não exportável | Execução para na validação e usa fallback manual somente após confirmação do cliente | Preservar fonte, registrar `CRM não validado` e não criar integração alternativa |
| Privacidade | Lote contém sinal sensível do DHO | Registro é recusado para esta SPEC e não é copiado para a tabela de demanda | Devolver ao DHO/cliente para classificação e seguir sem o dado sensível |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** `03-Projeto/02-Escopo-Definitivo.md` seção Fase 1; `03-Projeto/requisitos.md` RQ-001, RQ-002 e RQ-009; `02-Reuniao/Kickoff Call/02-Ata_reuniao.md` seções “Contexto e situação atual” e “Dores e riscos levantados”; `03-Projeto/02-Plano_de_acao/matriz-de-rastreabilidade.md` linhas da Fase 1.
2. **Alterar somente:** campos autorizados no CRM ou a tabela manual e os três artefatos de evidência desta SPEC.
3. **Não alterar:** registros de produção fora da amostra; integrações; permissões; sinais do DHO; metas; histórico original; SPECs sem emenda aprovada.
4. **Executar nesta ordem:** validar acesso → fechar dicionário → importar/mapear lote → checar qualidade → gerar baseline → registrar gate humano → anexar provas.
5. **Parar e pedir validação quando:** não houver acesso/schema do CRM; aparecer dado pessoal/sensível não autorizado; a origem não puder ser identificada; alguém pedir alvo, fórmula ou período por inferência; houver ação externa ou destrutiva.
6. **Estado válido ao parar:** fontes preservadas; lote rejeitado separado; dicionário versionado; baseline marcado `BLOQUEADO` quando faltarem decisões; nenhuma métrica inventada.

## Checklist de execução

- [ ] Superfície de registro e permissão mínima foram confirmadas.
- [ ] Dicionário contém todos os campos mínimos, valores permitidos e regra de desconhecido.
- [ ] Amostra contém pelo menos um registro inbound e um outbound, ou a ausência foi registrada como bloqueio.
- [ ] Validação de origem, duplicidade, qualidade, responsável e evidência foi executada.
- [ ] Baseline reproduzível e `gate-alvo-f1.md` foram gerados sem converter relato em meta.

## Critérios de aceite

- [ ] **CA-1-01:** uma pessoa que não criou o artefato consegue localizar a definição, tipo, fonte e regra de ausência de cada campo do dicionário.
- [ ] **CA-1-02:** a amostra demonstra inbound e outbound separados, com origem, responsável e referência de evidência; se uma origem estiver ausente, ela aparece como `desconhecido`.
- [ ] **CA-1-03:** o relatório reproduz 37 vagas como valor relatado e identifica que período, fórmula e alvo não estão demonstrados; não apresenta 60, 70 ou 50% como resultado aprovado.
- [ ] **CA-1-04:** `gate-alvo-f1.md` contém decisão humana `APROVADO` com alvo, fórmula, período e definição de lead qualificado, ou `BLOQUEADO` com dono, motivo e próximo passo; nenhuma decisão é inventada pelo executor.
- [ ] **CA-1-05:** um lote com dado ausente, possível duplicidade ou sinal sensível produz tratamento observável conforme RN-F1-002 a RN-F1-004 e não altera a fonte original.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | Tentar gerar o baseline usando somente “37 para 60–70” e “1–3 leads/mês”, sem período/fórmula | Criar um rascunho de relatório sem `gate-alvo-f1.md` e submetê-lo à revisão do consultor | Reprova CA-1-03/CA-1-04: relatório fica `BLOQUEADO` e não pode declarar alvo ou sucesso | Registro de revisão com o motivo do bloqueio |
| GREEN | Mapear fixtures `FIX-IN-001` inbound e `FIX-OUT-001` outbound, mais `FIX-UNK-001` sem origem | Preencher a tabela com o dicionário e gerar o relatório | Passa CA-1-01/CA-1-02; origem desconhecida é visível e as contagens por tipo reproduzem a tabela | `dicionario-demanda-f1.csv`, `baseline-demanda-f1.md` e captura/relatório da revisão |
| REFACTOR/REGRESSÃO | Reexecutar com `FIX-DUP-001` sem identificador estável e um registro com sinal de DHO | Rodar a checagem de qualidade e revisar o lote | Possível duplicidade fica pendente; sinal de DHO é recusado; fonte permanece intacta; passa CA-1-05 | Log de rejeições e comparação antes/depois |

**Dados/fixtures:** `FIX-IN-001` (inbound, campanha `F1-FIXTURE-IN`), `FIX-OUT-001` (outbound, campanha `F1-FIXTURE-OUT`), `FIX-UNK-001` (origem desconhecida), `FIX-DUP-001` (sem identificador estável) e um registro sintético com `sensibilidade=restrito`; todos devem ser marcados como dados de teste, sem nomes ou contatos reais.
**Caminhos de erro obrigatórios:** origem ausente; campo obrigatório ausente; possível duplicidade; acesso negado; período desconhecido; alvo não aprovado; sinal sensível do DHO.
**Evidência exigida:** três artefatos de evidência, lote/fixture usado, log de rejeições, decisão humana do gate ou bloqueio com dono e data.

## Handoff e operação

- **Como demonstrar:** abrir o dicionário, selecionar um registro inbound e um outbound, reproduzir as contagens e mostrar o gate de alvo sem preencher uma meta por inferência.
- **Como operar depois:** marketing/comercial atualizam somente os campos autorizados; direção/consultor mantêm a decisão de métrica; operação informa estados e resultados quando disponíveis.
- **Como monitorar:** revisão da qualidade do lote e dos registros desconhecidos na cadência definida pela direção; qualquer aumento de rejeições vira pendência, não sucesso.
- **Pendência conhecida:** nome/schema/acesso do CRM e decisão de alvo/fórmula/período/lead qualificado precisam estar no gate ou no bloqueio.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F1-T01 | Validar superfície e materializar dicionário | Representante de dados do cliente | SPEC-F1-001 | CA-1-01 | RED/GREEN do dicionário | dicionário + superfície/permissão | check aprovado; CRM validado ou fallback | planejada |
| F1-T02 | Mapear amostra e checar qualidade | Marketing/comercial piloto | SPEC-F1-001 | CA-1-02, CA-1-05 | GREEN/REFACTOR com fixtures | lote + rejeições + comparação | F1-T01; amostra autorizada | planejada |
| F1-T03 | Gerar baseline e gate de alvo | Consultor Adapta | SPEC-F1-001 | CA-1-03, CA-1-04 | RED/GREEN do baseline e gate | baseline + decisão/bloqueio | F1-T02; decisão humana ou bloqueio formal | planejada |

## Emendas

<!-- Append-only (D19): mudanças aprovadas depois da geração. A história não é reescrita. -->

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
