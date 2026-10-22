# SPEC-F3-005 — Funil visual (Kanban) com origem e jornada de cada demanda

**Fase:** 3
**Status:** planejada
**Criada em:** 2026-10-22 (evolução EV-5C-01, decisão P1)
**Dono:** comercial/gerentes operam; marketing e direção leem; consultor valida a primeira demonstração
**Origem no escopo:** §12.2 C-04a; C-03; C-04; DC-002; DC-004
**Degrau da solução:** reuso — visão nova sobre `demandas`, `propostas`, `vagas`, log de transições e atribuição F2 já existentes; sem coleção nova, sem conector, sem estado novo.

## Em linguagem simples

**O que você vai ver:** uma tela **"Funil"** no Skip, em colunas, igual a um quadro de tarefas. Cada
coluna é uma etapa (suspect, prospect, lead qualificado, oportunidade, proposta, vaga aberta e
encerrados). Cada cartão é uma empresa/demanda e mostra **de onde veio** (inbound ou outbound, canal,
campanha), **o que ela quer** (R&S, TMO ou os dois), a área, quem é o dono e qual é a próxima ação.
Clicando no cartão você vê a **história completa**: por quais etapas passou, quando, quem moveu, quais
propostas e vagas nasceram dele e de qual campanha ele veio.

**Onde executar:** Maestro, com o conector Skip apontando para o projeto **"repositório adapta"**.

## Contexto e decisões fechadas

- **Estado atual:** a F1 entregou o pipeline com estados e painel de contagens; a F3-T01 está criando
  propostas, vagas, retorno e o campo `origem_dado`. Não existe tela em que se veja cada demanda na sua
  etapa nem a jornada dela. Na 5ª call (22/10) o cliente disse que esta é a principal coisa que falta.
- **Estado desejado:** qualquer pessoa autorizada abre o Funil, entende onde cada demanda está e de onde
  veio, e consegue mover um cartão de etapa pelo mesmo caminho de transição já existente.
- **Decisões já fechadas:** a taxonomia de estados da F1 não muda; mover um cartão é uma transição comum
  e exige evidência (RN-F1-007); origem ausente aparece como `desconhecido` (RN-F3-005); contagens vêm
  da fonte (RN-F3-006); dado sintético aparece com selo TESTE (decisão de 21/10).
- **Bloqueios:** B3-LGPD-01 — dado real de contato só aparece após política aprovada; B3-MET-01 — a
  coluna "lead qualificado" existe, mas a regra de qualificação segue pendente de G-001 (o cartão só
  entra nela por transição manual com evidência, como hoje).

## Resultado observável

1. Tela Funil com uma coluna por estado ativo e uma coluna "Encerrados" (ganho, perdido, sem timing,
   desqualificado), com a contagem no topo de cada coluna.
2. Cartão com: empresa, tipo (inbound/outbound), canal, campanha, serviço de interesse, área, dono,
   próxima ação com prazo (vencido em destaque), número de propostas/vagas e selo TESTE quando
   `origem_dado = sintetico`.
3. Painel do cartão ("Jornada") com a linha do tempo do log de transições, as propostas/vagas ligadas e
   a campanha de origem.
4. Filtros: período, inbound/outbound, canal, campanha, serviço, dono e "incluir dados de teste".
5. Arrastar o cartão abre o formulário de transição; sem evidência o cartão volta e aparece o motivo.

## Limites e dependências

- **Inclui:** página Funil; cartão; painel Jornada; filtros; arrastar = transição com evidência.
- **Fora de escopo:** coleção ou estado novo; regra automática de qualificação; RD Station, 1CRM, Omie;
  leitura direta da Meta (é da F3-006); envio de mensagem a contato; exibição de e-mail/telefone no
  cartão.
- **Entradas e pré-condições:** F3-T01 aceita por teste humano (propostas, vagas, retorno e
  `origem_dado` existem); fixtures sintéticos inbound/outbound/parado da F3-T01.
- **Saídas/artefatos:** página Funil no projeto "repositório adapta"; evidência `funil-f3.md` em
  `05_entregas/fase-3/`.
- **Dependências e responsáveis:** comercial move cartões; marketing confere origem; direção lê;
  consultor revisa a primeira demonstração.
