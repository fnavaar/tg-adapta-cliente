# Pipeline F1 — Implementação F1-T04 (entregue, aguardando validação humana)

> **Data:** 2026-08-31 · **Spec:** SPEC-F1-002 · **Task:** F1-T04 · **Status:** IMPLEMENTADO — AGUARDANDO TESTE/VALIDAÇÃO HUMANA DO CHAMPION

## O que foi implementado

### 1. Migration 0004 — 4 campos autorizados (aplicada, QA ok)
Adicionados à collection `demandas` (Skip Cloud / PocketBase):
| Campo | Tipo | Valores |
|---|---|---|
| `status_proposta` | select | em_negociacao, aceita, recusada, sem_retorno |
| `data_conversao_comercial` | date | — |
| `data_conquista` | date | — |
| `tipo_conquista` | select | aquisicao_nova, reativacao |

**Verificação (schema real, collection `demandas`):**
- ✅ exatamente 4 campos novos; **nenhum 5º campo** criado
- ✅ `grupo_economico` **NÃO existe**
- ✅ booleano `conversao_comercial` **NÃO existe**
- ✅ 10 estados preservados (suspect, prospect, lead_qualificado, oportunidade, proposta, vaga_aberta, ganho, perdido, sem_timing, desqualificado)
- ✅ `oferta_servico` continua sendo a fonte R&S × TMO (campo existente, sem novo campo de serviço)

### 2. Hooks de validação (v0.0.23+, QA ok)
- `pipeline_transicoes_create.js` — `onRecordCreateRequest`
- `pipeline_transicoes_update.js` — `onRecordUpdate` com `e.oldRecord`

**Regras implementadas (conforme autorização e emenda E1):**
1. Suspect pode existir sem responsável/próxima ação/prazo (emenda E1); a partir de prospect, os 3 campos são obrigatórios (CA-1-07)
2. suspect→prospect exige responsável + próxima ação + prazo
3. lead_qualificado exige evidência de necessidade real + contato válido + serviço definido (ICP sem campo técnico nesta fase → limitação registrada)
4. oportunidade exige demanda concreta + avanço comercial
5. proposta exige evidência de proposta registrada
6. proposta→vaga_aberta exige status_proposta=aceita
7. vaga_aberta→ganho exige evidência de fechamento (CA-1-10)
8. estados terminais exigem motivo/resultado; ganho exige evidência (RN-F1-009)
9. sem retrocesso de estado terminal
10. data_conquista só em vaga_aberta/ganho; 1ª vaga/demanda válida exige data_conquista
11. tipo_conquista não é preenchido sem evidência de histórico (não presumir)

Toda recusa: HTTP 400 + registro NÃO persistido (mantido sem alteração indevida) + log de request da plataforma.

### 3. Testes executados (via API real, registros fictícios FIX-* removidos após)
**Jornada GREEN (outbound→TMO):** suspect→prospect→LQ→oportunidade→proposta(aceita)→vaga_aberta(data_conquista+tipo_conquista)→ganho = **200 em todos**; retrocesso de terminal = **400**.
**Recusas RED (cada regra):**
- suspect→prospect sem os 3 campos → 400 ✅
- LQ sem contato válido → 400 ✅ (com contato → 200)
- proposta sem evidência → 400 ✅
- terminal sem motivo → 400 ✅
- ganho sem evidência → 400 ✅ (com evidência → 200)
- data_conquista fora de vaga/ganho → 400 ✅
- vaga_aberta sem data_conquista → 400 ✅ (com data_conquista → 200)
- tipo_conquista sem evidência → 400 ✅ (com evidência → 200)
- proposta→vaga_aberta sem aceita → 400 ✅

## Limitações / pendências registradas
1. **ICP sem campo técnico nesta fase** — validação de LQ cobre evidência+contato+serviço; o critério ICP fica para campo/validação futura (registrado como pendência, NÃO inventado).
2. `data_conversao_comercial` é preenchida manualmente no aceite da proposta (sem autopreenchimento automático no hook) — representação por status_proposta=aceita + data preenchida.
3. `e.oldRecord` em `onRecordUpdate`: `$app.logger()`/`$app` queries dentro de `onRecordValidate` quebram saves neste runtime (goja); solução validada foi model hook com `e.oldRecord`.

## NÃO foi alterado (confirmação explícita)
- ❌ `grupo_economico` não criado
- ❌ Nenhum campo além dos 4 aprovados
- ❌ Nenhum estado criado/removido/renomeado (10 estados intactos)
- ❌ SPEC não alterada (emenda E1 já havia sido aplicada em append-only em 31/08)
- ❌ RD Station / 1CRM / integrações / automações externas intocados
- ❌ Nenhum e-mail/WhatsApp/LinkedIn executado
- ❌ Metas comerciais, ICP, inatividade, deduplicação: não inventados
- ❌ F1-T05 não iniciada

## Evidências para validação humana
1. Schema real da collection `demandas` (4 campos, sem extras) — consultável via API/Skip.
2. Logs de request com status 400 das recusas (plataforma).
3. Registros FIX-* usados nos testes foram removidos; fixtures originais intactos.
4. Versões Skip v0.0.7 → v0.0.23 (QA ok em todas).
5. Este artefato (artifacts/pipeline-f1.md) + changelog.md + estado-atual.md.