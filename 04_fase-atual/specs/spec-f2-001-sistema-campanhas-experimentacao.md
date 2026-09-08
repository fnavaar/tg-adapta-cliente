# SPEC-F2-001 — Sistema de campanhas e experimentação de Growth Marketing

**Fase:** 2 — Sistema de campanhas e experimentação de Growth Marketing  
**Status:** planejada  
**Dono:** marketing, gestor de tráfego e consultor Adapta  
**Origem no escopo:** C-02, C-01 expandido, C-04 expandido, RQ-002, RQ-005, DC-001, DC-004, DC-007 e G-009  
**Degrau da solução:** reuso/extensão — estender o dicionário de demanda e a camada de pipeline da Fase 1 para estruturar o registro de experimentos de Growth Marketing, mantendo formulários/planilhas de cadastro e relatórios de experimentos vinculados.

## Contexto e decisões fechadas

- **Estado atual:** as ações de geração de demanda ocorrem sem versionamento de hipóteses, segmentação ou criativos. Métricas de alcance (impressões/cliques) são por vezes misturadas com conversão real em oportunidades. Fonte: `03-Projeto/02-Escopo-Definitivo.md`, seção Fase 2.
- **Estado desejado:** cada campanha ou teste possui registro de hipótese, público-alvo (ICP), mensagem, versão de criativo, canal, orçamento autorizado, janela de execução, dono e critério explícito de parada/continuidade.
- **Decisões já fechadas:** funis inbound e outbound operam com métricas separadas; volume de cliques não é critério isolado de sucesso; migração VSL → formulário/chatbot é tratada como hipótese a testar; orçamentos e publicações externas exigem aprovação explícita; nenhuma otimização autônoma sem revisão humana é permitida nesta fase.

## Resultado observável

Ao aceitar esta SPEC, a equipe demonstra três artefatos da Fase 2:

1. `03-Projeto/02-Plano_de_acao/02.Fase_2/02-Evidencias/registro-experimentos-f2.csv` (ou visualização equivalente no CRM/Painel), com hipóteses, criativos, canais, janelas e orçamentos.
2. `03-Projeto/02-Plano_de_acao/02.Fase_2/02-Evidencias/relatorio-experimento-piloto-f2.md`, comparando resultados inbound vs outbound em termos de cliques, leads, leads qualificados e oportunidades geradas.
3. `03-Projeto/02-Plano_de_acao/02.Fase_2/02-Evidencias/decisao-experimento-f2.md`, registrando a decisão formal (`CONTINUAR`, `AJUSTAR` ou `INTERROMPER`) com embasamento de qualidade e prova de reversibilidade (rollback).

## Limites e dependências

- **Inclui:** modelo de dados para registro de experimentos; separação estrita entre métricas de volume e conversão qualificada; vinculo dos leads capturados à taxonomia da Fase 1; critérios de parada e rollback de versões de campanha.
- **Fora de escopo:** alteração autônoma de orçamento; disparo de emails/mensagens sem aprovação prévia; redesign do site institucional; integração presumida com agência sem contratação/SLA.
- **Entradas e pré-condições:** Fase 1 concluída e dicionário de demanda operacional; orçamento e canais aprovados pela direção/cliente.
- **Saídas/artefatos:** registros de experimentos, relatório do piloto inbound/outbound e termo de decisão do experimento.

## Regras de negócio

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F2-001 — Hipótese antes da ação | Nova campanha ou variação | Exigir documento/registro com hipótese, ICP, versão, canal e critério de parada | Ações sem hipótese formal são classificadas como `não documentadas` e bloqueadas | C-02, DC-007 |
| RN-F2-002 — Inbound e outbound isolados | Apuração de resultados | Separar métricas de custo/clique e qualificação de inbound e outbound no painel | Não consolidar custo por lead geral sem a quebra por origem | DC-001, C-04 |
| RN-F2-003 — Clique não é sucesso | Avaliação de performance | Qualificação e avanço para oportunidade se sobrepõem ao volume de cliques | Se o custo/clique for baixo mas a qualificação for zero, sinalizar `hipótese frustrada` | C-02, RQ-005 |
| RN-F2-004 — Aprovação prévia para publicação | Qualquer alteração de verba ou peça | Exigir aprovação do responsável antes de ativar a versão | Publicações sem aceite prévio devem ser pausadas imediatamente (rollback) | DC-006, G-009 |

## Checklist de execução

- [ ] Estrutura de cadastro de experimentos (hipótese, ICP, oferta, mensagem, orçamento e dono) está pronta.
- [ ] Separação de métricas de inbound e outbound está configurada no painel.
- [ ] Vínculo dos leads capturados com a taxonomia (`record_id`, `origem`, `campanha`) da Fase 1 foi validado.
- [ ] Teste piloto executado e decisão de continuidade registrada com evidências.

## Critérios de aceite

- [ ] **CA-2-01:** Todo experimento possui registro contendo hipótese, público-alvo, canal, versão de criativo, janela de execução, orçamento e critério de parada.
- [ ] **CA-2-02:** A captura de leads decorrente de campanhas atribui corretamente a origem (`inbound` ou `outbound`) e conecta os registros ao pipeline da Fase 1.
- [ ] **CA-2-03:** O relatório do experimento exibe de forma distinta métricas de alcance (impressões/cliques) e métricas de conversão comercial (leads qualificados/oportunidades).
- [ ] **CA-2-04:** A decisão de interromper ou pausar uma variação de campanha restabelece a versão anterior sem perda de histórico de dados capturados.
