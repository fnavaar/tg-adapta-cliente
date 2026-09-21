# F2-T07 — roteiro de validação humana

A F2-T07 está no gate de validação humana. O objetivo é confirmar o contrato documental, não executar integração ou importar dados.

## O que o Champion deve verificar

1. Abrir `05_entregas/fase-2/f2-t07/META-F2-001-checklist-fallback.md`.
2. Confirmar que a modalidade é `fallback_manual`.
3. Confirmar que o owner da decisão é João Paulo (Champion/direção) e que a operação está atribuída ao marketing/gestor de tráfego.
4. Confirmar que o documento afirma claramente: **não existe integração Meta validada**.
5. Conferir os campos de controle obrigatórios do lote: `batch_id`, datas, `source_mode`, owner, unidade, campos presentes/ausentes e status de reconciliação.
6. Confirmar que `campaign_id`, `campaign_name`, `adset_id`, `ad_id`, período, origem/canal e impressões/cliques são atributos aceitos apenas quando vierem no export autorizado.
7. Confirmar que custo/gasto, leads, formulários, e-mail, telefone e demais dados pessoais não entram no escopo da T07.
8. Confirmar que `batch_id` é a chave de idempotência do lote, enquanto `record_id` só é usado no escopo da fonte declarada; não há identidade global/multi-fonte.
9. Confirmar a separação de responsabilidades: T08 prova o lote/manual e falhas simuladas; T09 é condicional para leitura Meta real.
10. Confirmar que não houve alteração funcional, conexão externa ou início de T08/T09.

## Resultado esperado

A documentação está coerente com a SPEC F2-004 e com a autorização: `fallback_manual` selecionado, sem integração Meta alegada, sem credenciais, sem dados pessoais e com handoff explícito para T08/T09.

## Como reconhecer falha

- o documento indicar `integrada_validada`;
- houver token, OAuth, segredo ou chamada externa;
- houver lead, formulário ou contato real;
- `record_id` for tratado como identidade global;
- a T08/T09 for considerada executada nesta etapa;
- qualquer collection, migration, hook, RLS, `demandas` ou T04 tiver sido alterado.

Após conferir, responda se o roteiro está aprovado ou qual ponto precisa de correção. A F2-T07 não deve ser concluída antes dessa confirmação.
