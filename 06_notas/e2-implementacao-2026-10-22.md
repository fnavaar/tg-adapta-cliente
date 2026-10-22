# E2 — Implementação da segregação `origem_dado` (22/10/2026)

**Autorização:** Champion/owner em 22/10/2026, 15:59 — "Autorizo a E2 — pode implementar".
**Escopo:** migration não destrutiva + backfill + núcleo de consulta + painel oficial segregado (Skip 51414). Nenhum dado real, nenhum registro `producao` criado.

## O que foi implementado

1. **Migration `pocketbase/migrations/0021_origem_dado.js`**
   - Campo select `origem_dado` com valores fechados {sintetico, producao} na coleção `demandas`.
   - Backfill: todo registro existente marcado `sintetico` (idempotente — só preenche campo vazio).
   - Rollback não destrutivo: remove apenas o campo; registros intactos.
   - Status na instância: **applied** (22/10/2026 19:09:29 UTC, id 32ee5ef716c9bcdedca6c622be1118d3).

2. **Núcleo de consulta `src/lib/origem-dado.ts`**
   - `ORIGEM_DADO` ({SINTETICO, PRODUCAO}), `normalizarOrigemDado` (default seguro: ausente/inválido = sintetico), `filtroOrigemDado` (cláusula server-side por modo), `classificarOrigem`, `resumirSegregacao`, `filtrarPorOrigem`.
   - Diretriz 3 da DECISÃO: indicadores oficiais só `producao`; diretriz 4: sintéticos consultáveis em modo homologação.

3. **Painel oficial `src/pages/Index.tsx`**
   - `recordsProducao` = somente `origem_dado=producao`; cards, filtros, opções de filtro e reconciliação (`buildSourceFilter` via `filtroOrigemDado('producao', …)`) passam por essa lista.
   - Selo "Painel oficial — somente origem_dado=producao" com contagem do modo homologação preservado.

## Verificação automática (evidência)

- QA Skip apply 1 — **v0.0.97, ref 08c6e6a**: setup/staticAnalysis/build/integrations OK, test.ran=false (projeto sem suite).
- QA Skip apply 2 — **v0.0.98, ref 2aab7da**: idem OK (estado + opções de filtro segregadas).
- Banco via API do PocketBase (22/10/2026 ~19:15 UTC):
  - `totalItems` = **10**
  - `origem_dado="sintetico"` = **10**
  - `origem_dado="producao"` = **0**
  - `origem_dado=""` (vazio) = **0**
  - `producao && tipo_origem="inbound"` = 0 (filtro combinado server-side funciona)
  - Registros conferidos por `record_id`: FIX-IN-001, FIX-OUT-001, FIX-UNK-001, FIX-DUP-001, FIX-SEC-001, FIX-GREEN-002, FIX-DIAG-002, ATR-F2-IN-001, ATR-F2-OUT-001, ATR-F2-UNK-001 — todos `sintetico`.

## Critérios

- CA-E2-01 (preservação): 10 antes → 10 depois, nenhum excluído/mesclado — PASSA.
- CA-E2-02 (backfill): 10/10 `sintetico` — PASSA.
- CA-E2-03 (producao): 0 registros `producao` (LGPD pendente, diretriz 8) — PASSA.

## Limitações

- Teste suite do projeto não existe (`test.ran=false`); verificação por QA de build + leitura direta do banco.
- Painel em preview ainda não conferido visualmente — é o teste humano do Champion.
- Nota de escopo: a E2 de coleções da F3-T01 (propostas/vagas) segue bloqueada por D4; esta E2 trata exclusivamente do campo `origem_dado`.
