# F2-T09 — Checkpoint de elegibilidade — 2026-09-22

## Gate 1 — Identificação dos ativos Meta — VALIDADO (declaração do owner)

- **Portfólio empresarial:** `talentgroup.br`.
- **ID do portfólio empresarial:** `954962358469228`.
- **Conta de anúncios:** `TalentGroup_01`.
- **ID da conta de anúncios:** `1667348577717128`.
- Validação formal: campos completos, numéricos e associados aos nomes. Sem segredo, sem conexão, sem chamada.

## Gate 2 — Owner nominal e acesso de leitura — VALIDADO (2026-09-22, 10:56)

### Trajetória da validação

1. Capturas de 10:22 e 10:27: owner nominal com controle total no portfólio e na conta (João Paulo Oliveira); conta `TalentGroup_01` com 2 acessos, ambos de controle total (João Paulo Oliveira e AYPLA DIGITAL), sem usuário somente leitura.
2. Decisão do owner (10:32): opção 1 — usuário dedicado somente leitura.
3. Execução do owner (10:44/10:50): convite enviado ao leitor dedicado; atribuição na `TalentGroup_01` configurada somente com "Ver desempenho" (gerenciar campanhas, modelos do Creative Hub e acesso total desligados); convite pendente de aceite.
4. Captura final (10:56): convite ACEITO e acesso ATIVO.

### Estado comprovado na captura final (10:56)

- **Leitor nominal dedicado:** Luiz Carlos Manni — ativo, online pela última vez em 22/09/2026 (convite aceito).
- **Conta de anúncios `TalentGroup_01`:** **Acesso parcial (Ver desempenho)** — ATIVO, sem pendência.
- **Consistência:** mesmo portfólio `talentgroup.br` (`954962358469228`) dos gates anteriores.
- Nenhum e-mail ou dado pessoal foi transcrito nesta evidência.
- Nenhuma permissão preexistente foi alterada; nenhuma conexão ou chamada foi feita.

### Observações de governança registradas (não bloqueiam)

1. O leitor dedicado também possui **controle total do portfólio** (pode gerenciar configurações, pessoas e ativos e excluir o portfólio). O acesso à conta de anúncios — superfície da prova T09 — é somente leitura; o controle do portfólio não altera a natureza somente leitura do acesso à conta, mas fica registrado para o rollback (a revogação limpa é do acesso parcial da conta).
2. Agência externa (AYPLA DIGITAL) com poder de escrita na conta de anúncios.
3. Perfil inativo ainda com controle total do portfólio.
4. Dois perfis externos com controle total do portfólio (um com expiração em 8 dias a partir de 22/09).

## Gate 3 — Contrato de campos autorizados e política de dados — VALIDADO (2026-09-22, 11:02)

### Aprovação do owner

- **Decisão:** `Aprovo como proposto`.
- **Escopo:** aprovação do contrato de leitura e da política de dados; não autoriza conexão, chamada real, implementação, publicação, alteração de orçamento ou uso de segredo.

### Campos autorizados para leitura

1. Identificador e nome de campanha, conjunto de anúncios e anúncio, quando disponíveis.
2. Período.
3. Origem/canal declarado.
4. Impressões.
5. Cliques.
6. Custo (`spend`), somente como leitura.

### Campos e ações proibidos

- contatos, leads e dados pessoais;
- conteúdo de formulários;
- criativos não públicos;
- qualquer escrita em campanha, orçamento ou criativo.

### Política aprovada

- Campo fora do contrato: descartar e registrar, sem inferência (RN-F2-012).
- Erro 401/403/429, timeout ou payload inválido: interromper o modo integrado, registrar o erro e não fazer retry cego (RN-F2-013).
- Rollback documentado, preservando logs e evidências.
- Nenhuma leitura real ou chamada Meta foi realizada neste gate.

## Gate 4 — Chave de identidade e reconciliação — VALIDADO (2026-09-22, 11:13)

### Decisão do owner

- **Estratégia escolhida:** `sistema_origem_tecnico + record_id`.
- **Racional registrado:** manter cada identificador vinculado à fonte técnica; evitar colisões; preservar rastreabilidade; não inventar um `record_id` global.
- **Escopo:** decisão de governança/arquitetura; não cria campo, índice, chave física ou vínculo no banco e não autoriza implementação.

### Regra operacional para a futura prova

- A identidade deverá ser tratada como par `(sistema_origem_tecnico, record_id)`.
- A fonte Meta será identificada como sistema de origem somente quando a leitura autorizada for executada.
- Sem chave válida, o registro será marcado como não vinculado/desconhecido; não será deduplicado por inferência.
- A agregação entre fontes técnicas só poderá ocorrer respeitando esse par e o contrato aprovado.

## Gate 5 — Payload autorizado — VALIDADO (2026-09-22, 11:20)

### Aprovação do owner

- **Decisão:** `Aprovo o payload como está`.
- **Natureza:** aprovação de um contrato sintético/anonimizado; não é evidência de resposta real do Meta.

### Limites confirmados

- Payload limitado aos campos aprovados no Gate 3.
- Identidade sintética no formato `(meta_ads, record_id)`.
- Sem leads, contatos, dados pessoais, formulários, criativos não públicos, tokens, segredos ou campos de escrita.
- Nenhuma conexão, chamada ou leitura real foi realizada.

## Reavaliação oficial da elegibilidade da F2-T09 — 2026-09-22, 11:20

### Pré-condições da task

