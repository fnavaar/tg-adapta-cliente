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

## Gate 4 — Chave de identidade e reconciliação — PENDENTE DE DECISÃO

A pendência arquitetural oficial da F1-T06 permanece aberta. Antes de qualquer integração efetiva com múltiplas fontes técnicas, é necessário aprovar uma estratégia de identidade:

- `record_id` global; ou
- `sistema_origem_tecnico + record_id`; ou
- outra chave explicitamente aprovada.

Até essa decisão:

- não deduplicar nem agregar fontes técnicas;
- não criar identidade global por inferência;
- não iniciar leitura real ou implementação da T09.

## Próximo gate após a decisão de identidade

**Gate 5 — payload autorizado:** apresentar exemplo sintético/anonimizado do retorno esperado, limitado aos campos aprovados, antes de qualquer leitura real.

Após os gates restantes, será feita a reavaliação oficial da elegibilidade da F2-T09 e apresentado o plano de implementação para autorização expressa do Champion.
