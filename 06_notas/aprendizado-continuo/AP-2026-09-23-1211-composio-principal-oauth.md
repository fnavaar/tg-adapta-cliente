# AP-2026-09-23-1211 — Conexão OAuth via Composio herda permissões de quem consente

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T09 (SPEC F2-004); gates 1–5 e decisão do leitor dedicado (gate 2)
- Sinal: O toolkit `metaads` do runtime é servido pelo Composio; a connected account criada pelo consentimento OAuth herda as permissões Meta de QUEM concluiu o fluxo — não de quem planejou o acesso. A conexão de 23/09 ficou com principal "João Paulo Oliveira" (controle total) em vez do leitor dedicado somente leitura decidido no gate 2. Alterar escopos no auth config só afeta conexões NOVAS.
- Evidência: `mcp_metaads_metaads_get_user` retornou João Paulo Oliveira (23/09); documentação Composio (docs.composio.dev — connected accounts, controlling scopes); erro "No connected account" de 22/09 resolvido sem troca de principal.
- Regra reutilizável: Para acesso mínimo real em integrações OAuth, o usuário de menor permissão deve concluir ele próprio o Connect Link; registrar o principal efetivo como evidência de gate antes de usar a conexão.
- Quando aplicar: Qualquer task futura que conecte toolkits via OAuth (Meta, RD Station, 1CRM) com exigência de permissão mínima.
- Quando não aplicar: Conexões via API key de system user com escopo próprio (o segredo nunca trafega pelo chat).
- Confiança: média — comportamento confirmado na prática e na documentação oficial; a regularização do leitor dedicado ainda é pendência aberta do owner.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
