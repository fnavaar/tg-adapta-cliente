# SPEC-F2-004 — Prova de integração Meta ou fallback manual explícito

**Fase:** 2  
**Status:** liberada para execução das tasks de checklist/fallback (F2-T07/F2-T08); modo integrado permanece bloqueado até prova de acesso  
**Dono:** gestor de tráfego/direção para acesso e permissões; marketing opera o fallback  
**Origem no escopo:** Fase 2, DC-003, G-009, C-01, C-04  
**Degrau da solução:** integração nativa somente após contrato demonstrado; enquanto isso, importação/manualização controlada — o escopo define Meta como candidata, não como integração presumida.

## Contexto e decisões fechadas

- **Estado atual:** Meta é prioritária como candidata, porém acesso, permissões, campos, formato e payload não foram apresentados nesta sessão. O Skip informado requer login e não está acessível por esta conexão.
- **Estado desejado:** a equipe comprova a integração de leitura com campos autorizados **ou** usa fallback manual auditável, sem perda da origem e sem afirmar que há integração.
- **Decisões já fechadas:** publicação, alteração de orçamento e abordagem externa não pertencem a esta SPEC; dados ausentes ficam explícitos.
- **Bloqueios:** sem prova de conta autorizada, escopo de permissão, amostra de payload, owner e política de dados, a modalidade integrada não pode iniciar.

## Resultado observável

Existe um registro `META-F2-###` que classifica a modalidade como `integrada_validada`, `fallback_manual` ou `bloqueada`. Na modalidade integrada, uma leitura autorizada reproduz campos de origem definidos no relatório F2-002. Na modalidade fallback, um lote manual assinado registra origem, período, unidade e lacunas, sem simular conexão Meta.

## Limites e dependências

- **Inclui:** checklist de prontidão Meta, contrato de campos autorizados, prova de leitura/reconciliação ou lote manual, tratamento de erro e rollback.
- **Fora de escopo:** OAuth/credenciais inventados, publicação de campanha, orçamento, escrita no Meta, scraping, integração com agência sem SLA, LinkedIn/Trello/site/Crisp.
- **Entradas e pré-condições:** F2-001/F2-002; decisão de identidade técnica para multi-fonte; aprovação de acesso de leitura; payload sintético/anonimizado; owner da conta.
- **Saídas/artefatos:** checklist de acesso, mapa de campos, evidência de leitura ou log de fallback e reconciliação.
- **Atores e permissões mínimas:** gestor de tráfego concede leitura mínima; direção aprova terceiros/escopo; marketing importa lote; consultor revisa prova inicial.
- **Superfícies afetadas:** conector Meta de leitura se validado; caso contrário, somente superfície manual já autorizada.
- **Risco e plano B:** erro de autorização, rate limit, payload divergente ou indisponibilidade → parar integração, não fazer retry cego e usar/retomar fallback manual com lote identificado.
- **Rollback:** desabilitar somente conector/consulta F2, revogar permissão conforme owner, preservar logs/lotes e dados F1.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Meta → atribuição F2 | API/export oficial da conta autorizada | identificador de campanha/conjunto/anúncio quando disponível, período, origem, canal, custo/impressão/clique; nenhum contato sem aprovação | leitura mínima aprovada; segredo fora de Git/artefato | timeout e limite documentados conforme contrato verificado; importação por lote/chave | 401/403/429/payload inválido interrompem modo integrado |
| fallback manual → atribuição F2 | export assinado ou lançamento do owner | lote_id, data, período, unidade, campos fornecidos, lacunas | editor autorizado | mesmo lote_id não duplica resultado | origem=manual e lacuna Meta explícitas |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F2-011 | acesso/campos/permissão/payload Meta não comprovados | estado `fallback_manual` ou `bloqueada`; não criar conector | nenhuma | G-009 |
| RN-F2-012 | conector lê dados | mapear somente campos autorizados e reconciliar IDs/contagens | dado não previsto é descartado e registrado | §7 F2 |
| RN-F2-013 | 401/403/429, timeout ou payload inválido | parar, registrar erro, não repetir ação externa automaticamente | fallback manual somente se autorizado | §10 do escopo |
| RN-F2-014 | lote manual | marcar origem e período; nunca chamar de dado Meta integrado | nenhuma | DC-003 |

## Fluxo e regras

