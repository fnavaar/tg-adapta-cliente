# Evidências — F2-T08

## Evidência 1 — QA oficial

- Versão Skip: **0.0.85** (`25c717a`).
- Setup, análise estática, build, integrações e testes: **passaram**.

## Evidência 2 — Critérios e regressões

- T04: **7/7** verificações determinísticas.
- T08: **8/8** verificações determinísticas.
- Bateria humana do Champion: **5/5** testes aprovados.
- `demandas`: 10 registros.
- Migrations: até `0020_f2_t05_decisoes`.
- Collections: somente as existentes antes da T08.
- Nenhuma escrita em `demandas`.
- Nenhuma chamada externa.

## Evidência 3 — Fallback manual

- Lote: `META-F2-MANUAL-001`.
- `source_mode=manual_export`.
- 5 linhas, 100% sintéticas, sem dados pessoais.
- Classificações: vinculado, não vinculado, desconhecido, divergente e inválido.
- Primeira execução: uma criação somente planejada, sem persistência.
- Estado seguro com divergência/inválido: `bloqueada`.

## Evidência 4 — Idempotência e falhas

- Replay idêntico: `replay_skip`, 0 novas ações/contagens.
- Mesmo `batch_id` com payload diferente: `payload_conflict`, `bloqueada`, decisão humana necessária.
- 401/403/429/timeout/payload inválido: todos `SIMULADO`, sem chamada externa e sem retry automático; retorno `fallback_manual` ou `bloqueada`.

## Evidência 5 — Homologação humana

- Teste 1: T04 7/7, pipeline 10, replay 0 — aprovado.
- Teste 2: T08 8/8 e classificações — aprovado.
- Teste 3: replay/conflito — aprovado.
- Teste 4: falhas simuladas — aprovado.
- Teste 5: regressão/proteção de escopo — aprovado.

Evidências anexadas pelo Champion:

- `uploads/d1df2dc5-teste_t08.pdf`
- `uploads/3f201c65-teste_t08_1.pdf`
- `uploads/245f65bd-image.png`
- `uploads/cd87c996-image.png`
- `uploads/971ea98a-teste_t08_5.pdf`

## Limitação registrada

O verificador independente previsto pela rotina não estava disponível neste runtime; checklist equivalente foi executado em série. Não houve critério sem evidência: a limitação foi registrada para auditoria.
