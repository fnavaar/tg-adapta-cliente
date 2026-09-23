# SPEC-F3-003 — Handoffs por papel com aceite, SLA e recuperação

**Fase:** 3
**Status:** planejada
**Dono:** direção aprova a matriz; gerentes/comercial/operação executam; consultor valida o primeiro handoff
**Origem no escopo:** Fase 3; C-05; DC-004; DC-005; RQ-004; G-004; G-005
**Degrau da solução:** construção mínima — registro de handoff com aceite, SLA, escalonamento e recuperação sobre o pipeline existente; sem conector externo.

## Contexto e decisões fechadas

- **Estado atual:** a F1 entregou handoff manual com registro de tentativa (RN-F1-012: sem ação externa automática); a F2 validou tratamento de falha externa com estado seguro e sem retry cego (CA-2-12 real). Não existe matriz nominal de handoffs (quem age, o que recebe, SLA, como aceita, como escala, como registra falha, como encerra/recupera).
- **Estado desejado:** cada passagem de guarda (comercial→operação, marketing→comercial, operação→comercial) tem registro com destinatário, conteúdo mínimo, SLA de aceite, estado (pendente/aceito/recusado/expirado), escalonamento e recuperação; handoff sem aceite, sem resposta e com falha de acesso tem recuperação demonstrável.
- **Decisões já fechadas:** handoff é sempre humano e registrado; falha externa → estado seguro + registro + fallback manual, sem retry automático (EV-04); agência/terceiro somente com escopo/dado/SLA explicitamente aprovados (G-004).
- **Bloqueios:** B3-RACI-01 — matriz nominal de papéis/handoffs aprovada pelo Champion (quem aceita, quem escala, SLA por papel) antes da PROVA de handoff; a task de materialização pode avançar com papéis provisórios registrados como pendência, mas CA-3-06/07/08 exigem a matriz nominal.

## Resultado observável

1. Um handoff registrado contém: origem (papel/pessoa), destinatário, conteúdo mínimo (registro de demanda, próxima ação, prazo), SLA de aceite e estado rastreável.
2. Handoff sem aceite no SLA escala automaticamente ao dono definido na matriz; sem resposta mantém pendência visível com dono e prazo.
3. Falha de acesso/canal registra o motivo e retorna o caso ao remetente com estado seguro — sem perda do registro e sem retry cego.
4. Encerramento/recuperação: handoff recusado ou expirado volta ao pipeline com motivo; nada é encerrado sem pessoa responsável.

## Limites e dependências

- **Inclui:** registro de handoff + estados + SLA + escalonamento + recuperação; log append-only de eventos de handoff; superfície mínima para registrar/aceitar/recusar.
- **Fora de escopo:** disparo automático de mensagem externa; WhatsApp/e-mail automáticos; integração com ferramenta de terceiros; decisão comercial sem pessoa; Customer Success.
- **Entradas e pré-condições:** SPEC-F3-001 aceita (pipeline integrado); matriz RACI nominal para a prova (B3-RACI-01).
- **Saídas/artefatos:** registro de handoffs; log de eventos; evidência `handoffs-f3.md`.
- **Dependências e responsáveis:** direção aprova SLA/matriz; gerentes executam; operação aceita/devolve; consultor revisa o primeiro ciclo.
- **Atores e permissões mínimas:** escrita por papel (remetente/destinatário); leitura direção/consultor; sem dado sensível.
- **Superfícies/arquivos/configurações afetadas:** nova estrutura de registro de handoff (não destrutiva); superfície mínima; sem conector externo.
- **Risco e plano B:** matriz RACI atrasa → materializar com papéis provisórios e pendência nomeada; adoção baixa → medir separadamente (G-005).
- **Rollback ou reversão:** suspender novos handoffs no fluxo integrado, manter registro manual e reprocessar somente casos com evidência preservada (rollback da fase).

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| Pipeline (F3-001) → handoff | Registro de demanda + próxima ação | handoff_id, origem, destinatário, conteúdo mínimo, SLA, estado, motivo, eventos | Escrita por papel | Handoff idempotente por registro+destinatário+ação; reenvio = novo evento com motivo | Falha de acesso → estado seguro + retorno ao remetente (RN-F3-013) |
| Handoff → pipeline | Estado aceito/recusado/expirado | estado resultante, motivo, próxima ação | Escrita por papel | Aceite/recusa idempotentes por handoff_id | Expirado → escalonamento (RN-F3-011) |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-011 — SLA de aceite | Handoff pendente além do SLA | Escalar ao dono da matriz; pendência visível | Sem matriz nominal → dono provisório + pendência B3-RACI-01 | C-05 |
| RN-F3-012 — Sem resposta | Destinatário não responde | Manter pendência com dono e prazo; nunca encerrar por silêncio | — | §Fase 3 checklist |
| RN-F3-013 — Falha externa segura | Erro de acesso/canal ao registrar/aceitar | Estado seguro + registro do motivo + retorno ao remetente; sem retry automático | Retry manual = novo evento | EV-04, CA-2-12 |
| RN-F3-014 — Encerramento responsável | Recusar/expirar handoff | Voltar ao pipeline com motivo e próxima ação; ninguém encerra sem responsável | — | §Fase 3 regras |

