# Evidências da F2-T07 — META-F2-001

## Escopo executado

- [x] Modalidade formalmente selecionada como `fallback_manual`.
- [x] Owner da decisão: João Paulo (Champion/direção).
- [x] Responsável operacional: marketing/gestor de tráfego.
- [x] Responsável pela qualidade/reconciliação: marketing + comercial, com direção para divergências.
- [x] Registro explícito de que não existe integração Meta validada.
- [x] Contrato mínimo de lote manual documentado.
- [x] Campos de campanha aceitos documentados.
- [x] Campos ausentes, desconhecidos e proibidos documentados.
- [x] Leads, formulários e dados pessoais excluídos do escopo.
- [x] Regra de `batch_id` e reenvio idempotente documentada.
- [x] Regra de reconciliação limitada ao `record_id` da fonte declarada documentada.
- [x] Ausência de identidade global/multi-fonte preservada.
- [x] Operação reservada à F2-T08 documentada.
- [x] Leitura real condicional reservada à F2-T09 documentada.

## RED equivalente da T07

**Condição:** tentar habilitar modo integrado sem checklist, acesso, permissão e payload.

**Resultado esperado:** não habilitar integração; manter a modalidade `fallback_manual`; não criar segredo, token, OAuth ou conector.

**Resultado observado nesta task:** o produto não foi alterado e nenhuma tentativa de conexão foi executada. A análise de baseline confirmou que não existe conector Meta, token, OAuth ou collection Meta no Skip. O documento `META-F2-001` registra explicitamente o bloqueio do modo integrado e seleciona o fallback.

**Status:** PASSOU por prova documental e de escopo.

## GREEN equivalente da T07

**Condição:** owner registra `fallback_manual` com contrato de campos, lote, lacunas e reconciliação.

**Resultado esperado:** registro `META-F2-001` completo, sem alegação de integração e sem ingestão de dados reais.

**Resultado observado:** documento completo criado em `05_entregas/fase-2/f2-t07/META-F2-001-checklist-fallback.md`, com owner, modalidade, contrato, limites e handoff para T08/T09.

**Status:** PASSOU por inspeção documental.

## Regressão de escopo

- [x] Skip permanece na versão funcional v0.0.81 (`e64f8bc`) antes do checkpoint documental.
- [x] Migrations permanecem até `0020_f2_t05_decisoes`; nenhuma migration F2-T07 foi criada.
- [x] Collections permanecem as existentes; nenhuma collection Meta/manual foi criada.
- [x] Rotas funcionais existentes permanecem Pipeline, Experimentos, Atribuição T04 e Decisões F2.
- [x] Nenhuma chamada externa ao Meta foi feita.
- [x] Nenhum token/OAuth/segredo foi criado, lido ou armazenado.
- [x] Nenhum dado real, lead, formulário ou contato foi importado.
- [x] `demandas` e T04 não foram alterados.
- [x] F2-T08 e F2-T09 não foram iniciadas.

## Limitações honestas

- O fallback ainda não foi exercitado com o lote operacional; isso pertence à F2-T08.
- Nenhuma permissão Meta foi verificada; leitura real pertence à F2-T09, se elegível.
- Não há integração Meta validada.
- A reconciliação continua restrita à fonte declarada e não resolve identidade global/multi-fonte.
