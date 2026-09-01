# AP-2026-09-01-1835 — Campos opcionais com semântica explícita no handoff e ICP

- Status: candidato
- Escopo: projeto do cliente
- Task/SPEC: F1-T05 / SPEC-F1-002
- Sinal: campos select opcionais representam estados distintos quando vazios ou preenchidos; as transições de handoff e qualificação precisam validar a semântica do valor atual sem inferência automática.
- Evidência: migration 0005 aplicada com `handoff_status` e `icp_validado`; testes H1-H10 e ICP-1 a ICP-6 passaram via API real; schema confirmado no Skip Cloud.
- Regra reutilizável: para campos opcionais de decisão humana, documentar explicitamente o significado do vazio e bloquear transições incompatíveis com mensagens específicas; não inferir decisão nem criar automação implícita.
- Quando aplicar: ao adicionar gates manuais ou estados auxiliares opcionais em novas tasks do pipeline.
- Quando não aplicar: não usar para transformar ausência de análise em recusa, desqualificação ou retry automático.
- Confiança: alta — regra sustentada por migration, schema e testes API observáveis.
- Privacidade: sem segredo, dado pessoal ou conteúdo bruto
