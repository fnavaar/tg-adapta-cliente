# SPEC-F3-004 — Sinais de conta do DHO separados e com acesso restrito

**Fase:** 3
**Status:** planejada
**Dono:** DHO alimenta somente campos autorizados; direção aprova a lista; consultor valida o isolamento
**Origem no escopo:** Fase 3; C-06; DC-005; DC-006; RQ-009; G-003
**Degrau da solução:** construção mínima — objeto separado de sinal de conta com acesso restrito e encaminhamento humano; sem ingestão de dado sensível além dos sinais autorizados.

## Contexto e decisões fechadas

- **Estado atual:** não existe registro de sinais de conta do DHO no sistema. O escopo define C-06 como capacidade da F3 "se usada": registrar somente sinais explicitamente autorizados, separados da saúde da conta e com encaminhamento humano.
- **Estado desejado:** se a direção decidir usar C-06 na F3, existe um objeto `sinal-de-conta` separado da oportunidade e da saúde da conta, com lista fechada de sinais autorizados, acesso restrito por papel e encaminhamento humano registrado; se a direção decidir não usar, a capacidade fica formalmente inativa com a decisão registrada.
- **Decisões já fechadas:** DHO não assume venda; saúde da conta não vira ação comercial automática; sem governança (G-003/DC-006) não há uso de dado sensível; o sinal é objeto separado da oportunidade (escopo §Fase 3 regras).
- **Bloqueios:** B3-DHO-01 — lista nominal de sinais autorizados + política de acesso restrito aprovada pela direção/DHO antes de qualquer registro real de sinal. Sem a lista, a SPEC materializa a estrutura vazia e inativa (fail-closed), e a prova usa somente fixtures sintéticos.

## Resultado observável

1. Objeto `sinal-de-conta` separado: nenhum campo de sinal aparece na oportunidade, no pipeline ou no dashboard comercial; a relação é por conta/empresa com encaminhamento humano registrado.
2. Lista fechada de sinais autorizados versionada; sinal fora da lista é recusado com registro.
3. Acesso restrito: somente papel DHO escreve; leitura restrita ao papel aprovado; comercial não vê o conteúdo do sinal — vê somente o encaminhamento humano decidido.
4. Encaminhamento humano: cada sinal vira, no máximo, uma sugestão de próxima ação para uma pessoa decidir; nenhuma ação comercial parte do sinal sem decisão humana registrada.

## Limites e dependências

- **Inclui:** estrutura do objeto; lista versionada; permissões server-side; encaminhamento humano; prova de isolamento.
- **Fora de escopo:** ingestão de saúde da conta integral; dado sensível além dos sinais autorizados; decisão comercial automática; integração externa; scraping; obrigação de venda para o DHO.
- **Entradas e pré-condições:** B3-DHO-01 (lista + política) para qualquer dado real; sem ele, somente fixtures e estrutura inativa.
- **Saídas/artefatos:** objeto + permissões; evidência `sinal-dho-f3.md`; decisão de uso/não-uso registrada.
- **Dependências e responsáveis:** direção decide usar/não usar; DHO alimenta; consultor valida isolamento.
- **Atores e permissões mínimas:** escrita DHO; leitura papel aprovado; comercial sem acesso ao conteúdo.
- **Superfícies/arquivos/configurações afetadas:** nova coleção/objeto separado; permissões server-side; nenhuma superfície comercial.
- **Risco e plano B:** pressão para "colar" o sinal no CRM comercial → recusar e registrar; lista não aprovada → estrutura inativa fail-closed.
- **Rollback ou reversão:** desativar o objeto mantendo registros; nada sensível é exposto; decisão de não-uso registrada.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| DHO → sinal-de-conta | Lista autorizada versionada | conta/empresa, sinal autorizado, data, observação permitida, encaminhamento | Escrita DHO; leitura papel aprovado | Sinal idempotente por conta+sinal+data; duplicata recusada | Sinal fora da lista → recusa registrada (RN-F3-015) |
| Sinal → encaminhamento humano | Decisão registrada | próxima ação sugerida, decisor, decisão | Leitura restrita; decisão humana | Encaminhamento idempotente | Sem decisor → pendência, nunca ação automática |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-015 — Lista fechada | Sinal fora da lista autorizada | Recusar e registrar | Nova categoria exige aprovação e nova versão da lista | C-06 |
| RN-F3-016 — Isolamento | Qualquer leitura comercial | Sinal nunca aparece em pipeline/dashboard comercial; somente encaminhamento decidido | — | §Fase 3 regras |
| RN-F3-017 — Encaminhamento humano | Sinal existe | No máximo sugestão com decisor; sem decisão registrada, pendência | — | DC-005, C-06 |
| RN-F3-018 — Fail-closed sem política | B3-DHO-01 aberto | Objeto inativo; somente fixtures; dado real recusado | Política aprovada → ativação por emenda | DC-006, G-003 |

