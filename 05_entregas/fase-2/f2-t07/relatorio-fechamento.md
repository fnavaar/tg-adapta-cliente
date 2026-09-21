# Atendimento e fechamento — F2-T07

**Data do fechamento:** 2026-09-21  
**Task:** F2-T07 — Preencher o checklist Meta e documentar contrato de campos/owner ou selecionar formalmente fallback manual  
**Champion:** João Paulo  
**SPEC de referência:** F2-004 — Prova de integração Meta ou fallback manual explícito  
**Resultado:** CONCLUÍDA — `META-F2-001` aprovado humanamente; modalidade `fallback_manual` formalizada; nenhuma implementação funcional.

## Escopo autorizado

A F2-T07 foi executada e fechada exclusivamente como task documental/de governança. O Champion aprovou humanamente o `META-F2-001`, a modalidade `fallback_manual` e o contrato apresentado.

Não houve:

- conexão com Meta;
- token, OAuth ou segredo;
- acesso a Business Manager, conta de anúncios, página ou Pixel;
- chamada externa;
- importação de lote ou dados reais;
- importação de leads, formulários ou contatos;
- nova tela ou rota;
- nova collection, campo, migration, hook ou RLS;
- alteração em `demandas`, T04 ou decisões existentes;
- início da F2-T08 ou F2-T09.

## Registro aprovado

- **Registro:** `META-F2-001`.
- **Modalidade:** `fallback_manual`.
- **Integração Meta:** não validada neste momento.
- **Owner de decisão/governança:** João Paulo (Champion/direção).
- **Responsável operacional:** marketing/gestor de tráfego, definido por função nesta etapa.
- **Responsável por qualidade/reconciliação:** marketing + comercial, definido por função nesta etapa.
- **Owner operacional nominal:** deverá ser indicado quando houver operação real, conforme a governança aplicável.

A aprovação humana confirmou explicitamente que `fallback_manual` é fallback e não integração Meta.

## Matriz de revalidação

| Item | Regra/contrato | Evidência | Resultado |
|---|---|---|---|
| Modalidade | RN-F2-011: sem acesso/campos/permissão/payload comprovados, não habilitar integração; selecionar fallback ou bloqueio. | `META-F2-001` registra `Status: fallback_manual` e ausência de integração validada. Aprovação humana do Champion. | **PASSOU** |
| Owner e papéis | SPEC F2-004: direção governa; marketing opera o fallback; comercial devolve qualidade; consultor revisa a primeira prova. | Seção 3 do `META-F2-001`; papéis aprovados pelo Champion. | **PASSOU** |
| Contrato de lote | RN-F2-014: lote manual deve registrar origem, período, unidade e lacunas. | Campos `batch_id`, datas, `source_mode`, `source_owner`, `unit_label`, `provided_fields`, `missing_fields` e `reconciliation_status`. | **PASSOU** |
| Campos permitidos | F2-004: mapear somente campos autorizados; métricas de campanha não equivalem a qualidade. | IDs/nomes de campanha, conjunto e anúncio; período, canal/origem declarados, impressões, cliques e `spend` apenas como leitura. | **PASSOU** |
| Campos proibidos | Limite aprovado: sem contatos sem autorização; T07 não ingere leads/formulários/dados pessoais. | Nome, e-mail, telefone, cargo, `lead_id`, `form_id`, conteúdo de formulário, Pixel/eventos de pessoa e contatos reais excluídos. | **PASSOU** |
| Ausência/divergência | F2-002/RN-F2-004: ausentes não viram zero; desconhecido não é inferido. | `missing_fields`, estados `não_vinculado`/`desconhecido`, `divergente`/`bloqueado`; sem inferência. | **PASSOU** |
| Idempotência | Contrato de fallback: mesmo `batch_id` não duplica resultado. | `batch_id` aprovado como chave de idempotência do lote manual. | **PASSOU** |
| Reconciliação | F2-002: `record_id` permanece restrito à fonte declarada; sem identidade global/multi-fonte. | `record_id` só é usado quando o lote autorizado trouxer referência correspondente; sem chave global/composta. | **PASSOU** |
| Handoff | F2-T08 prova o lote e falhas simuladas; F2-T09 é condicional para leitura real. | Seções 8 e 9 do `META-F2-001`; T08/T09 não iniciadas. | **PASSOU** |

## Revalidação do RED/GREEN equivalente

### RED — integração sem acesso

- Condição: não há checklist de acesso, permissão, payload ou owner técnico Meta comprovados.
- Resultado esperado: modo integrado não é habilitado; nenhum segredo, token, OAuth ou conector é criado.
- Resultado observado: `fallback_manual` foi selecionado; nenhuma conexão ou credencial foi criada.
- Veredito: **PASSOU**.

### GREEN — contrato manual completo

- Condição: owner registra modalidade, contrato, lacunas e regra de reconciliação.
- Resultado esperado: `META-F2-001` completo, sem alegar integração e sem ingerir dados reais.
- Resultado observado: checklist/contrato aprovado pelo Champion e mantido no artefato documental.
- Veredito: **PASSOU**.

### Regressão de escopo

Consulta somente leitura confirmou:

- Skip funcional: v0.0.81 (`e64f8bc`);
- migrations: aplicadas até `0020_f2_t05_decisoes`;
- collections: apenas as existentes da Fase 1/F2-T01–T05;
- contagens vivas: `demandas=10`, `experimentos_f2=3`, `experimento_versoes_f2=26`, `aprovacoes_f2=4`, `bloqueios_f2=2`, `decisoes_f2=6`;
- rotas existentes: Pipeline, Experimentos, Atribuição T04 e Decisões F2;
- nenhuma chamada externa ao Meta;
- nenhum token/OAuth/segredo;
- nenhum dado real, lead, formulário ou contato;
- nenhuma alteração em `demandas`, T04 ou decisões F2;
- F2-T08 e F2-T09 não iniciadas.

O arquivo de verificador previsto pela rotina não estava disponível neste runtime; o checklist independente equivalente foi executado em série, sem ocultar essa limitação.

## Preservação

- Fase 1 permanece preservada e homologada.
- F2-T01 permanece preservada.
- F2-T02 permanece preservada.
- F2-T03 permanece preservada, com `record_id` restrito à fonte declarada.
- F2-T04 permanece preservada, sem integração externa ou escrita adicional em `demandas`.
- F2-T05 permanece preservada, incluindo decisões, histórico, revogação e TDD 6/6.
- F2-T06 permanece preservada, com fechamento documental já aprovado.

## Evidências e handoff

- Contrato: `05_entregas/fase-2/f2-t07/META-F2-001-checklist-fallback.md`.
- Evidências: `05_entregas/fase-2/f2-t07/evidencias.md`.
- Roteiro humano: `05_entregas/fase-2/f2-t07/roteiro-validacao-humana.md`.
- Prova operacional do lote manual: F2-T08.
- Leitura Meta real, se elegível: F2-T09.

## Veredito

A F2-T07 está formalmente concluída como task de contrato, checklist, owner, modalidade e governança da fonte:

- `fallback_manual` aprovado;
- contrato aprovado;
- ausência de integração Meta explicitamente registrada;
- critérios RN-F2-011 e RN-F2-012 atendidos;
- nenhuma alteração funcional realizada.

A F2-T08 permanece bloqueada até novo pedido/autorização e a F2-T09 permanece condicional. Nenhuma task posterior foi iniciada.
