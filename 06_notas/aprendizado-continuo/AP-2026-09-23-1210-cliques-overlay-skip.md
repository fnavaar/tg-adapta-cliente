# AP-2026-09-23-1210 — Cliques em botões abaixo da dobra caem no overlay do Skip

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T09 (SPEC F2-004); padrão já observado na F2-T02 (dialogs) e T08
- Sinal: Em páginas longas do Skip, cliques automatizados (agent-browser) em botões fora da área visível não disparam o handler — a prova T09 não executava e o clique retornava sucesso. Rolar o botão para o viewport (`scrollIntoView({block:'center'})`) antes do clique resolveu.
- Evidência: Preview /atribuicao-t04 em 23/09/2026 — dois cliques via ref sem efeito (`placeholder` persistia); após scrollIntoView + click, prova executou e retornou PASSOU 10/10.
- Regra reutilizável: Em qualquer validação automatizada no Skip, rolar o elemento para o centro do viewport antes de clicar; desconfiar de clique "bem-sucedido" sem mudança observável de estado.
- Quando aplicar: Provas humanas/automatizadas em superfícies Skip com scroll (páginas longas, dialogs, seções abaixo da dobra).
- Quando não aplicar: Elementos já visíveis no snapshot com viewport pequeno; cliques via teclado/enter em formulários.
- Confiança: alta — padrão reproduzido 2× no projeto (T02 dialogs, T09 página longa) com causa e correção observadas.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
