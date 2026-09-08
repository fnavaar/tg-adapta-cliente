# F1-T06 — Painel mínimo, reconciliação e reprocessamento controlado

**Data:** 2026-09-03 · **Task:** F1-T06 · **Status:** CONCLUÍDA — VALIDADA HUMANAMENTE PELO CHAMPION

## Resultado

A F1-T06 foi implementada e aprovada expressamente pelo Champion em 2026-09-03.

- Tela real somente leitura em `src/pages/Index.tsx`, rota `/`.
- Consulta da collection `demandas` com filtros locais por período, `tipo_origem`, canal, campanha, `oferta_servico`, responsável e estado.
- Reconciliação real entre painel e consulta equivalente da fonte, comparando quantidade e identidade dos registros.
- Categoria `desconhecido` preservada separadamente.
- Reprocessamento controlado por aplicação, sem UNIQUE.
- Rollback limitado à camada da F1-T06 e registros fictícios/controlados.

## Evidências

- Fonte: 7 registros; 7 `record_id` preenchidos; 7 distintos; nenhuma duplicidade.
- Filtros e combinações testados com diferença zero e IDs coincidentes.
- U1–U7 passaram.
- Regressão F1-T01 a F1-T05 passou.
- Registros temporários `F1T06-*`: zero restantes.
- Fixtures oficiais `FIX-IN-001`, `FIX-OUT-001`, `FIX-UNK-001`, `FIX-DUP-001` e `FIX-SEC-001`: preservados, uma ocorrência cada.
- Skip v0.0.31, hash `1293baa`; QA completo passou.

## Pendência arquitetural

Antes de integração efetiva com múltiplas fontes técnicas, definir a estratégia de identidade: `record_id` global, `sistema_origem_tecnico + record_id` ou outra chave aprovada. Só depois reavaliar proteção em duas camadas: aplicação e UNIQUE apropriado no banco.

RD Station e 1CRM não foram tocados.
