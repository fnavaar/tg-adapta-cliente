# AP-2026-09-21-0936 — Fallback manual não é integração e não resolve identidade global

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T07 / SPEC F2-004
- Sinal: a F2-T07 foi concluída sem conexão Meta, formalizando `fallback_manual`, contrato de lote e owner funcional; a aprovação humana separou `batch_id` (idempotência do lote) de `record_id` (somente no escopo da fonte declarada).
- Evidência: `05_entregas/fase-2/f2-t07/META-F2-001-checklist-fallback.md`, `05_entregas/fase-2/f2-t07/evidencias.md`, aprovação humana do Champion e revalidação do Skip v0.0.81 (`e64f8bc`) sem Meta/credencial/collection nova.
- Regra reutilizável: quando uma fonte externa ainda não tem acesso validado, formalizar o fallback como modalidade distinta da integração; usar uma chave de lote para idempotência e preservar a chave da fonte declarada sem inferir identidade global ou deduplicação multi-fonte.
- Quando aplicar: preparação de fontes externas, exports manuais e tasks anteriores a uma integração real.
- Quando não aplicar: quando houver contrato de identidade global aprovado e integração real autorizada; nesse caso as chaves e o mapeamento precisam de nova decisão explícita.
- Confiança: alta — contrato aprovado, regressão conferida e nenhum efeito externo produzido.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
