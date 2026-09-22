# Jornada — Fase 2

## Tasks

| ID | Leva | Task | Dono | SPEC | Critério | Subseção exata da SPEC | Recorte da prova | Evidência esperada | Pré-condições | Ponto de parada | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| F2-T01 | 1 | Materializar a superfície mínima de briefing versionado e seus estados, usando apenas massa sintética. | Marketing/gestor de tráfego | F2-001 | CA-2-01 | Dados e integrações; Fluxo e regras; Checklist | Criar `EXP-F2-IN-001` e `EXP-F2-OUT-001`, localizar por ID/versão/dono. | Captura/export da superfície com os dois briefings. | Acesso à superfície F1 ou fallback manual confirmado; owner do modelo; autorização confirmada. | Parar se exigir campo estrutural, dado pessoal, gasto ou publicação. | Concluída e validada |
| F2-T02 | 2 | Provar validações de briefing incompleto, duplicação e aprovação de publicação/gasto. | Marketing/gestor de tráfego | F2-001 | CA-2-01, CA-2-02, CA-2-03 | Critérios de aceite; TDD da SPEC | RED `EXP-F2-RED-001`; alterar mensagem/criativo e preservar versão anterior. | Log/captura de bloqueio, comparação v1/v2 e aprovação/bloqueio rastreável. | F2-T01 aceita por teste humano; autorização confirmada. | Parar se o sistema permitir publicação/gasto sem aprovação humana. | Concluída e validada em 2026-09-11 |
| F2-T03 | 3 | Configurar/registrar contrato de atribuição de fonte única e fixtures de qualidade, sem agregação multi-fonte. | Marketing + comercial | F2-002 | RN-F2-004, RN-F2-005, RN-F2-006 | Dados e integrações; Fluxo e regras; Checklist | Criar `ATR-F2-IN-001`, `ATR-F2-OUT-001`, `ATR-F2-UNK-001`; registrar chave usada e pendência multi-fonte. | Mapa de campos/chave, fixtures e registro de pendência. | F2-T02 aceita; fonte única declarada; dono da qualidade definido. | Parar se precisar escolher `record_id` global/composto ou agregar fonte técnica adicional. | Concluída e validada em 2026-09-14 |
| F2-T04 | 4 | Provar atribuição, desconhecido, duplicidade e reconciliação por IDs contra a fonte declarada. | Marketing + comercial | F2-002 | CA-2-04, CA-2-05, CA-2-06 | Critérios de aceite; TDD da SPEC | RED sem origem/chave repetida; GREEN inbound/outbound; regressão reexecuta lote. | Relatório, lista de IDs, comparação fonte×relatório e lista de lacunas com dono. | F2-T03 aceita por teste humano; fonte acessível ou lacuna formal aceita. | Parar diante de divergência sem explicação, duplicação ou tentativa de somar multi-fonte. | Concluída e validada em 2026-09-17 |
| F2-T05 | 5 | Materializar o registro de decisão e a fila de próxima ação para um experimento já reconciliado. | Direção/marketing | F2-003 | RN-F2-008, RN-F2-010 | Dados e integrações; Fluxo e regras; Checklist | Criar estrutura `DEC-F2-###` ligada a briefing, período, evidência, decisão, owner e próxima ação. | Captura/export do registro e permissões de decisão. | F2-T04 aceita; decisor identificado; critério de decisão definido no briefing. | Parar se exigir decisão automática, meta inferida, mudança de orçamento ou publicação. | Concluída e validada em 2026-09-21 |
| F2-T06 | 6 | Provar decisão baseada em qualidade e o histórico de ajuste/revogação. | Direção/marketing | F2-003 | CA-2-07, CA-2-08, CA-2-09 | Critérios de aceite; TDD da SPEC | RED `DEC-F2-RED-001` só com clique; GREEN decisão `ajustar`; regressão revoga e preserva histórico. | Decisão humana, relatório referenciado e histórico de revogação/versão. | F2-T05 aceita por teste humano. | Parar se resultado incompleto aparecer como êxito ou se o sistema agir externamente. | Concluída e validada em 2026-09-21 |
| F2-T07 | 5 | Preencher o checklist Meta e documentar contrato de campos/owner ou selecionar formalmente fallback manual. | Gestor de tráfego/direção | F2-004 | RN-F2-011, RN-F2-012 | Contexto e decisões fechadas; Dados e integrações; Checklist | Tentar iniciar modo integrado sem checklist; selecionar `fallback_manual`/`bloqueada` quando faltar acesso. | Checklist de acesso, mapa de campos ou justificativa de fallback com owner. | F2-T04 aceita; decisão de identidade para multi-fonte não é necessária se permanecer manual. | Parar sem acesso, permissão, payload ou se houver pedido de segredo/OAuth/escrita Meta. | Concluída e validada em 2026-09-21 |
| F2-T08 | 6 | Provar o fallback manual e a recuperação simulada de falhas sem escrita externa ou duplicidade. | Marketing/gestor de tráfego | F2-004 | CA-2-10, CA-2-12 (simulado) | Critérios de aceite; TDD da SPEC | RED sem credencial; lote `META-F2-MANUAL-001`; simular 401/403/429/timeout/payload inválido e lote repetido. | Log/captura de fallback/bloqueio, estado final e reconciliação do lote. | F2-T07 aceita por teste humano; fallback manual autorizado. | Parar se a prova exigir chamada real ao Meta ou qualquer escrita/publicação. | Concluída e validada em 2026-09-21 — bateria humana 5/5, CA-2-10/12 aprovados |
| F2-T09 | Condicional | Provar leitura Meta limitada, mapeamento autorizado e tratamento real de erro, sem escrita. | Gestor de tráfego/direção | F2-004 | CA-2-11, CA-2-12 (real) | Dados e integrações; Critérios de aceite; TDD da SPEC | Consulta limitada com payload autorizado; reconciliar IDs/contagens; exercer erro real permitido. | Checklist aprovado, mapa de campos, log de leitura, comparação e rollback. | F2-T07 e F2-T08 aceitas; acesso de leitura, permissão, payload, chave multi-fonte e autorização explícita para esta task. | Parar em 401/403/429/timeout/campo não autorizado; desabilitar consulta e retornar a fallback. | Implementação autorizada; bloqueada por conector Meta sem conta conectada |

