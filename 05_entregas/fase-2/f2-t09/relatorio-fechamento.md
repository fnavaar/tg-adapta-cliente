# Atendimento e fechamento — F2-T09

**Data do fechamento:** 2026-09-23  
**Task:** F2-T09 — Provar leitura Meta limitada, mapeamento autorizado e tratamento real de erro, sem escrita  
**Champion:** João Paulo  
**SPEC:** F2-004 — Prova de integração Meta ou fallback manual explícito  
**Resultado:** CONCLUÍDA — leitura real limitada executada, prova automática 10/10, teste humano aprovado (PDF 5 páginas); CA-2-11 e CA-2-12 (real) atendidos.

## Escopo fechado

A F2-T09 foi executada exclusivamente dentro do plano autorizado em 22/09 e retomado com autorização expressa do owner em 23/09 ("autorizar implementação da t09"), após a verificação da conexão MetaAds.

- Bloqueio externo de 22/09 (`No connected account`) resolvido em 23/09: conexão ativa no conector, principal João Paulo Oliveira.
- Leitura real limitada executada UMA vez via conector: conta `act_1667348577717128` (TalentGroup_01), nível account, período 15–21/09/2026, somente os 7 campos do contrato do gate 3 — HTTP 200, 0 linhas (sem entregas no período; não é erro).
- Implementação somente frontend: adapter `src/lib/f2/t09/metaBatch.ts` + superfície `src/components/f2/T09IntegratedProof.tsx` integrada em `/atribuicao-t04`.
- Núcleo de reconciliação compartilhado reutilizado (`src/lib/f2/reconciliation/core.ts`) — mesmo padrão T04/T08.
- Registro `META-F2-002` classifica a modalidade como `integrada_validada` em dry-run (o `META-F2-001` da T07 permanece como fallback_manual documentado).
- Nenhuma migration, collection, schema, hook ou RLS novo; nenhuma escrita em `demandas`; nenhum token/segredo no código; nenhuma alteração de campanha, orçamento ou criativo.

## Matriz de critérios

| Critério | Regra/prova | Evidência | Veredito |
|---|---|---|---|
| CA-2-11 | Com acesso validado, leitura limitada reproduz campos aprovados e reconcilia quantidade/identidade com a fonte | Leitura real registrada na superfície (conta, período, 7 campos, HTTP 200, 0 linhas, log_id); contagens do relatório coincidem com o lote (8 linhas, 5 chaves, 1 duplicidade, 1 conflito, 1 inválida, 1 desconhecida); identidade `sistema_origem_tecnico + record_id` (gate 4) | **PASSOU** |
| CA-2-12 (real) | Erro real deixa a integração sem escrita, com registro e retorno seguro | Erro REAL de 22/09 (`connector_no_connected_account`) registrado na superfície: estado `bloqueada`, retry `false`, escritas externas `0`; regras 401/403/429/timeout/payload inválido sem retry cego (RN-F2-013) | **PASSOU** |
| RN-F2-012 | Somente campos autorizados mapeados; campo fora do contrato descartado e registrado | Sanitização provada na bateria (`lead_user_email`, `form_field_answers` descartados e listados) | **PASSOU** |
| Regressão T04/T08/painel | Preservar engine, replay, fallback e painel homologados | T04 7/7, T08 8/8, painel `/` somente leitura; `demandas` 10 registros | **PASSOU** |
| Proteção de dados/escopo | Sem dado pessoal, sem escrita, sem segredo, sem chamada a partir da tela | Rodapé "Modo Somente Leitura" no PDF do Champion; zero escrita verificada | **PASSOU** |

## Teste humano

Aprovado pelo Champion em 23/09/2026 — PDF de 5 páginas (`uploads/5d191bfe-teste_t09.pdf`):

1. Rota correta (`/atribuicao-t04`), pipeline 10, dry-run 0 (pág. 1).
2. Seção T09 visível com proteção de escopo (pág. 2).
3. Leitura real (TalentGroup_01, HTTP 200, 0 linhas, 7 campos do contrato) e erro real de 22/09 com estado seguro (pág. 3).
4. 10/10 verificações verdes + resumo "PASSOU — TDD da F2-T09 (leitura real + dry-run)" (pág. 4).
5. Reconciliação das 8 linhas correta (não vinculado, duplicidade, conflito, desconhecido, inválido) + "Modo Somente Leitura" (pág. 5).

## Verificação automatizável final

- Skip **v0.0.91**, hash **`3a4b243`** (implementação funcional em v0.0.90, `6c739b3`).
- QA oficial: setup, análise estática, build, integrações e testes — todos passaram.
- Prova T09: **10/10** no preview.
- T04: **7/7** · T08: **8/8**.
- `demandas`: 10 registros · migrations até 0020 · collections preservadas.
- Nenhuma escrita em `demandas`; nenhuma chamada Meta a partir da tela; nenhum segredo no código.
- O verificador independente previsto pela rotina não estava disponível neste runtime; o checklist equivalente foi executado em série e essa limitação permanece explicitamente registrada.

## Pendências de governança preservadas

- O principal conectado no conector é **João Paulo Oliveira** (owner nominal), não o leitor dedicado somente leitura decidido no gate 2. A conexão OAuth via Composio herda as permissões de quem consente; regularizar (novo Connect Link pelo leitor dedicado) antes de ampliar o uso da integração — registrada em AP-2026-09-23-1211.
- Agência externa (AYPLA DIGITAL) mantém acesso de escrita na conta de anúncios.
- Nenhuma relação estrutural `demandas` ↔ `experimentos_f2` foi criada (fora do escopo da fase).

## Veredito

A F2-T09 está **formalmente concluída**. Com ela, a Fase 2 atinge **9/9 tasks concluídas**; o encerramento formal da fase e a publicação da próxima dependem da validação do consultor na reunião de ciclo.