- F2-T07: concluída e validada; `META-F2-001` e `fallback_manual` aprovados.
- F2-T08: concluída e validada; bateria humana 5/5; CA-2-10 e CA-2-12 no recorte simulado.
- F2-T04: reconciliação determinística, replay e proteção de escopo preservados.

### Matriz de elegibilidade

| Requisito | Evidência | Resultado |
|---|---|---|
| Conta/portfólio identificados | Gate 1; declaração não sensível do owner | **Atendido** |
| Owner nominal e acesso mínimo | Gate 2; leitor dedicado ativo com acesso parcial "Ver desempenho" na `TalentGroup_01` | **Atendido** |
| Contrato de campos e política de dados | Gate 3; aprovação sem ressalvas | **Atendido** |
| Chave de identidade/reconciliação | Gate 4; `sistema_origem_tecnico + record_id` | **Atendido** |
| Payload autorizado | Gate 5; payload sintético aprovado | **Atendido** |
| Autorização para implementação | Ainda não concedida | **Pendente — não é falha de elegibilidade** |

### Veredito

A F2-T09 está **elegível para implementação controlada**, mas **não está autorizada para implementação**. A task sai do bloqueio de elegibilidade e entra em `aguardando_autorizacao`.

Os critérios CA-2-11 e CA-2-12 no recorte real ainda não foram executados e continuam pendentes de implementação, leitura real autorizada e teste humano. Não há integração Meta validada até este momento.

## Plano de implementação para autorização

### 1. Escopo mínimo

- Reutilizar o núcleo determinístico de reconciliação T04/T08; não criar uma segunda engine.
- Criar somente o adapter de leitura Meta e o tratamento de resposta, mantendo o fallback manual disponível.
- Operar em modo somente leitura e dry-run; não escrever em `demandas`.
- Não criar leads, contatos, formulários, vínculo estrutural campanha→lead ou receita.
- Não criar nova collection, migration, campo, hook, RLS ou alteração de orçamento. Se isso se tornar necessário, parar e pedir nova decisão.

### 2. Consulta real limitada

- Usar a conta de anúncios já comprovada `TalentGroup_01` (`1667348577717128`).
- Fazer uma única consulta inicial, com período curto previamente registrado e somente os campos aprovados.
- Usar a superfície oficial de Insights da conta; endpoint, versão e disponibilidade de cada campo serão confirmados antes da chamada contra o contrato vigente da Meta.
- A consulta não poderá buscar leads, contatos, formulários, criativos não públicos ou permissões de escrita.
- Segredo/token, se tecnicamente necessário pelo conector aprovado, ficará fora do chat, GitHub e artefatos; não será solicitado pelo chat.

### 3. Normalização e identidade

- Registrar a origem técnica como `meta_ads` somente após a leitura autorizada.
- Usar o par `(meta_ads, record_id)`.
- Planejamento inicial: consultar no nível que retorne um identificador estável do objeto e usar esse ID como `record_id`; nunca usar nome de campanha como chave.
- Se o identificador aprovado não vier, marcar `não vinculado/desconhecido` e parar; não inferir, deduplicar ou substituir por outra chave.
- Preservar o payload bruto sanitizado e o relatório normalizado somente dentro da prova controlada, sem segredo ou dado pessoal.

### 4. Reconciliação

- Comparar resposta bruta autorizada × relatório normalizado.
- Conferir quantidade de linhas, unicidade do par de identidade, campos permitidos, campos ausentes, duplicidade e conflito.
- Registrar divergências e lacunas com estado explícito.
- Não interpretar impressão, clique ou `spend` como lead, qualidade comercial, oportunidade ou receita.
- Não afirmar atribuição ao pipeline F1, pois a relação estrutural `demandas` ↔ `experimentos_f2` não existe.

### 5. Erros e rollback

- 401/403/429, timeout ou payload/campo inválido: interromper, registrar e retornar a `fallback_manual`/`bloqueada`, sem retry cego.
- Não provocar rate limit, bloqueio de conta ou erro destrutivo deliberadamente.
- Se ocorrer erro real permitido durante a leitura, preservar status, resposta sanitizada e decisão de recuperação.
- Se nenhum erro real ocorrer, não inventar uma evidência; a cobertura simulada permanece a da T08.
- Ao fim da prova, o owner poderá revogar o acesso parcial da conta; logs e evidências permanecem preservados.

### 6. Verificações automatizáveis

1. Testes do parser/normalizador com o payload sintético aprovado.
2. Teste de rejeição de campos fora do contrato.
3. Teste da chave `(sistema_origem_tecnico, record_id)` e da ausência de chave.
4. Teste de duplicidade, conflito e replay sem escrita.
5. Teste de erro e retorno seguro, reutilizando a cobertura T08 e registrando qualquer erro real observado.
6. Build, análise estática e regressão das rotas/painel F1, T04 e T08.
7. Verificação viva de que `demandas`, collections e migrations não sofreram alteração.

### 7. Teste humano obrigatório

O Champion deverá confirmar:

- conta, período e campos consultados;
- somente leitura e ausência de escrita;
- quantidade e IDs reconciliados;
- campos proibidos ausentes;
- comportamento seguro diante de erro, se observado;
- fallback e rollback documentados;
- preservação do painel F1 e das provas T04/T08.

A task só poderá ser concluída após esse teste humano e a revalidação dos critérios CA-2-11 e CA-2-12.

## Estado após a reavaliação

- **Elegibilidade:** aprovada para implementação controlada.
- **Autorização de implementação:** ausente.
- **Estado operacional:** `aguardando_autorizacao`.
- **Próxima ação única:** aguardar autorização expressa do Champion para executar este plano.
