# AP-2026-09-21-0831 — Detector de qualidade: evidência positiva ≠ marcador de ausência

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F2-T05 / SPEC F2-003 (RN-F2-009)
- Sinal: a regra que bloqueia "clique isolado" passou a bloquear o GREEN porque o texto continha "0 oportunidades" junto de "1 lead qualificado sintético"; o marcador numérico de ausência foi tratado como ausência total de qualidade
- Evidência: TDD visível 4/6 na v0.0.77; 6/6 na v0.0.78 após separar evidência positiva de qualidade (lead qualificado, oportunidade, proposta, conversão, cliente) de marcadores de ausência
- Regra reutilizável: em detectores de qualidade por texto, testar primeiro a existência de evidência positiva; quantidade zero de métrica secundária não anula evidência positiva presente
- Quando aplicar: validações de evidência em decisões/atribuições (a F2-T06 usará critérios reais)
- Quando não aplicar: quando a regra de negócio exigir mínimo simultâneo de múltiplas métricas — nesse caso a exigência é explícita, não heurística
- Confiança: alta — reproduzida e corrigida com TDD visível
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
