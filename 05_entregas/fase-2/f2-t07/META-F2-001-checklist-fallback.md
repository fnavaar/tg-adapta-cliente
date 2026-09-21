# META-F2-001 — Checklist e contrato Meta/fallback manual

**Task:** F2-T07  
**SPEC:** F2-004 — Prova de integração Meta ou fallback manual explícito  
**Data:** 2026-09-21  
**Status:** `fallback_manual`  
**Owner da decisão e governança:** João Paulo (Champion/direção)  
**Responsável operacional proposto:** marketing/gestor de tráfego, sob revisão da direção  
**Responsável pela qualidade/reconciliação:** marketing registra o lote; comercial devolve qualidade quando disponível; direção decide qualquer ampliação.

## 1. Decisão de modalidade

A modalidade oficial deste ciclo é **`fallback_manual`**.

Não existe integração Meta validada neste momento.

Esta decisão significa:

- não há conector Meta habilitado;
- não há token, OAuth ou segredo armazenado;
- não há chamada à API, Webhook, Business Manager, conta de anúncios, página ou Pixel;
- não há alegação de sincronização automática;
- qualquer dado recebido será identificado como exportação/lote manual do owner;
- uma futura leitura integrada só poderá ser analisada em task própria, com acesso e payload comprovados.

`fallback_manual` **não significa integração Meta**. Significa um processo manual controlado para não bloquear a governança enquanto o acesso integrado não for validado.

## 2. Motivo da decisão

No momento da F2-T07 não foram apresentados, nem verificados:

- conta Meta autorizada;
- Business Manager ou conta de anúncios;
- owner técnico da conta com permissão de leitura;
- escopo de permissão aprovado;
- amostra de payload/API/Webhook/export oficial;
- política de dados para qualquer lead ou contato;
- chave global ou composta para agregar uma segunda fonte técnica.

Conforme RN-F2-011, a ausência de acesso/campos/permissão/payload comprovados impede habilitar o modo integrado. O fallback manual é a modalidade autorizada para este ciclo.

## 3. Owner e responsabilidades

| Papel | Responsável | Responsabilidade |
|---|---|---|
| Decisão e governança | João Paulo (Champion/direção) | Aprovar a modalidade, o escopo do contrato e qualquer futura ampliação. |
| Operação do fallback | Marketing/gestor de tráfego | Receber o export/lote autorizado, registrar `batch_id`, período, campos e lacunas; não chamar o Meta. |
| Qualidade comercial | Comercial | Devolver qualidade/oportunidade disponível, sem inferir informação ausente. |
| Reconciliação | Marketing + responsável pela qualidade da fonte | Comparar lote com a fonte declarada e registrar divergências, sem deduplicação multi-fonte. |
| Revisão inicial | Consultor Adapta | Revisar a primeira prova do fallback, conforme SPEC. |

O owner da conta Meta, a conta específica e as permissões de leitura permanecem **não informados/não validados**. A ausência desses dados é uma lacuna registrada, não uma autorização implícita.

## 4. Contrato mínimo do lote manual

A prova operacional posterior deverá receber um lote identificado, preferencialmente como CSV/XLSX ou lançamento manual assinado pelo owner, contendo somente os campos autorizados e disponíveis.

### Campos de controle obrigatórios

| Campo | Obrigatório | Regra |
|---|---:|---|
| `batch_id` | Sim | Identificador único do lote. O mesmo `batch_id` reenviado não pode gerar uma segunda contagem. |
| `received_at` | Sim | Data/hora de recebimento do lote pelo marketing. |
| `period_start` | Sim | Início do período de referência. |
| `period_end` | Sim | Fim do período de referência. |
| `source_mode` | Sim | Valor fixo `manual_export` ou `manual_entry`; nunca `meta_integrated`. |
| `source_owner` | Sim | Identificador do responsável que forneceu/assinou o lote. |
| `unit_label` | Sim | Unidade/conta/campanha descrita pelo owner, sem inferência técnica. |
| `provided_fields` | Sim | Lista dos campos efetivamente presentes no lote. |
| `missing_fields` | Sim | Lista dos campos esperados e ausentes, quando houver. |
| `reconciliation_status` | Sim | `pendente`, `reconciliado`, `divergente` ou `bloqueado`. |

### Campos de campanha aceitos, se presentes no export

| Campo | Regra |
|---|---|
| `campaign_id` | Preservar como identificador fornecido; não tratar como identidade global. |
| `campaign_name` | Preservar o nome informado pelo owner. |
| `adset_id` | Aceitar somente se vier no lote autorizado; pode ficar ausente. |
| `adset_name` | Aceitar somente se vier no lote autorizado; pode ficar ausente. |
| `ad_id` | Aceitar somente se vier no lote autorizado; pode ficar ausente. |
| `ad_name` | Aceitar somente se vier no lote autorizado; pode ficar ausente. |
| `period` | Usar o período declarado no lote; não inferir de timestamp parcial. |
| `channel` | Registrar `Meta`/`manual_export` somente como origem declarada do lote; não converter clique em lead. |
| `impressions` | Métrica de atividade; não é qualidade comercial. |
| `clicks` | Métrica de atividade; não é qualidade comercial. |
| `spend` | Não aceitar nesta task como autorização de orçamento ou gasto; se aparecer, registrar como campo não utilizado/lacuna e não importar. |

## 5. Leads, formulários e dados pessoais

A F2-T07 não autoriza ingestão de leads nem de contatos.

Não serão aceitos nesta task:

- nome de pessoa;
- e-mail;
- telefone;
- cargo de pessoa;
- `lead_id` como identidade de demanda;
- conteúdo de formulário;
- Pixel/eventos de pessoa;
- qualquer dado pessoal ou contato real.

