# AP-2026-09-21-1723 — Reconciliação segura de fallback manual

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T08 / SPEC F2-004
- Sinal: a prova manual sintética combinou um núcleo compartilhado de reconciliação com uma chave de lote separada da identidade da fonte e uma máquina explícita de retorno seguro.
- Evidência: `src/lib/f2/reconciliation/core.ts`, `src/lib/f2/t04/engine.ts`, `src/lib/f2/t08/manualBatch.ts`; T04 7/7; T08 8/8; bateria humana 5/5; `demandas` 10; migrations até 0020; nenhuma chamada externa.
- Regra reutilizável: em fallback manual, separar (1) núcleo de reconciliação por identidade da fonte, (2) `batch_id` para idempotência do lote e (3) estados de erro/fallback; replay idêntico deve ser skip e payload divergente do mesmo lote deve exigir decisão humana sem overwrite.
- Quando aplicar: fontes externas ainda sem acesso integrado validado, exports manuais e provas anteriores a uma integração real.
- Quando não aplicar: quando houver identidade multi-fonte aprovada e integração real autorizada; nesse caso o contrato de chave e o tratamento de erros exigem nova decisão.
- Confiança: alta — TDD, QA e cinco testes humanos confirmaram o comportamento.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto.
