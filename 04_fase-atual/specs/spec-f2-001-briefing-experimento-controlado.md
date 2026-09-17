# SPEC-F2-001 — Briefing versionado de experimento controlado

**Fase:** 2  
**Status:** liberada para execução — F2-T01 e F2-T02 concluídas e validadas (2026-09-11)  
**Dono:** marketing/gestor de tráfego; direção aprova canal, orçamento e publicação quando aplicável  
**Origem no escopo:** Fase 2, C-02, C-01, DC-001, DC-004 e G-006  
**Degrau da solução:** construção mínima no CRM/tabela controlada já usada na Fase 1 — a Fase 2 precisa registrar o experimento antes de qualquer integração ou automação.

## Contexto e decisões fechadas

- **Estado atual:** a Fase 1 declarou pipeline/painel mínimo aceito; a fonte técnica viva não foi acessível nesta sessão. O escopo exige separar inbound de outbound e não confundir clique com qualidade.
- **Estado desejado:** cada tentativa de campanha possui um briefing versionado e executável por uma pessoa autorizada.
- **Decisões já fechadas:** VSL → formulário/chatbot é hipótese; publicação e orçamento nunca são automáticos; Meta não é pré-requisito.
- **Bloqueios:** sem ICP, oferta, canal, período, owner e critério de parada aprovados para o experimento, não iniciar execução.

## Resultado observável

Um briefing identificado `EXP-F2-###` contém hipótese, inbound/outbound, segmento/ICP, oferta, mensagem, versão de criativo, canal, período, dono, critério de decisão, critério de parada e aprovação humana aplicável; sua execução humana pode ser registrada sem publicar via sistema.

## Limites e dependências

- **Inclui:** modelo de briefing, versionamento, estado `planejado`/`aprovado para execução humana`/`pausado` e referência ao pipeline F1.
- **Fora de escopo:** publicar anúncio, criar campanha Meta, definir orçamento em nome da direção, redesenhar site, chatbot ou VSL.
- **Entradas e pré-condições:** owner identificado; ICP/oferta/mensagem fornecidos pelo responsável; autorização escrita quando houver gasto ou publicação.
- **Saídas/artefatos:** briefing de experimento e registro de aprovação ou bloqueio.
- **Atores e permissões mínimas:** marketing edita rascunho; direção aprova gasto/publicação; comercial só consulta e devolve qualidade; consultor revisa primeiro ciclo.
- **Superfícies afetadas:** superfície de campanha no Skip ou tabela manual controlada; nenhuma integração nova.
- **Risco e plano B:** se a superfície Skip não estiver acessível, usar tabela controlada com o mesmo esquema e marcar `origem_registro=manual`.
- **Rollback:** pausar o briefing e preservar versões/decisões; não apagar histórico.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Briefing → superfície F1 | formulário/tabela aprovada | `experimento_id`, tipo, hipótese, ICP/segmento, oferta, mensagem, criativo_versao, canal, período, dono, critério_decisão, parada, estado | editor autorizado | reenvio do mesmo `experimento_id` atualiza versão, não cria duplicata | campos obrigatórios ausentes mantêm rascunho bloqueado |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F2-001 | tipo é inbound ou outbound | registrar um único tipo por experimento | desconhecido bloqueia aprovação | Fase 2/C-02 |
| RN-F2-002 | mudança de mensagem, criativo, canal ou segmento | criar nova versão; preservar a anterior | correção meramente descritiva registra motivo | Fase 2 |
| RN-F2-003 | há gasto/publicação | exigir referência de aprovação humana imediatamente anterior | sem aprovação, estado fica `planejado` | §8 e §10 do escopo |

## Fluxo e regras