## Fluxo e regras

1. Remetente registra handoff com conteúdo mínimo + SLA + destinatário da matriz.
2. Destinatário aceita (atualiza pipeline) ou recusa (motivo).
3. SLA vencido escala; sem resposta mantém pendência.
4. Falha de acesso registra motivo e retorna ao remetente com estado seguro.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | handoff aceito no SLA | pipeline atualizado; evento registrado | falha de acesso → estado seguro |
| Limite | sem resposta no SLA | escalonamento + pendência com dono | dono provisório se RACI pendente |
| Falha | erro de acesso/canal | motivo registrado; retorno ao remetente; sem retry cego | retry manual como novo evento |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** SPEC-F3-001, escopo §5 C-05 e §7 Fase 3; aprendizado AP-2026-09-23-1211 (herança de permissões OAuth) — não aplicável a conector aqui, mas registrar acessos.
2. **Alterar somente:** estrutura de handoff, superfície mínima, log de eventos.
3. **Não alterar:** pipeline/estados (F3-001); atribuição F2; disparo externo; permissões globais.
4. **Executar nesta ordem:** fixtures → registro → aceite/recusa → SLA/escalonamento → falha de acesso → recuperação.
5. **Parar e pedir validação quando:** pedirem disparo automático externo; faltar matriz RACI nominal para a prova; alguém quiser encerrar handoff sem responsável.
6. **Estado válido ao parar:** pipeline intacto; handoffs de teste removíveis; log íntegro.

## Checklist de execução

- [ ] Handoff com conteúdo mínimo, SLA, destinatário e estado rastreável.
- [ ] Sem aceite no SLA → escalonamento; sem resposta → pendência com dono.
- [ ] Falha de acesso → estado seguro + retorno, sem retry automático.
- [ ] Recusa/expiração → volta ao pipeline com motivo e próxima ação.
- [ ] Caminhos exercitados; bateria humana registrada; matriz RACI nominal anexada (ou pendência).

## Critérios de aceite

- [ ] **CA-3-06:** um handoff entre papéis é registrado com destinatário, conteúdo mínimo, SLA e estado, e seu aceite/recusa atualiza o pipeline de origem de forma idempotente.
- [ ] **CA-3-07:** handoff sem aceite no SLA escala ao dono definido e handoff sem resposta permanece como pendência visível com dono e prazo — nunca encerrado por silêncio.
- [ ] **CA-3-08:** falha de acesso/canal no handoff registra motivo, retorna o caso ao remetente em estado seguro e não executa retry automático; recusa/expiração volta ao pipeline com motivo.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | handoff sem destinatário/SLA; aceite duplicado; disparo automático | tentar operar | bloqueio/pendência; idempotência; disparo negado | log/captura |
| GREEN | handoff completo aceito no SLA | registrar → aceitar | pipeline atualizado; evento registrado | registro + captura |
| REFACTOR/REGRESSÃO | SLA vencido; sem resposta; falha de acesso; recusa/expiração | exercitar cenários | escalonamento, pendência, estado seguro, retorno com motivo | bateria + log |

**Dados/fixtures:** handoffs sintéticos entre papéis provisórios/nominais; sem contatos reais.
**Caminhos de erro obrigatórios:** SLA vencido; sem resposta; falha de acesso; aceite duplicado; recusa sem motivo.
**Evidência exigida:** log de eventos, capturas, bateria humana (EV-08), matriz RACI (ou pendência nomeada).

## Handoff e operação

- **Como demonstrar:** registrar→aceitar→escalar→falhar→recuperar um handoff na superfície.
- **Como operar depois:** gerentes registram; destinatários aceitam/recusam; direção revisa pendências.
- **Como monitorar:** handoffs expirados; pendências sem dono; recusas sem motivo.
- **Pendência conhecida:** B3-RACI-01 governa a prova; sem matriz nominal, CA-3-06..08 ficam pendentes.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T05 | Materializar registro de handoff com SLA, escalonamento e recuperação com massa sintética | Gerentes/comercial | F3-003 | CA-3-06 | Dados e integrações; Fluxo e regras; Checklist | Captura/export do registro e estados | F3-T01 aceita; papéis provisórios registrados | ☐ |
| F3-T06 | Provar aceite/recusa, SLA vencido, sem resposta e falha de acesso com matriz nominal | Gerentes + operação + direção | F3-003 | CA-3-06, CA-3-07, CA-3-08 | Critérios de aceite; TDD da SPEC | Bateria humana completa + matriz RACI anexa | F3-T05 aceita por teste humano; B3-RACI-01 fechado | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
