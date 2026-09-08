# F1-T05 — Jornada e handoff controlado

**Data:** 2026-09-01 18:15–18:20 · **Task:** F1-T05 · **Status:** IMPLEMENTADA — AGUARDANDO VALIDAÇÃO HUMANA DO CHAMPION

## Implementado

- Migration 0005 aplicada no Skip Cloud, adicionando somente `handoff_status` (select opcional: pendente/aceito/recusado) e `icp_validado` (select opcional: sim/nao).
- Hook `pipeline_transicoes_update.js` ajustado exclusivamente para handoff, proteção do aceite e validação humana de ICP.
- Nenhum estado, collection, tabela de histórico ou integração externa criado.

## Regras demonstradas

- Suspect sem handoff continua válido.
- Handoff pendente exige evidência e mantém Suspect.
- Suspect→Prospect exige handoff_status=aceito, responsável, próxima ação e prazo.
- Handoff recusado exige resultado, evidência, responsável e qualidade=pendente; permanece Suspect.
- Retry recusado→pendente é manual e exige nova evidência. Não existe retry automático nem histórico estruturado nesta fase.
- Após aceite, handoff_status=aceito não pode voltar a pendente, recusado ou vazio.
- ICP é decisão humana: vazio não analisado, sim dentro do ICP, nao fora do ICP; o sistema não preenche o campo.
- Prospect→Lead Qualificado exige ICP=sim, evidência de necessidade/interesse real, contato profissional válido e serviço identificado.
- ICP vazio recusa com “ICP ainda não validado.”; ICP=nao recusa com “Empresa validada como fora do ICP.”; ICP=nao não cria estado terminal.
- Canal indisponível: NÃO DEMONSTRÁVEL TECNICAMENTE nesta fase; não foi criado campo, estado, simulação ou integração.

## Testes via API real

- **H1–H10:** H1, H2, H3, H4, H5, H6, H7, H8 e H9 passaram com 200/400 esperados e mensagens específicas. H10: nenhum endpoint/job de retry foi executado; não há cron configurado para handoff.
- **ICP-1–ICP-6:** todos passaram; ICP-1/2/3/4 recusados com 400; ICP-5 permitido com 200; ICP-6 confirmou campo vazio sem preenchimento automático.
- **Jornada inbound:** Suspect→pendente→aceito→Prospect→ICP sim→Lead Qualificado→Oportunidade, 200 em todas as etapas; `tipo_origem=inbound` preservado.
- **Jornada outbound:** Suspect→pendente→aceito→Prospect→ICP sim→Lead Qualificado→Sem timing com motivo/evidência, 200 em todas as etapas; `tipo_origem=outbound` preservado.
- **CA-1-10/regressão F1-T04:** vaga_aberta não virou ganho sem nova evidência; terminal sem motivo recusado; Lead Qualificado sem ICP recusado; origem outbound preservada. Regras anteriores permaneceram ativas.
- Foram usados 16 registros fictícios de teste com prefixo `F1T05-TEST-` e registros de regressão `F1T05-REG-`; todos foram removidos ao final.

## Schema e evidências

- Collection ao vivo `demandas`: migration 0005 aplicada; os dois campos têm tipo select, seleção única, não obrigatório e valores exatos autorizados.
- Nenhum terceiro campo; estados e fixtures originais preservados.
- Skip v0.0.28, hash `d72ec36`; QA: setup, análise estática, build, integrações e testes automáticos passaram.
- Working tree do Skip limpo após aplicação, exceto `.skip.config.json` com metadado interno `lastDevBuildRef`.

## Limitações e não alterado

- Não há histórico estruturado de retries; `evidencia` registra tentativas e `handoff_status` representa a situação atual.
- Redistribuição futura entre GNs não faz parte desta entrega.
- RD Station, 1CRM, integrações externas, contatos externos, metas, ICP aprovado, F1-T04 e F1-T06 não foram tocados.

**Próximo gate:** validação humana expressa do Champion. F1-T05 não deve ser marcada como concluída antes dessa validação.
