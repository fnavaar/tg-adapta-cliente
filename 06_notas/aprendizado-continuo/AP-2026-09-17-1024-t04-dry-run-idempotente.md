# AP-2026-09-17-1024 — Reconciliação dry-run com lote-fonte independente

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T04 / F2-002
- Sinal: a reconciliação idempotente exigiu separar o baseline preservado da verificação do lote completo; o destino deve ser comparado com todas as chaves preenchidas do lote-fonte para que o replay dos GREEN não seja classificado como pipeline-only, enquanto a reconciliação do baseline continua validando somente os 10 registros preservados.
- Evidência: `05_entregas/fase-2/f2-t04/relatorio-fechamento.md`; Skip v0.0.66 (`c27bc10`); 7/7 verificações determinísticas; replay com 0 novas criações; pipeline real preservado em 10 registros.
- Regra reutilizável: quando uma task opera em dry-run sobre fonte independente, manter a engine pura, separar baseline de lote completo e calcular idempotência contra todas as chaves da fonte declarada; não gravar no destino sem autorização explícita.
- Quando aplicar: reconciliação de lote, reprocessamento ou atribuição em que a fonte é independente e o destino precisa permanecer somente leitura.
- Quando não aplicar: não transformar `record_id` local em identidade global, não agregar fontes técnicas diferentes e não substituir a validação humana por inferência.
- Confiança: alta — sustentado por QA, prova determinística, replay e três testes humanos aprovados.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
