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
- **Não existe nenhum usuário somente leitura** (Analyst / "Visualizar desempenho" + "Acessar relatórios") na conta.

### Riscos de governança registrados (não bloqueiam a T09)

1. Agência externa (AYPLA DIGITAL) com poder de escrita na conta de anúncios.
2. Perfil inativo ainda com controle total do portfólio.
3. Dois perfis externos com controle total do portfólio.

### Por que o gate 2 NÃO fechou

A SPEC F2-004 exige **permissão mínima de leitura** para o modo integrado. Hoje só existem acessos de controle total (escrita). Usar a conta de acesso total do owner como via de leitura fere o princípio do privilégio mínimo e comprometeria o rollback (revogação limpa).

### Ponto de parada aplicado

Conforme a SPEC ("parar e pedir validação quando for necessário conceder permissão"), a decisão de como fornecer o acesso de leitura mínima é do owner, que a executaria no Meta. Nenhuma permissão foi alterada; nenhuma conexão ou chamada foi feita.

## Próximo passo

Owner decide o caminho do acesso de leitura mínima (atribuir papel Analyst a uma pessoa existente, criar usuário dedicado somente leitura, ou outro que definir). Depois de executada a alteração no Meta, nova captura fecha o gate 2.