## Ordem e independência

- **Leva 1:** F2-T01.
- **Leva 2:** F2-T02, após F2-T01.
- **Leva 3:** F2-T03, após F2-T02.
- **Leva 4:** F2-T04, após F2-T03.
- **Leva 5:** F2-T05, após F2-T04; F2-T07, após F2-T04 — são independentes entre si.
- **Leva 6:** F2-T06, após F2-T05; F2-T08, após F2-T07 — são independentes entre si.
- **F2-T09:** não participa de leva fixa; ficou inelegível até os gates explícitos da própria linha; após a reavaliação de 2026-09-22 foi autorizada, mas a execução está bloqueada pela ausência de conta conectada no conector Meta.
- **Execução:** uma task por vez, mediante autorização expressa do Champion e teste humano ao fim de cada uma.

## Registro de tentativa de execução da F2-T09 (2026-09-22)

- Autorização expressa recebida às 11:28.
- Preflight confirmou produto preservado; a única pendência do Skip era o `.skip.config.json` preexistente.
- A consulta planejada foi limitada à conta `act_1667348577717128`, nível `account`, período 15/09/2026–21/09/2026 e campos aprovados.
- A primeira tentativa foi rejeitada antes da chamada por parâmetro técnico inválido; após correção, o conector retornou `No connected account found for user ID 29567e12-3903-4558-9e24-8358d910e5d4`.
- Nenhum dado foi retornado; não houve chamada efetiva ao Meta, alteração de produto, banco, `demandas`, campanha, orçamento ou criativo.
- A T09 permanece aberta e bloqueada por dependência externa; retomada somente após conexão/autorização do Meta no ambiente do conector.

## Registro de fechamento da F2-T08 (2026-09-21)

- F2-T08 foi concluída após autorização expressa do Champion, revalidação automatizável e bateria humana 5/5 aprovada.
- CA-2-10 passou: `fallback_manual` foi mantido explícito; não há integração Meta alegada ou criada.
- CA-2-12 passou no recorte simulado: lote manual, replay idempotente, conflito de payload e cinco falhas simuladas sem escrita ou retry cego.
- T04 permaneceu 7/7; T08 permaneceu 8/8; `demandas` permaneceu com 10 registros.
- F2-T01–T07 foram preservadas. Nenhuma collection, migration, campo, hook, RLS, token, OAuth, dado real/pessoal, publicação ou alteração de orçamento foi criada no fechamento.
- O produto funcional permaneceu em Skip v0.0.85 (`25c717a`).
- O verificador independente prescrito não estava disponível neste runtime; checklist equivalente foi executado em série e a limitação foi registrada na evidência/relatório.
- F2-T09 não foi iniciada e continua condicional.

## Registro de regularização documental (2026-09-17)

- Publicadas as SPECs F2-003 e F2-004, que constavam da decomposição aprovada em 03/09 mas não haviam sido enviadas na liberação original da fase.
- As SPECs F2-001 e F2-002 foram substituídas pelas versões validadas da mesma decomposição, eliminando a divergência de numeração CA/RN entre esta jornada e as SPECs.

## Registro de reavaliação da F2-T09 (2026-09-22)

- Gates 1 a 5 de elegibilidade foram atendidos e registrados em `06_notas/f2-t09-elegibilidade-2026-09-22.md`.
- A F2-T09 está elegível para implementação controlada, mas não autorizada e não concluída.
- CA-2-11 e CA-2-12 no recorte real permanecem pendentes.
- Nenhuma conexão, chamada Meta, leitura real ou alteração funcional foi realizada.