- **Atores e permissões mínimas:** direção e marketing leem todos os cartões; gerentes leem todos e movem
  os seus; operação lê; nada do DHO aparece no Funil (F3-004 fica separado).
- **Superfícies/arquivos/configurações afetadas:** nova página/rota `funil` no app; consultas de leitura;
  nenhuma migration; nenhum hook de escrita externa.
- **Risco e plano B:** muitas demandas sem origem → coluna mostra `desconhecido` e um contador de "sem
  origem" no topo; tela lenta com muitos cartões → paginação por coluna (20 cartões + "ver mais").
- **Rollback ou reversão:** esconder a rota `funil`; dados, estados e log ficam intactos.

## Dados e integrações

| Origem/destino | Fonte de verdade | Campos/contrato | Autenticação/permissão | Timeout/retry/idempotência | Tratamento de erro |
|---|---|---|---|---|---|
| `demandas` → cartão | registro da demanda | `record_id`, empresa, tipo, canal, campanha_id, oferta_servico, área, estado, dono, próxima ação, prazo, `origem_dado` | leitura por papel | consulta de leitura; sem cache divergente | campo ausente → `desconhecido`/"Não informado" |
| atribuição F2 → campanha do cartão | F2-002 (fonte única) | `sistema_origem_tecnico`, campanha/experimento_id, nome da campanha | leitura | ligação por identidade da fonte (B3-ID-01) | sem ligação → campanha `desconhecida` |
| `propostas`/`vagas` → cartão e Jornada | coleções da F3-T01 | `demanda_id`, nº, serviço, área, prazo operacional (vaga), resultado | leitura | contagem pela fonte | filho órfão não aparece; registra pendência |
| log de transições → Jornada | log append-only | data, de→para, quem, evidência | leitura | ordem cronológica | log ausente → aviso "histórico indisponível" |
| arrastar cartão → transição | fluxo de transição F1/F3-001 | estado destino + evidência | escrita do dono/gerente | idempotente por `record_id` + versão | sem evidência ou sem permissão → recusa, cartão volta |

| Regra de negócio | Condição | Ação/resultado | Exceção | Fonte |
|---|---|---|---|---|
| RN-F3-020 — Funil é visão, não pipeline novo | qualquer uso | coluna = estado F1 existente; cartão = demanda | proposta/vaga não vira cartão próprio | E-F3-001-01, P1 |
| RN-F3-021 — Mover = transição | arrastar cartão | abre transição com evidência obrigatória | sem evidência → recusa registrada | RN-F1-007 |
| RN-F3-022 — Origem sempre visível | cartão sem tipo/canal/campanha | exibir `desconhecido` | — | RN-F3-005 |
| RN-F3-023 — Teste marcado | `origem_dado = sintetico` | selo TESTE; fora por padrão nos indicadores oficiais | filtro "incluir dados de teste" mostra | decisão 21/10 |
| RN-F3-024 — Sem dado de contato no cartão | sempre | cartão não exibe e-mail/telefone | detalhe só com permissão e após B3-LGPD-01 | B3-LGPD-01 |

## Fluxo e regras

1. Ler demandas, propostas, vagas, log e atribuição pela fonte.
2. Montar colunas por estado e cartões com os campos do contrato.
3. Aplicar filtros e o filtro de teste.
4. Ao abrir um cartão, montar a Jornada pelo log.
5. Ao arrastar, chamar a transição existente; sucesso move o cartão e grava no log; falha devolve.

| Cenário | Dado/condição | Resultado esperado | Caminho de erro/recuperação |
|---|---|---|---|
| Principal | fixtures inbound e outbound da F3-T01 | cartões nas colunas certas, com origem, serviço, dono e jornada | divergência de contagem → pendência |
| Limite | demanda sem campanha/canal | cartão com `desconhecido` e contador "sem origem" | — |
| Falha | arrastar sem evidência ou sem permissão | cartão volta; motivo visível; log registra a recusa | refazer com evidência |

## Instruções de execução para o Maestro (antigo Ethos)

1. **Ler antes de alterar:** SPEC-F3-001 (estados, E-F3-001-01/02), SPEC-F2-002 (atribuição),
   SPEC-F1-002 (painel), §12 do escopo.