1. Marketing cria `EXP-F2-###` como rascunho e preenche campos mínimos.
2. Direção aprova ou bloqueia gasto/publicação; sem essa necessidade, owner aprova a execução interna.
3. O experimento recebe versão e período; a pessoa autorizada executa fora do sistema.
4. O resultado é entregue à SPEC-F2-002; nenhuma métrica aprova a hipótese nesta etapa.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | briefing completo, sem publicação | versão pronta para medição | seguir SPEC-F2-002 |
| Limite | canal ou criativo ainda desconhecido | rascunho bloqueado e lacuna explícita | completar pelo owner |
| Falha | pedido de publicação sem aprovação | não publicar; registrar bloqueio | direção decide ou pausa |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** escopo definitivo §5 C-01/C-02, §7 Fase 2 e §8; estado e dicionário F1.
2. **Alterar somente:** superfície/tabela de briefing e suas permissões mínimas.
3. **Não alterar:** orçamento, contas Meta, campanhas, pipeline F1, dados DHO e dados pessoais não necessários.
4. **Executar nesta ordem:** validar acesso → criar massa sintética → validar RED/GREEN → criar um briefing real somente após aceite.
5. **Parar e pedir validação quando:** houver gasto, publicação, novo canal, dado pessoal ou campo estrutural não previsto.
6. **Estado válido ao parar:** briefing permanece rascunho/bloqueado, sem ação externa.

## Checklist de execução

- [ ] Campos mínimos e valores permitidos configurados/documentados.
- [ ] Uma versão sintética inbound e uma outbound criadas sem publicação.
- [ ] Aprovação/bloqueio de gasto é rastreável.
- [ ] Evidência e owner registrados.

## Critérios de aceite

- [ ] **CA-2-01:** um briefing completo de experimento pode ser localizado por ID, versão e dono.
- [ ] **CA-2-02:** tentativa de aprovar briefing sem hipótese, período, tipo, owner ou critério de parada é bloqueada visivelmente.
- [ ] **CA-2-03:** gasto/publicação não é registrado como autorizado sem referência de aprovação humana.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | briefing sem período e owner | salvar massa `EXP-F2-RED-001` | bloqueado, sem execução | captura/log da superfície |
| GREEN | briefing `EXP-F2-IN-001` completo, sem publicação | registrar e consultar por ID | versão e campos obrigatórios visíveis | registro exportado/captura |
| REFACTOR/REGRESSÃO | alterar mensagem/criativo | criar versão 2 e consultar v1 | v1 preservada; sem nova publicação | comparação das versões |

**Dados/fixtures:** `EXP-F2-IN-001`, `EXP-F2-OUT-001`, sem contatos reais.  
**Caminhos de erro obrigatórios:** campo ausente, tipo inválido, publicação sem aprovação, duplicação de ID.  
**Evidência exigida:** captura/export do briefing, aprovação/bloqueio e demonstração pelo owner.

## Handoff e operação

- **Como demonstrar:** abrir dois briefings sintéticos e mostrar que nenhum cria publicação.
- **Como operar depois:** marketing revisa antes da execução; direção aprova gastos; comercial recebe somente o ID do experimento.
- **Como monitorar:** revisar briefings bloqueados e versões sem critério de decisão.
- **Pendência conhecida:** capacidade por etapa e Meta permanecem fora desta SPEC.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F2-T01 | Materializar a superfície mínima de briefing versionado e seus estados, usando apenas massa sintética. | Marketing/gestor de tráfego | F2-001 | CA-2-01 | Dados e integrações; Fluxo e regras; Checklist | Captura/export da superfície com os dois briefings. | Acesso à superfície F1 ou fallback manual confirmado; owner do modelo. | Concluída e validada em 2026-09-11 |
| F2-T02 | Provar validações de briefing incompleto, duplicação e aprovação de publicação/gasto. | Marketing/gestor de tráfego | F2-001 | CA-2-01, CA-2-02, CA-2-03 | Critérios de aceite; TDD da SPEC | Log/captura de bloqueio, comparação v1/v2 e aprovação/bloqueio rastreável. | F2-T01 aceita por teste humano. | Concluída e validada em 2026-09-11 |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
| | | | |