1. O owner apresenta checklist de acesso, permissão e payload de exemplo; sem os quatro, selecionar fallback/bloqueado.
2. Em modo integrado, mapear campos aprovados, executar somente leitura em massa sintética/escopo aprovado e reconciliar com F2-002.
3. Em fallback, marketing registra lote e lacunas; não há conector, token ou alegação de sincronização.
4. Qualquer falha interrompe a modalidade integrada e preserva o dado existente.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | acesso e payload validados | leitura de campos autorizados reconciliada | habilitar somente consulta aprovada |
| Limite | Meta indisponível, mas export autorizado | fallback manual identificado | revisar quando acesso retornar |
| Falha | 401/403/429 ou campo não previsto | nenhuma escrita/retry cego; erro visível | revogar/desativar e registrar dono |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** escopo §7 F2, §8, G-009 e F2-002; política de dados e decisão de chave, se existirem.
2. **Alterar somente:** checklist, mapa de campos, conector de leitura validado ou importador manual.
3. **Não alterar:** campanhas Meta, orçamento, criativos, permissões amplas, contatos, pipeline F1, integrações de terceiros.
4. **Executar nesta ordem:** validar contrato → testar RED sem credencial → testar leitura com escopo mínimo → reconciliar → testar erro/rollback.
5. **Parar e pedir validação quando:** for necessário conceder permissão, armazenar segredo, ler campo não autorizado, criar OAuth ou haver qualquer escrita/publicação.
6. **Estado válido ao parar:** conector desabilitado ou fallback manual, sem alteração externa e com lacuna visível.

## Checklist de execução

- [ ] Checklist de acesso, conta, escopo, owner e payload foi preenchido.
- [ ] Contrato de campos e chave de reconciliação foi aprovado.
- [ ] Modo integrado passou prova de leitura **ou** fallback manual está explicitamente selecionado.
- [ ] Erro de autorização/limite/timeout exercitado sem escrita externa.
- [ ] Reconciliação de IDs/contagens e rollback foram registrados.

## Critérios de aceite

- [ ] **CA-2-10:** sem acesso Meta validado, o sistema registra `fallback_manual` ou `bloqueada` e não cria/alega integração.
- [ ] **CA-2-11:** com acesso validado, uma leitura limitada reproduz os campos aprovados e reconcilia quantidade e identidade com a fonte.
- [ ] **CA-2-12:** erro de permissão, limite, timeout ou payload inválido deixa a integração sem escrita, com registro do erro e retorno seguro ao fallback/bloqueio.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | tentar modo integrado sem checklist/acesso | iniciar configuração | bloqueado; nenhum segredo/conector criado | checklist e log |
| GREEN | usar payload autorizado/anonimizado ou export manual | importar/consultar e reconciliar | campos permitidos e IDs/contagens coincidem | mapa + comparação |
| REFACTOR/REGRESSÃO | simular 401/403/429/timeout ou lote repetido | executar fluxo de falha | sem escrita/duplicata; fallback/bloqueio visível | log e estado final |

**Dados/fixtures:** payload anonimizado autorizado ou lote `META-F2-MANUAL-001`; sem token, contato, criativo não público ou orçamento.  
**Caminhos de erro obrigatórios:** ausência de acesso, 401/403, rate limit, timeout, payload/campo desconhecido, lote repetido.  
**Evidência exigida:** checklist, contrato de campos, captura/log de leitura ou fallback, reconciliação e demonstração de rollback.

## Handoff e operação

- **Como demonstrar:** mostrar primeiro o estado fallback/bloqueado; somente com acesso comprovado, executar consulta limitada e simular falha.
- **Como operar depois:** gestor de tráfego mantém permissão mínima; marketing monitora lotes/lacunas; direção decide qualquer ampliação.
- **Como monitorar:** erros de acesso, divergência de IDs, lotes repetidos e campos não mapeados.
- **Pendência conhecida:** acesso ao Skip e contrato Meta não foram verificáveis nesta sessão; não habilitar modo integrado até prova concreta.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F2-T07 | Preencher o checklist Meta e documentar contrato de campos/owner ou selecionar formalmente fallback manual. | Gestor de tráfego/direção | F2-004 | RN-F2-011, RN-F2-012 | Contexto e decisões fechadas; Dados e integrações; Checklist | Checklist de acesso, mapa de campos ou justificativa de fallback com owner. | F2-T04 aceita; decisão de identidade para multi-fonte não é necessária se permanecer manual. | Elegível — aguarda autorização expressa do Champion |
| F2-T08 | Provar o fallback manual e a recuperação simulada de falhas sem escrita externa ou duplicidade. | Marketing/gestor de tráfego | F2-004 | CA-2-10, CA-2-12 (simulado) | Critérios de aceite; TDD da SPEC | Log/captura do fallback/bloqueio, estado final e reconciliação do lote. | F2-T07 aceita por teste humano; fallback manual autorizado. | Bloqueada — depende de F2-T07 |
| F2-T09 | Provar leitura Meta limitada, mapeamento autorizado e tratamento real de erro, sem escrita. | Gestor de tráfego/direção | F2-004 | CA-2-11, CA-2-12 (real) | Dados e integrações; Critérios de aceite; TDD da SPEC | Checklist aprovado, mapa de campos, log de leitura, comparação e rollback. | F2-T07 e F2-T08 aceitas; acesso de leitura, permissão, payload, chave multi-fonte e autorização explícita para esta task. | Condicional — não elegível |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
| | | | |