2. **Alterar somente:** nova página `funil` e suas consultas de leitura, no projeto "repositório adapta".
3. **Não alterar:** estados, transições, `demandas`, `propostas`, `vagas`, atribuição, conectores,
   permissões globais e o painel F1/F2.
4. **Executar nesta ordem:** colunas e contagens → cartão → filtros → Jornada → arrastar com transição.
5. **Explicar antes de começar:** dizer ao Champion, em linguagem simples, o que esta etapa vai mostrar
   na tela.
6. **Parar e pedir validação quando:** precisar de campo que não existe; pedirem regra automática de
   qualificação; pedirem exibir dado de contato real; qualquer escrita externa.
7. **Estado válido ao parar:** rota `funil` desativável; nenhum dado alterado fora de transições válidas.

## Checklist de execução

- [ ] Colunas por estado com contagens iguais à fonte.
- [ ] Cartão com origem, campanha, serviço, área, dono, próxima ação/prazo e selo TESTE.
- [ ] Jornada com linha do tempo, propostas/vagas e campanha.
- [ ] Filtros funcionando, incluindo "incluir dados de teste".
- [ ] Arrastar sem evidência é recusado; com evidência move e grava no log.

## Critérios de aceite

- [ ] **CA-3-13:** o Funil mostra cada demanda na coluna do seu estado com tipo, canal, campanha, serviço,
  área, dono e próxima ação/prazo; contagens iguais à fonte; `desconhecido` e selo TESTE visíveis.
- [ ] **CA-3-14:** ao abrir um cartão, a Jornada mostra todas as transições do log, as propostas/vagas
  ligadas e a campanha de origem; arrastar sem evidência é recusado e com evidência gera transição
  registrada.

## TDD da SPEC

| Etapa | Prova | Comando/ação | Resultado esperado | Evidência |
|---|---|---|---|---|
| RED | cartão sem origem exibido em branco; arrastar sem evidência move o cartão; contagem da coluna diferente da fonte | abrir Funil e tentar | `desconhecido` exibido; recusa registrada; contagem = fonte | captura + log |
| GREEN | fixtures `PIPE-F3-IN-001`, `PIPE-F3-OUT-001`, `PIPE-F3-STUCK-001` | abrir Funil, filtrar, abrir Jornada, mover com evidência | CA-3-13 e CA-3-14 demonstráveis | capturas + log |
| REFACTOR/REGRESSÃO | recarregar; mover e desfazer pelo fluxo normal; abrir painel F1/F2 | replay + comparação | sem duplicação; painel anterior intacto | comparação fonte×tela |

**Dados/fixtures:** fixtures sintéticos da F3-T01; nenhum contato real.
**Caminhos de erro obrigatórios:** origem ausente; arrastar sem evidência; arrastar sem permissão; log ausente.
**Evidência exigida:** capturas do Funil e da Jornada, comparação fonte×tela, teste humano do Champion.

## Handoff e operação

- **Como demonstrar:** abrir o Funil, mostrar de onde veio cada cartão, abrir a Jornada de um caso
  inbound e de um outbound, mover um cartão com evidência.
- **Como operar depois:** comercial mantém os cartões em dia; direção abre o Funil na reunião semanal.
- **Como monitorar:** contador "sem origem"; cartões com prazo vencido; divergência fonte×tela.
- **Pendência conhecida:** B3-LGPD-01 (dado real) e B3-MET-01 (lead qualificado).

## Tasks vinculadas

| ID | Task | Dono | SPEC | Critério | Recorte da prova | Evidência esperada | Pré-condições | Status |
|---|---|---|---|---|---|---|---|---|
| F3-T10 | Construir a tela Funil (Kanban) com cartões, origem, filtros e Jornada usando os dados de teste | João Paulo | F3-005 | CA-3-13 | Dados e integrações; Fluxo e regras; Checklist | Capturas do Funil e da Jornada + comparação fonte×tela | F3-T01 aceita | ☐ |
| F3-T11 | Provar o Funil: origem desconhecida, arrastar sem evidência, contagens e regressão do painel | João Paulo | F3-005 | CA-3-13, CA-3-14 | Critérios de aceite; TDD da SPEC | Bateria humana + log + comparação | F3-T10 aceita por teste humano | ☐ |

## Emendas

| Data | Origem do sinal | Micro-spec/task | Motivo |
|---|---|---|---|
