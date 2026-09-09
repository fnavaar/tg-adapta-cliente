# Atendimento dos critérios da F2-T01

## Escopo

Implementação local/file-backed exclusiva da F2-T01, com massa sintética. Não é arquitetura definitiva da Fase 2.

## Briefings sintéticos

- `EXP-F2-IN-001`: inbound, site/formulário sintético, R&S.
- `EXP-F2-OUT-001`: outbound, prospecção manual sintética, TMO.

## TDD

- Total: 20 testes.
- Aprovados: 20.
- Falhos: 0.
- Massa: exclusivamente sintética/teste.
- Testes positivos: campos CA-2-01, origem/canal, serviço, hipótese, responsáveis, janela, orçamento.
- Testes negativos: campo ausente, dado real, aprovação por agente, ação externa não autorizada.
- Testes de versionamento e rollback documental: aprovados.
- Resultado detalhado: `../evidence/test-results.json`.

## Critérios e funcionalidades cobertos

- CA-2-01: briefing registra hipótese, público, canal, versão de criativo, janela, orçamento e critério de parada.
- Estados permitidos: Rascunho, Em revisão, Aprovado para preparação, Bloqueado, Rejeitado e Arquivado.
- Estados proibidos nesta task: Em execução, Pausado e Concluído.
- Origem e canal permanecem separados.
- R&S e TMO permanecem identificáveis.
- ICP não é inferido automaticamente.
- Orçamento e datas são sintéticos/teste.
- Responsabilidades usam identificadores `HUMANO-SINTETICO-*`.
- Criativo pode ser não aplicável.
- Histórico e rollback são documentais.
- Aprovação real não foi concedida; registros de aprovação estão marcados como não concedidos.

## Falhas e correções

- Não houve falha no TDD executado: 20/20 aprovados.
- Não houve correção de produto necessária.
- A primeira tentativa de geração em diretório temporário foi bloqueada pelo guardrail de segurança; nenhuma alteração no repositório ocorreu nessa tentativa. A execução foi refeita em diretório de trabalho relativo seguro.

## Evidências

- `data/briefings.json`
- `data/briefing_versions.json`
- `data/creative_versions.json`
- `data/approvals.json`
- `data/blockers.json`
- `surface/state-machine.json`
- `surface/index.html`
- `evidence/test-results.json`
- `evidence/baseline-protection.md`
- `evidence/limits.md`

## Proteção da Fase 1

- Commit-base: `262ce63f1019ca343843e99a348be0866fb8949b`.
- A área autorizada foi somente `05_entregas/fase-2/f2-t01/`.
- A Fase 1 permaneceu fora do recorte de implementação.
- A comparação final deverá confirmar diff e lista de arquivos exclusivamente nessa área, além dos documentos de governança autorizados.

## Limites respeitados

Não houve PocketBase, collection, schema, migration, hook, integração RD Station/1CRM/Meta, publicação, campanha real, orçamento real, gasto, contato externo, dado real, alteração do ICP oficial ou alteração da Fase 1.

## Situação

**Atendimento técnico automatizado dos critérios da F2-T01: evidências preparadas; validação humana do Champion pendente.**

Este relatório não encerra formalmente a task.