`form_id` e `lead_id` não fazem parte do contrato operacional desta T07. Se forem necessários no futuro, exigem decisão de escopo, política de dados, regra de minimização e autorização específica.

## 6. Campos ausentes, desconhecidos e proibidos

- Campo ausente não vira zero.
- Campo não fornecido deve aparecer em `missing_fields`/lacunas.
- Campo desconhecido não deve ser inferido a partir do nome da campanha, canal ou clique.
- Campo não previsto deve ser descartado do processamento e registrado como não mapeado.
- Custo/gasto não autoriza orçamento nem publicação.
- Impressão/clique não equivale a lead qualificado, oportunidade, proposta, conversão ou receita.
- A origem manual deve permanecer explícita; não registrar o lote como integração Meta.

## 7. Regra de chave e reconciliação

A T07 não cria identidade global nem identidade composta entre fontes técnicas.

A regra autorizada para o fallback é:

1. `batch_id` identifica o lote manual e garante idempotência do reprocessamento do mesmo lote;
2. `campaign_id`/`adset_id`/`ad_id`, se presentes, são atributos preservados do export, não chaves globais do CRM;
3. para comparar com a fonte já declarada na F2-002, usar somente a chave disponível no escopo dessa fonte (`record_id`) quando o lote autorizado trouxer referência correspondente;
4. se não houver `record_id` correspondente, classificar como `não_vinculado`/`desconhecido`, sem criar, mesclar ou deduplicar contra outra fonte;
5. divergência de quantidade ou identidade permanece visível com owner e status `divergente`/`bloqueado`;
6. nenhuma regra desta task decide `record_id` global, chave composta ou agregação Meta + outra fonte.

## 8. Como o fallback deverá funcionar na F2-T08

A F2-T07 somente deixa o contrato preparado. A F2-T08 deverá provar, com lote sintético/manual autorizado:

1. receber `META-F2-MANUAL-001` com `batch_id`, período, origem manual e campos permitidos;
2. registrar o lote sem alegar conexão Meta;
3. comparar contagens/identificadores disponíveis com a fonte declarada;
4. manter lacunas e desconhecidos explícitos;
5. reenviar o mesmo `batch_id` sem duplicar resultado;
6. simular 401/403/429/timeout/payload inválido como falhas de fluxo, sem chamada externa;
7. deixar o estado final como fallback/manual ou bloqueado, conforme o cenário;
8. preservar os dados F1/F2 e não escrever em `demandas` sem autorização específica.

Nenhum desses testes foi executado nesta T07.

## 9. O que fica para a F2-T09

A F2-T09 é condicional e somente poderá ocorrer depois de T07 e T08 aceitas, com autorização própria, se houver:

- acesso de leitura aprovado;
- owner da conta identificado;
- permissão mínima definida;
- payload autorizado/anonimizado;
- política de dados aprovada;
- contrato de chave/reconciliação aceito;
- autorização explícita para a consulta real.

A T09 poderá provar uma leitura Meta limitada, mapeamento dos campos autorizados, reconciliação e erro real permitido. Ainda assim, não poderá publicar, alterar orçamento ou escrever no Meta.

## 10. Checklist de prontidão F2-T07

| Item | Estado | Evidência/observação |
|---|---|---|
| Modalidade escolhida | **PASSOU** | `fallback_manual` autorizada pelo Champion. |
| Integração Meta validada | **NÃO** | Nenhuma chamada, token ou payload real foi apresentado/verificado. |
| Conta/Business Manager/conta de anúncios | **NÃO INFORMADO** | Não necessário para selecionar o fallback; necessário somente se T09 for autorizada. |
| Owner da decisão | **PASSOU** | João Paulo (Champion/direção). |
| Responsável operacional | **PASSOU** | Marketing/gestor de tráfego. |
| Responsável pela qualidade | **PASSOU** | Marketing + comercial, com direção para divergência/ampliação. |
| Política de dados para contatos | **NÃO APLICÁVEL À T07** | A T07 não aceita leads, formulários ou contatos. |
| Payload Meta | **NÃO** | Não solicitado nem obtido; fallback não simula payload Meta. |
| Contrato mínimo de campos | **PASSOU** | Seções 4 a 6 deste documento. |
| Regra de lote/idempotência | **PASSOU** | `batch_id` identifica o lote; reenvio não duplica. |
| Regra de reconciliação | **PASSOU COM LIMITE** | `record_id` somente no escopo da fonte declarada; sem identidade global/multi-fonte. |
| F2-T08 autorizada/iniciada | **NÃO** | Próxima task depende deste fechamento e de novo gate. |
| F2-T09 autorizada/iniciada | **NÃO** | Condicional; requer gates próprios. |

## 11. Evidências e limites desta task

- Registro: `META-F2-001`.
- Modalidade: `fallback_manual`.
- Artefato: contrato/checklist deste documento.
- Dados reais Meta: nenhum.
- Leads/contatos: nenhum.
- Token/OAuth/segredo: nenhum.
- Chamada externa: nenhuma.
- Alteração em `demandas`: nenhuma.
- Alteração em T04: nenhuma.
- Nova collection/migration/hook/RLS: nenhuma.
- Prova operacional do lote: reservada à F2-T08.
- Leitura real Meta: reservada, se elegível, à F2-T09.

## 12. Veredito da F2-T07

O contrato mínimo da modalidade `fallback_manual` está definido, com owner, campos permitidos, lacunas, dados proibidos, regra de lote, idempotência e reconciliação limitada à fonte declarada.

A F2-T07 não criou nem alegou integração Meta. O documento deixa explícito o que será provado na F2-T08 e o que permanece condicional para a F2-T09.

A task deve parar no gate de validação humana antes de qualquer fechamento formal.
