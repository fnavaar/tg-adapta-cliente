# Pipeline F1 — Implementação F1-T04 (correções aplicadas, aguardando validação humana)

> **Data:** 2026-09-01 · **Spec:** SPEC-F1-002 · **Task:** F1-T04 · **Status:** IMPLEMENTADO + CORREÇÕES — AGUARDANDO TESTE/VALIDAÇÃO HUMANA DO CHAMPION

## O que foi implementado

### 1. Migration 0004 — 4 campos autorizados (aplicada, QA ok)
Adicionados à collection `demandas` (Skip Cloud / PocketBase):
| Campo | Tipo | Valores |
|---|---|---|
| `status_proposta` | select | em_negociacao, aceita, recusada, sem_retorno |
| `data_conversao_comercial` | date | — |
| `data_conquista` | date | — |
| `tipo_conquista` | select | aquisicao_nova, reativacao |

**Verificação (schema real, collection `demandas`, 01/09):**
- ✅ exatamente 4 campos novos; **nenhum 5º campo** criado
- ✅ `grupo_economico` **NÃO existe**
- ✅ booleano `conversao_comercial` **NÃO existe**
- ✅ 10 estados preservados (suspect, prospect, lead_qualificado, oportunidade, proposta, vaga_aberta, ganho, perdido, sem_timing, desqualificado)
- ✅ `oferta_servico` continua sendo a fonte R&S × TMO (campo existente, sem novo campo de serviço)

### 2. Hooks de validação (v0.0.27, QA ok)
- `pipeline_transicoes_create.js` — `onRecordCreateRequest`
- `pipeline_transicoes_update.js` — `onRecordUpdate` com `record.original()` (estado anterior)

**Regras implementadas (conforme autorização, emenda E1 e correções 01/09):**
1. Suspect pode existir sem responsável/próxima ação/prazo (emenda E1); a partir de prospect, os 3 campos são obrigatórios (CA-1-07)
2. suspect→prospect exige responsável + próxima ação + prazo
3. lead_qualificado exige evidência de necessidade real + contato válido + serviço definido (ICP sem campo técnico nesta fase → **pendência registrada, regra de negócio intacta**)
4. oportunidade exige demanda concreta + avanço comercial
5. proposta exige evidência de proposta registrada
6. proposta→vaga_aberta exige status_proposta=aceita
7. **vaga_aberta→ganho exige NOVA evidência de fechamento nesta atualização** (CA-1-10; evidência anterior não conta)
8. estados terminais exigem motivo/resultado; ganho exige evidência (RN-F1-009)
9. sem retrocesso de estado terminal
10. data_conquista só em vaga_aberta/ganho; 1ª vaga/demanda válida exige data_conquista
11. tipo_conquista não é preenchido sem evidência de histórico (não presumir)

**CORREÇÃO 1 — autopreenchimento de `data_conversao_comercial`:**
- No primeiro momento em que `status_proposta` = `aceita`, o sistema registra automaticamente a data/hora (UTC ISO, padrão do projeto).
- A data **não é sobrescrita** em edições posteriores (preservação da original via `record.original()`).
- Conversão Comercial continua NÃO sendo estado; `status_proposta=aceita` representa o aceite; `data_conversao_comercial` representa quando o aceite ocorreu; `data_conquista` continua sendo evento da 1ª vaga/demanda válida.

**CORREÇÃO 2 — motivo específico de recusa identificável:**
- Recusas lançam `BadRequestError(motivo)` → a resposta HTTP 400 **contém a mensagem específica** (ex.: `"Nao e possivel avancar para prospect: responsavel, proxima_acao e prazo sao obrigatorios..."`).
- Evidência observável: resposta HTTP + log de request (status 400).
- Nenhum campo de banco criado para erro; usa o construtor de erro padrão do PocketBase.

### 3. Testes executados (via API real, registros fictícios FIX-* removidos após) — 01/09/2026

**TESTE A (autopreenchimento):** `status_proposta: em_negociacao → aceita` → `data_conversao_comercial` preenchida automaticamente (`2026-09-01 17:22:21.827Z`). ✅

**TESTE B (preservação):** edição posterior do registro → `data_conversao_comercial` NÃO sobrescrita (mantida a original). ✅

**TESTE C (suspect→prospect sem campos):** HTTP 400, registro preservado em `suspect`, motivo específico na resposta. ✅

**TESTE D (proposta→vaga_aberta sem aceita):** HTTP 400, registro preservado em `proposta`, motivo: `"Nao e possivel avancar para Vaga Aberta: a proposta precisa estar aceita."` ✅

**TESTE E (vaga→ganho sem nova evidência):** HTTP 400, registro preservado em `vaga_aberta`, motivo: `"Nao e possivel marcar como Ganho: falta evidencia de fechamento da vaga/demanda (CA-1-10)."` ✅

**TESTE F (jornada válida completa):** suspect→prospect→LQ→oportunidade→proposta(aceita)→vaga_aberta→ganho = **200 em todos**, com `data_conversao_comercial` autopreenchida, `data_conquista` e `tipo_conquista` independentes. ✅

**Regressão de recusas:** LQ sem critérios (400 + motivo), terminal sem motivo (400 + motivo), data_conquista fora de vaga/ganho (400 + motivo), tipo_conquista sem evidência (400 + motivo), retrocesso de terminal (400 + motivo). ✅

## Limitações / pendências registradas
1. **ICP sem campo técnico nesta fase** — validação de LQ cobre evidência+contato+serviço; o critério ICP fica para campo/validação futura. **Regra de negócio oficial (3 condições) NÃO alterada.** Esta pendência, isoladamente, não impede a conclusão da F1-T04 (conforme Champion).
2. `data_conversao_comercial` é preenchida automaticamente no aceite (correção aplicada); não há mais dependência de preenchimento manual.

## NÃO foi alterado (confirmação explícita)
- ❌ `grupo_economico` não criado
- ❌ Nenhum campo além dos 4 aprovados (nenhum campo de erro criado)
- ❌ Nenhum estado criado/removido/renomeado (10 estados intactos)
- ❌ SPEC não alterada (emenda E1 já aplicada em append-only em 31/08)
- ❌ RD Station / 1CRM / integrações / automações externas intocados
- ❌ Nenhum e-mail/WhatsApp/LinkedIn executado
- ❌ Metas comerciais, ICP, inatividade, deduplicação: não inventados
- ❌ F1-T05 não iniciada

## Evidências para validação humana
1. Schema real da collection `demandas` (4 campos, sem extras; sem grupo_economico) — consultável via API/Skip.
2. Respostas HTTP com motivo específico (evidência acima).
3. Registros FIX-* usados nos testes removidos; fixtures originais intactos.
4. Versões Skip v0.0.24 → v0.0.27 (QA ok em todas).
5. Este artefato (04_fase-atual/pipeline-f1-f1-t04.md) + changelog.md + estado-atual.md.
