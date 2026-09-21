# AP-2026-09-21-0830 — Reenvio de migration no Skip após apply com build falho

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T05 / SPEC F2-003
- Sinal: migration persistida em um apply cujo build falhou (v0.0.70) não foi reenviada ao backend no apply seguinte (v0.0.71, QA verde) sem alteração no arquivo; só subiu após edição mínima no próprio arquivo (v0.0.72)
- Evidência: sequência v0.0.70/71/72 — `skip_cloud_list_migrations` sem a 0020 e collection ausente até o apply pós-edição, apesar de QA verde na v0.0.71
- Regra reutilizável: após qualquer apply com build falho que contenha migration nova, editar minimamente o arquivo da migration (ex.: comentário de controle) antes do próximo apply e conferir `skip_cloud_list_migrations` + `skip_cloud_get_collections` antes de validar o produto
- Quando aplicar: todo apply do Skip que carregue migration nova e falhe em qualquer estágio do QA
- Quando não aplicar: applies verdes na primeira tentativa; migrations já aplicadas são imutáveis
- Confiança: alta — observado em três applies consecutivos com verificação de backend
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
