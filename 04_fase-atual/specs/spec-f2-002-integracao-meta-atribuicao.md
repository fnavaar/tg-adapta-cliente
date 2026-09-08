# SPEC-F2-002 — Integração Meta Ads e atribuição de origem

**Fase:** 2 — Sistema de campanhas e experimentação de Growth Marketing  
**Status:** planejada  
**Dono:** gestor de tráfego, responsável de TI/Dados do cliente e consultor Adapta  
**Origem no escopo:** DC-003, C-01, C-04, G-009 e RQ-002  
**Degrau da solução:** reuso/conector nativo — integrar a API/Webhook do Meta Ads quando token, permissões e schema forem demonstrados; utilizar importação manual com marcação de origem como fallback obrigatório se o acesso direto não for autorizado.

## Contexto e decisões fechadas

- **Estado atual:** dados de anúncios e formulários de cadastro do Meta (Facebook/Instagram Ads) são coletados sem automação de contrato nem garantia de repasse de parâmetros de origem (UTMs, `ad_id`, `form_id`). Fonte: `03-Projeto/02-Escopo-Definitivo.md`, seção Fase 2.
- **Estado desejado:** os leads gerados via Meta Ads entram no pipeline da Fase 1 mantendo a rastreabilidade completa da origem (`canal=Meta`, `campanha`, `adset`, `ad_id`, `form_id`), via integração direta ou fallback manual documentado.
- **Decisões já fechadas:** a integração nativa com o Meta é condicional à confirmação prévia de acessos e permissões da conta de anúncios; se não houver acesso verificado, é obrigatório utilizar o fluxo de importação manual com tag de origem para não bloquear a fase.

## Resultado observável

Ao aceitar esta SPEC, a equipe demonstra:

1. `03-Projeto/02-Plano_de_acao/02.Fase_2/02-Evidencias/contrato-dados-meta-f2.md`, especificando os campos capturados da API/Webhook ou do export manual.
2. Demonstração de ingestão de um lote de teste (ou real) vindo do Meta Ads, comprovando que a origem e campanha são gravadas no pipeline sem perda de atributos.
3. `03-Projeto/02-Plano_de_acao/02.Fase_2/02-Evidencias/plano-fallback-meta-f2.md`, atestando a operacionalidade da importação por planilha caso o acesso via API seja suspenso ou não concedido.

## Regras de negócio

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F2-005 — Validação de token/acesso | Início da configuração da integração Meta | Checar permissões `leads_retrieval` / `ads_read` | Se o acesso falhar, ativar imediatamente o fallback manual de exportação | DC-003, G-009 |
| RN-F2-006 — Atribuição inalterável | Entrada de lead vindo de anúncio | Gravar obrigatoriamente `canal=Meta_Ads`, `campanha_id` e `ad_id` | Se algum campo vier nulo, gravar `desconhecido` sem omitir o lead | C-01, RQ-002 |
| RN-F2-007 — Idempotência de leads | Reprocessamento de webhook ou arquivo | Usar `lead_id` do Meta como chave primária/canônica de deduplicação | Leads sem identificador do Meta usam combinação `email` + `data` | C-01, RN-F1-004 |

## Checklist de execução

- [ ] Credenciais e permissões da conta Meta Ads validadas ou fallback ativado.
- [ ] Mapeamento de campos do formulário Meta → dicionário de dados da Fase 1 realizado.
- [ ] Teste de ingestão (via Webhook/API ou planilha de fallback) executado com sucesso.
- [ ] Verificação de duplicidade por `lead_id` / `email` comprovada.

## Critérios de aceite

- [ ] **CA-2-05:** A permissão de acesso à API/Webhook do Meta Ads é confirmada, ou o plano de fallback de importação por planilha é homologado e testado.
- [ ] **CA-2-06:** Cada lead vindo do Meta Ads entra no pipeline com a taxonomia correta, preservando o nome da campanha e o identificador do anúncio/formulário.
- [ ] **CA-2-07:** Reenviar o mesmo lote ou evento do Meta Ads não gera duplicidade no CRM/pipeline (idempotência por `lead_id`).
