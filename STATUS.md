# STATUS — Projeto TG Mais Serviços de Tecnologia e RH LTDA

> **Atualizado em:** 2026-09-09 · **Por:** Adapta / Consultor

## Onde estamos

- **Fase atual:** 2 — Sistema de campanhas e experimentação de Growth Marketing.
- **Task ativa:** F2-T01 — Materializar briefing versionado de experimento com massa sintética.
- **Debate:** concluído pelo Champion nas Decisões 1–20.
- **Arquitetura:** aprovada para superfície local/file-backed isolada em `05_entregas/fase-2/f2-t01/`.
- **Implementação:** ainda não autorizada e não iniciada.
- **Progresso:** 0 de 9 tasks concluídas.

## Arquitetura aprovada para a F2-T01

A superfície será local e file-backed, exclusiva da F2-T01, com componentes próprios para interface, validação, máquina de estados, versionamento, aprovações, bloqueios, TDD e evidências. O armazenamento será sintético e append-only, com preservação integral do histórico.

## Proteções obrigatórias

Nesta task não criar nem alterar collections, schemas, migrations, hooks, PocketBase, collection `demandas`, código, regras ou dados da Fase 1, nem integrações externas. A arquitetura local não é a arquitetura definitiva da Fase 2 nem do futuro sistema de Growth Marketing.

## Gate de implementação

A aprovação arquitetural não autoriza implementação. Antes de iniciar, será necessário novo pedido expresso do Champion. Durante a implementação, se a superfície não atender algum critério obrigatório, a execução deverá parar, registrar a limitação, apresentar alternativas e aguardar nova decisão.

## Condição de encerramento

A F2-T01 somente poderá ser formalmente encerrada após testes obrigatórios e evidências essenciais aprovados, correção/reteste de falhas, relatório de atendimento dos critérios e validação humana expressa do Champion. Aprovação técnica ou automática não encerra a task.

## Próxima ação

Aguardar autorização expressa e específica para implementar F2-T01.

## Travas e limites

- F2-T09 permanece **condicional/não elegível** até acesso Meta, permissões, payload/campos, chave multi-fonte e autorização específica.
- Nenhuma task autoriza publicar campanha, alterar orçamento, escrever no Meta ou abordar contatos.
- Sem acesso Meta comprovado, o fluxo autorizado é fallback manual com lacuna explícita.

## Fase 1 arquivada

- Fase 1 foi encerrada em 2026-09-03 e está preservada em `05_entregas/fase-1/`.
- O histórico declara 6/6 tasks concluídas e aceite humano registrado; a fonte técnica viva não é versionada neste repositório.