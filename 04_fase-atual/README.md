# Fase atual — Fase 3

Esta pasta contém as SPECs e tasks da Fase 3 do projeto TG Mais. A Fase 2 encerrada está arquivada em
`05_entregas/fase-2/`, com evidências e manifesto de encerramento.

- `fase.md`: explicação da fase em linguagem simples, ordem recomendada, Jornada e tabela operacional (13 tasks).
- `00-Tasks_Gerais.md`: tabela operacional com "Onde executar" e "O que você vai ver" de cada task.
- `matriz-de-rastreabilidade.md`: origem, SPEC, critérios, provas e bloqueios.
- `specs/`: F3-001 pipeline integrado, F3-002 gargalos, F3-003 passagens entre áreas, F3-004 sinais do DHO,
  **F3-005 Funil (Kanban)** e **F3-006 Campanhas Meta via Maestro** (novas em 22/10/2026).

## Estado

- **Champion:** João Paulo.
- **Em andamento:** F3-T01 (E2 implementada em 22/10/2026, aguardando teste humano).
- **Próxima depois da F3-T01:** F3-T09 — diagnóstico no Maestro das automações, do destino dos leads e das campanhas.
- **Teste:** cada task exige provas da SPEC e teste humano antes da seguinte.
- **Como o Maestro trabalha:** explica a fase, a task atual e a próxima; combina cada passo; pede para
  conferir no Skip; fecha com resumo (protocolo no `CLAUDE.md`).

Bloqueios nomeados: B3-META-01 (só métricas de campanha pela F3-006), B3-META-LEITOR, B3-LGPD-01,
B3-ID-01, B3-MET-01, B3-RACI-01 e B3-DHO-01 — detalhes em `fase.md`.
