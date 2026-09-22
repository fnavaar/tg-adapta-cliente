# F2-T09 — Checkpoint de elegibilidade — 2026-09-22

## Gate 1 — Identificação dos ativos Meta — VALIDADO (declaração do owner)

- **Portfólio empresarial:** `talentgroup.br`.
- **ID do portfólio empresarial:** `954962358469228`.
- **Conta de anúncios:** `TalentGroup_01`.
- **ID da conta de anúncios:** `1667348577717128`.
- Validação formal: campos completos, numéricos e associados aos nomes. Sem segredo, sem conexão, sem chamada.

## Gate 2 — Owner nominal e acesso de leitura — EM ANDAMENTO

### Comprovado por capturas do owner (2026-09-22, 10:22 e 10:27)

**Nível do portfólio `talentgroup.br`:**
- **Owner nominal com controle total:** João Paulo Oliveira — sessão ativa em 2026-09-22; consistente com o Champion do projeto.
- Observações de governança: dois perfis externos (parceiros/agências) com controle total do portfólio (um com expiração em 8 dias); um perfil interno com acesso parcial; um perfil inativo com controle total.

**Nível da conta de anúncios `TalentGroup_01`:**
- **2 pessoas atribuídas**, ambas com **acesso total**:
  - João Paulo Oliveira — acesso total (owner nominal confirmado também neste nível).
  - AYPLA DIGITAL — acesso total (agência/parceiro externo).
- **Não existe nenhum usuário somente leitura** (Analyst / "Ver desempenho") na conta.

### Riscos de governança registrados (não bloqueiam a T09)

1. Agência externa (AYPLA DIGITAL) com poder de escrita na conta de anúncios.
2. Perfil inativo ainda com controle total do portfólio.
3. Dois perfis externos com controle total do portfólio.

### Por que o gate 2 NÃO fechou

A SPEC F2-004 exige **permissão mínima de leitura** para o modo integrado. Hoje só existem acessos de controle total (escrita). Usar a conta de acesso total do owner como via de leitura fere o princípio do privilégio mínimo e comprometeria o rollback (revogação limpa).

### Decisão do owner — 2026-09-22, 10:32

- **Caminho escolhido:** opção 1 — criar/usar um usuário dedicado somente leitura.
- **Objetivo:** atribuir à pessoa dedicada apenas a permissão mínima necessária para visualizar anúncios e acessar relatórios da conta `TalentGroup_01`.
- **Escopo da decisão:** governança de acesso; não autoriza conexão, chamada, leitura real, implementação ou uso de credencial pelo assistente.

### Execução pelo owner — convite enviado (2026-09-22, 10:50)

Comprovado por nova captura do owner (tela Configurações → Pessoas do portfólio):

- **Convite enviado** pelo owner (João Paulo Oliveira) ao **e-mail dedicado do leitor** — e-mail não transcrito nesta evidência por conter dado pessoal; visível apenas no Meta.
- **Atribuição configurada** na conta `TalentGroup_01` com somente a permissão **"Ver desempenho"** (captura de 10:44: gerenciar campanhas, modelos do Creative Hub e acesso total desligados).
- **Estado no Meta:** convite **pendente de aceite** (validade de 30 dias); seção "Ativos de negócios (pendente)" indica que a atribuição do ativo aguarda ativação.
- **Consistência verificada:** a captura exibe `business_id=954962358469228` — mesmo portfólio declarado no gate 1.
- Nenhuma permissão existente foi alterada; nenhuma conexão ou chamada foi feita.

### Por que o gate 2 segue EM ANDAMENTO

A configuração está correta, mas o acesso ainda não está ativo: o convite não foi aceito e a atribuição do ativo consta como pendente. O gate fecha com a prova final do estado ativo.

## Próximo passo

1. O leitor dedicado **aceitar o convite** recebido por e-mail.
2. O owner confirmar no Meta que a atribuição da conta `TalentGroup_01` saiu de pendente para ativa.
3. O owner enviar captura da **lista de pessoas da conta `TalentGroup_01`** mostrando o leitor dedicado com acesso parcial (somente "Ver desempenho"), sem e-mails ou dados pessoais.

Com essa evidência, o gate 2 é fechado e seguimos ao próximo requisito (contrato de campos/payload autorizado e política de dados). A T09 permanece bloqueada.
