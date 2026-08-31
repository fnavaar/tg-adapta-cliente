# AP-2026-08-31-2200 — Hooks de validação em Skip Cloud: usar onRecordUpdate + e.oldRecord, não $app dentro de onRecordValidate

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F1-T04 / SPEC-F1-002
- Sinal: `$app.logger()` e consultas `$app` dentro de `onRecordValidate` quebram TODOS os saves da collection (HTTP 400 genérico "Failed to update/create record"); request hooks com `e.request.pathValue('id')` não resolveram o id de forma confiável; model hook `onRecordUpdate` com `e.oldRecord` + `throw new Error` funcionou (recusas = 400, saves válidos = 200).
- Evidência: bateria de testes via API real (jornada GREEN completa 200 em todas as transições; recusas RED 400 com registro preservado), versões Skip v0.0.7→v0.0.23 com QA ok; artefato 04_fase-atual/pipeline-f1-f1-t04.md.
- Regra reutilizável: em hooks de validação de transição no Skip Cloud (PocketBase v0.36/goja), usar `onRecordUpdate((e) => ...)` com `e.oldRecord` para o estado anterior e `throw new Error(motivo)` para recusar — NÃO usar `$app.logger()`/`$app.findRecordById` dentro de `onRecordValidate`, e NÃO depender de `e.request.pathValue('id')` em request hooks para recuperar o estado anterior.
- Quando aplicar: qualquer hook de validação/campo computado em collections do projeto; também vale para hooks futuros de pipeline/painel.
- Quando não aplicar: hooks after-success (que podem usar `$app` livremente), rotas customizadas `routerAdd` (onde `$app` e helpers de erro são documentados e estáveis).
- Confiança: alta — comportamento reproduzido de forma consistente em múltiplos deploys e confirmado por testes verdes/vermelhos.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto.