# STATUS — Projeto TG Mais Serviços de Tecnologia e RH LTDA

> **Atualizado em:** 2026-09-23 · **Por:** Adapta / Champion  
> O painel do projeto: fase atual, progresso e o que precisa de atenção.

## Onde estamos

- **Fase atual:** 2 — Sistema de campanhas e experimentação de Growth Marketing (LIBERADA PARA EXECUÇÃO).
- **Task ativa:** F2-T09 — implementada em 23/09/2026 (Skip v0.0.90, `6c739b3`); aguardando teste humano do Champion.
- **Task anterior:** F2-T08 concluída e validada em 2026-09-21.
- **Progresso:** 8 de 9 tasks concluídas (89%); F2-T09 implementada, prova automática 10/10, pendente validação humana.

## Resultado da execução da F2-T09 (23/09/2026)

- Bloqueio externo resolvido: conexão MetaAds ativa no conector (principal João Paulo Oliveira); conta `TalentGroup_01` ativa e legível.
- Leitura real limitada executada: conta `act_1667348577717128`, 15–21/09/2026, somente campos do contrato do gate 3; HTTP 200, 0 linhas (sem entregas no período — não é erro).
- Implementação somente frontend, reutilizando o núcleo T04/T08: adapter `src/lib/f2/t09/metaBatch.ts` + superfície `src/components/f2/T09IntegratedProof.tsx` em `/atribuicao-t04`.
- Prova T09 10/10 PASSOU no preview: contrato de campos, sanitização RN-F2-012 (descarte registrado), identidade `sistema_origem_tecnico + record_id` (gate 4), contagens CA-2-11, dry-run sem escrita, replay idempotente, conflito de batch_id bloqueado, erro REAL de 22/09 tratado com estado seguro sem retry (CA-2-12 real), regras 401/403/429/timeout/payload inválido (RN-F2-013), núcleo compartilhado com pipeline somente leitura.
- Regressões: T04 7/7, T08 8/8, painel `/` OK; `demandas` 10 registros, zero escrita; nenhuma migration/collection/schema/hook novo.
- Nenhum token, senha ou segredo no código; nenhuma alteração de campanha/orçamento/criativo.

## Gate atual

**F2-T09 aguardando teste humano:** o Champion deve abrir `/atribuicao-t04` no preview, rolar até a seção "Prova da leitura Meta integrada (F2-T09)", clicar em "Executar prova T09" e conferir as 10 verificações verdes e o resumo "PASSOU — TDD da F2-T09 (leitura real + dry-run)". Sem essa aprovação a task não será concluída.

## Próxima ação única

Teste humano do Champion na seção T09 de `/atribuicao-t04`; após aprovação explícita, concluir a F2-T09.

## Resultado preservado da F2-T08

- Relatório de fechamento: `05_entregas/fase-2/f2-t08/relatorio-fechamento.md`.
- Produto funcional: Skip v0.0.85, hash `25c717a`, preservado durante o fechamento; versão atual v0.0.90 (`6c739b3`) com a T09.
- T04: 7/7; T08: 8/8; bateria humana: 5/5.
- Lote `META-F2-MANUAL-001`: 5 linhas, 100% sintéticas, `manual_export`, sem dados pessoais.
- Idempotência: replay `skip`; payload diferente com mesmo `batch_id` → conflito/bloqueio/decisão humana.
- Falhas 401/403/429/timeout/payload inválido simuladas, sem chamada externa, sem retry automático.
- `demandas`: 10 registros; migrations até 0020; collections preservadas.

## Pendências preservadas

- CA-2-11 e CA-2-12 no recorte real: provados em dry-run com leitura real registrada; fechamento formal depende do teste humano.
- Leitor dedicado tem acesso parcial na conta, mas controle total do portfólio; ressalva de governança registrada para rollback.
- Principal conectado no conector é João Paulo Oliveira, não o leitor dedicado; divergência de acesso mínimo registrada para decisão de regularização.
- Agência externa permanece com acesso de escrita na conta de anúncios.
- Nenhuma relação estrutural `demandas` ↔ `experimentos_f2` foi criada.
- F2-T09 implementada e aguardando teste humano; não está concluída.
