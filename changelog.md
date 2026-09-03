# Changelog — Projeto TG Mais Serviços de Tecnologia e RH LTDA

> Registro de tudo que acontece no projeto, em ordem cronológica inversa (mais recente no topo).
> Formato: `- AAAA-MM-DD · [quem] · o que aconteceu`
> **Dúvidas para o consultor** entram como: `- AAAA-MM-DD · [quem] · DÚVIDA: …` — ele responde
> na próxima sincronização.

## Registro

- 2026-09-03 · Champion (João Paulo) · F1-T06 CONCLUÍDA E VALIDADA HUMANAMENTE — aprovação expressa às 09:26 após revisão do painel real, reconciliação painel×fonte com diferença zero, filtros, record_id/reprocessamento, regressões F1-T01 a F1-T05, rollback controlado e limpeza. Fase 1 encerrada: 6/6 (100%). Pendência arquitetural de identidade técnica/UNIQUE permanece para fase futura; próxima fase não iniciada.
- 2026-09-01 · Champion (João Paulo) · F1-T05 CONCLUÍDA E VALIDADA HUMANAMENTE — aprovação expressa às 18:32 após revisão da implementação, migration 0005, handoff/ICP, testes H1-H10, ICP-1 a ICP-6, jornadas inbound/outbound, regressão F1-T04, artefato, emenda append-only e limitações. Fase 1: 5/6 (83%). F1-T06 não iniciada e permanece aguardando autorização expressa.
- 2026-09-01 · Adapta (Pepe) · CONCLUSÃO DOCUMENTAL DA F1-T05 — emenda append-only da SPEC registrada com handoff_status, icp_validado e validação humana do ICP; retry exclusivamente manual; testes H1-H10, ICP-1 a ICP-6, jornadas inbound/outbound e regressão F1-T04 documentados; ausência de histórico estruturado de retries e canal indisponível não demonstrável tecnicamente registrados. F1-T05 permanece AGUARDANDO VALIDAÇÃO HUMANA DO CHAMPION; F1-T06 não iniciada.
- 2026-09-01 · Adapta (Pepe) · F1-T05 IMPLEMENTADA — migration 0005 adicionou somente handoff_status e icp_validado; hook atualizado com handoff, proteção do aceite, retry manual e gate humano de ICP. Testes H1-H10, ICP-1 a ICP-6, jornadas inbound/outbound, CA-1-10 e regressão F1-T04 executados via API real; registros fictícios removidos. Skip v0.0.28 (QA ok). F1-T05 AGUARDANDO VALIDAÇÃO HUMANA DO CHAMPION; F1-T06 não iniciada. Evidência: 04-fase-atual/pipeline-f1-f1-t05.md.
- 2026-09-01 · Champion (João Paulo) · VALIDAÇÃO HUMANA APROVADA — F1-T04 CONCLUÍDA. Critérios atendidos; F1-T05 não iniciada antes de autorização expressa.
- 2026-09-01 · Adapta (Pepe) · CORREÇÃO LIMITADA F1-T04 aplicada: autopreenchimento/preservação de data_conversao_comercial, BadRequestError específico e nova evidência para vaga_aberta→ganho. Skip v0.0.27.
- 2026-08-31 · Adapta (Pepe) · F1-T04 IMPLEMENTADA com migration 0004 e hooks; aguardava validação humana.
- 2026-08-31 · Champion (João Paulo) · Emenda aprovada: Suspect é estado de entrada sem obrigação de responsável, próxima ação e prazo; a partir de Prospect, os 3 são obrigatórios.
- 2026-08-31 · Champion (João Paulo) · Unidade comercial corrigida para EMPRESA; sem grupo_economico.
- 2026-08-27 · Champion (João Paulo) · F1-T03 concluída e aprovada: baseline, metas, gate, dicionário comercial e definição de Lead Qualificado.
- 2026-08-25 · Champion (João Paulo) · Decisões comerciais consolidadas: baseline, metas, critério de conquista e ICP 2026.
- 2026-08-19 · Adapta · Pasta operacional preparada; Fase 1 liberada para execução controlada.
