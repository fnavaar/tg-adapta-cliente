# AP-2026-09-21-0901 — Fechamento de task de prova sem duplicar produto

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T06 / SPEC F2-003
- Sinal: a F2-T06 compartilha os critérios CA-2-07/08/09 com a implementação da F2-T05; a execução correta foi revalidar o backend e as evidências em leitura, sem recriar telas, regras ou dados.
- Evidência: relatório `05_entregas/fase-2/f2-t06/relatorio-fechamento.md`; consulta somente leitura da collection `decisoes_f2`; cadeia `DEC-F2-004 → DEC-F2-002`; TDD da T05 6/6; autorização expressa do Champion.
- Regra reutilizável: quando uma task posterior é de prova/aceite sobre uma capacidade já homologada, separar claramente implementação de revalidação, usar o estado vivo como fonte de verdade e não repetir testes com mutação.
- Quando aplicar: tasks documentais ou de aceite que reutilizam critérios e evidências de uma task técnica anterior.
- Quando não aplicar: quando a task exigir capacidade nova, correção funcional ou evidência ainda inexistente.
- Confiança: alta — escopo autorizado, backend consultado e nenhum produto alterado.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