## Fluxo e regras

1. Direção registra decisão de usar/não usar C-06 na F3.
2. Se usar: DHO registra sinal da lista autorizada; sistema valida lista e duplicata.
3. Encaminhamento humano com decisor; pendência sem decisor.
4. Prova de isolamento: tentar ler sinal pelo papel comercial → recusado.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | sinal autorizado + encaminhamento decidido | registro isolado + ação humana | — |
| Limite | lista não aprovada | objeto inativo; fixtures somente | política → ativação |
| Falha | sinal fora da lista; leitura comercial; duplicata | recusa/pendência registrada | aprovação nova versão |

## Instruções de execução para o Ethos

1. **Ler antes de alterar:** escopo §5 C-06, §7 Fase 3, DC-005/DC-006, G-003; SPEC-F3-001 (para o que NÃO pode ser tocado).
2. **Alterar somente:** objeto separado, permissões server-side, lista versionada.
3. **Não alterar:** pipeline/oportunidades/dashboard comercial (F3-001/002); atribuição F2; dado sensível.
4. **Executar nesta ordem:** decisão de uso → estrutura + permissões → fixtures → prova de isolamento → encaminhamento.
5. **Parar e pedir validação quando:** pedirem sinal fora da lista, exposição ao comercial, dado real sem política (B3-DHO-01), ou ação comercial automática.
6. **Estado válido ao parar:** objeto inativo ou isolado; nada sensível exposto; decisão registrada.

## Checklist de execução

- [ ] Decisão de usar/não usar C-06 registrada pela direção.
- [ ] Objeto separado com permissões server-side; leitura comercial recusada (prova negativa).
- [ ] Lista fechada versionada; sinal fora da lista recusado.
- [ ] Encaminhamento sempre humano com decisor; pendência sem decisor.
- [ ] Se B3-DHO-01 aberto: somente fixtures, objeto inativo, dado real recusado.

## Critérios de aceite

- [ ] **CA-3-09:** o sinal de conta do DHO, se usado, está em objeto separado da oportunidade/saúde da conta, com lista fechada versionada e acesso restrito — provado por leitura negativa do papel comercial.
- [ ] **CA-3-10:** nenhum sinal gera ação comercial sem decisão humana registrada; sem lista/política aprovada (B3-DHO-01), o objeto permanece inativo e recusa dado real (fail-closed).

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | sinal fora da lista; leitura pelo papel comercial; dado real sem política | tentar operar | recusa registrada; acesso negado; fail-closed | log/captura |
| GREEN | sinal autorizado + encaminhamento humano (fixture) | registrar → encaminhar | isolamento + decisão humana visíveis | registro + captura |
| REFACTOR/REGRESSÃO | duplicata; pipeline/dashboard comercial sem sinal; rollback do objeto | verificar | sem vazamento; sem duplicata; reversível | bateria + captura |

**Dados/fixtures:** sinais sintéticos de uma lista provisória claramente marcada como fixture; sem dado real de cliente.
**Caminhos de erro obrigatórios:** sinal fora da lista; leitura comercial; duplicata; dado real sem política.
**Evidência exigida:** prova negativa de acesso, lista versionada, decisão de uso, bateria humana (EV-08).

## Handoff e operação

- **Como demonstrar:** registrar um sinal fixture, tentar lê-lo como comercial (negado) e mostrar o encaminhamento humano.
- **Como operar depois:** DHO alimenta a lista aprovada; direção revisa encaminhamentos.
- **Como monitorar:** sinais recusados; pendências sem decisor; tentativas de leitura indevida.
- **Pendência conhecida:** B3-DHO-01 governa ativação; sem política, permanece inativo.

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T07 | Materializar objeto separado de sinal de conta com lista versionada e permissões (fail-closed) | DHO + direção | F3-004 | CA-3-09 | Dados e integrações; Fluxo e regras; Checklist | Captura do objeto inativo + prova negativa de acesso | F3-T01 aceita; decisão de uso registrada | ☐ |
| F3-T08 | Provar isolamento, lista fechada, encaminhamento humano e fail-closed sem política | DHO + direção + consultor | F3-004 | CA-3-09, CA-3-10 | Critérios de aceite; TDD da SPEC | Bateria humana com prova negativa + lista versionada | F3-T07 aceita por teste humano | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
