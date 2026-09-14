# AP-2026-09-14-0935 — Fonte única e metadado de build preexistente

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T03 / F2-002
- Sinal: a atribuição da F2-T03 foi comprovada mantendo uma única fonte declarada, com `record_id` usado apenas dentro de `demandas`; metadado preexistente de build foi separado da mudança funcional.
- Evidência: migration 0019 aplicada; 4/4 testes humanos; reconciliações com diferença zero; auditoria do `.skip.config.json` e registro de fechamento da F2-T03.
- Regra reutilizável: em tasks com working tree preexistente, separar explicitamente metadado automático de build da alteração funcional e registrar a chave somente no escopo da fonte autorizada; não inferir identidade multi-fonte.
- Quando aplicar: quando uma task de atribuição/reconciliação operar sobre uma fonte única e houver metadado de build pendente antes da implementação.
- Quando não aplicar: não usar `record_id` local como identidade global entre sistemas; não tratar metadado de build como mudança de produto sem evidência.
- Confiança: alta — sustentado por auditoria, migration aplicada, QA, regressão e validação humana.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto.
