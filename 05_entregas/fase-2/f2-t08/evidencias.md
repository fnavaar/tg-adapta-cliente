# Evidências — F2-T08

## Evidência 1 — QA oficial

- Versão Skip: **0.0.85**.
- Hash: **`25c717a`**.
- Setup: passou.
- Análise estática: passou.
- Build: passou.
- Integrações: passou.
- Testes: passou.

## Evidência 2 — T04 preservada

Na rota `/atribuicao-t04`, após executar o lote T04:

- baseline F1/F2-T03: fonte 10 × pipeline 10;
- duas criações somente planejadas;
- RED sem chave não inferido;
- uma duplicidade sinalizada;
- um conflito bloqueado;
- replay com 0 criações novas;
- engine pura;
- resultado exibido: **PASSOU — todas as verificações determinísticas da T04**.

## Evidência 3 — T08

Após executar `META-F2-MANUAL-001`:

- 5 linhas sintéticas;
- `source_mode=manual_export`;
- sem dados pessoais;
- pipeline lido: 10;
- uma criação planejada e não executada;
- estado seguro final: `bloqueada`, porque a massa contém divergente e inválido;
- classificações observadas: `vinculado`, `nao_vinculado`, `desconhecido`, `divergente`, `invalido`;
- TDD: **8/8 passou**.

## Evidência 4 — idempotência

- Reenvio idêntico de `META-F2-MANUAL-001`: `replay_skip`.
- Ações novas: 0.
- Mensagem exibida: “batch_id já registrado; zero nova criação e zero nova contagem”.
- Mesmo `batch_id` com campanha alterada: `payload_conflict`.
- Estado: `bloqueada`.
- Mensagem: decisão humana necessária, sem overwrite.

## Evidência 5 — falhas

| Código | Situação | Estado seguro | Chamada real ao Meta | Retry automático |
|---|---|---|---|---|
| 401 | autorização ausente/expirada | `fallback_manual` | não | não |
| 403 | permissão insuficiente | `fallback_manual` | não | não |
| 429 | limite de requisições | `fallback_manual` | não | não |
| timeout | ausência de resposta | `fallback_manual` | não | não |
| payload inválido | contrato incompleto | `bloqueada` | não | não |

A interface marca todos os cinco casos como **SIMULADO**. Nenhum é resposta real da Meta.

## Evidência 6 — preservação do produto

- `demandas`: 10 registros.
- Migrations: até `0020_f2_t05_decisoes`.
- Collections: apenas as existentes antes da T08.
- T04 e F2-T01–T07: preservadas.
- Nenhuma escrita em `demandas`.
- Nenhuma chamada externa.
- F2-T09: não iniciada.

## Validação humana em andamento

- **Teste 1 — APROVADO (2026-09-21 ~16:53)**: Champion executou o lote T04 e enviou PDF com as 7 verificações verdes, mensagem “PASSOU — todas as verificações determinísticas da T04”, pipeline preservado em 10 registros, 0 criações no replay e a seção T08 ainda não executada. Evidência: `uploads/d1df2dc5-teste_t08.pdf` (7 páginas).
- **Teste 2 (lote manual e classificações)**: aguardando execução pelo Champion.
- **Testes 3–5**: pendentes após aprovação do Teste 2.
- A F2-T08 permanece aberta; nenhum aceite final foi declarado.
