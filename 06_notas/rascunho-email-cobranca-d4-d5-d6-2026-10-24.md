# Rascunho — E-mail da cobrança D4/D5/D6 (para aprovação do Champion antes do envio)

**De:** luizcmanni@gmail.com (conta do Luiz — envio manual de gestão)
**Para:** Ramon Pádua (consultor técnico da Adapta)
**Cc:** Izabel (gestão do projeto)
**Assunto:** Adapta — cobrança de devolutiva: pacote de harmonizações da F3-T01 (D4/D5/D6) — prazo 31/10

---

Ramon,

Em primeiro lugar, parabéns pela assunção do projeto — a documentação das últimas calls está clara.

Preciso, porém, cobrar uma devolutiva que está pendente há 16 dias: o pacote único de harmonizações da F3-T01 (06_notas/f3-t01-pacote-harmonizacoes-2026-10-08.md, commit d691404), encaminhado em 08/10/2026 ao então consultor Navaar, segue sem resposta. Com a sua transição para o projeto, a responsabilidade pela resposta passa a ser sua.

Para desbloquear a F3-T01, preciso de uma emenda datada respondendo, em lote único:

1. **D4 — Persistência do "estado do retorno"** (SPEC F3-001, contrato Operação → retorno, linha 43): onde esse estado persiste — campo da coleção propostas/vagas ou atributo do log de eventos? Sem isso, não criamos as coleções (risco de retrabalho de schema) e ficam bloqueadas 8 tasks, incluindo o Funil (T10/T11), que é a entrega que a direção aguarda.

2. **D5 — Encerramento do ciclo de substituição**: como uma substituição concluída se encerra no "estado do retorno" — valor adicional na lista fechada versionada (com motivo) ou outro mecanismo dentro dos campos e eventos existentes? Bloqueia a etapa E5.

3. **D6 — Regras de recuperação comercial (RN-F3-004)**: incorporar à SPEC as regras que decidi em 24/09/2026 — recuperação limitada a 3 tentativas e 90 dias corridos; tentativa = ação humana registrada; ao atingir o limite, sugestão de "sem timing" com confirmação do Comercial (nunca encerramento automático); recusa explícita = "perdido" com motivo; resposta do cliente = Comercial encerra o escalonamento. Bloqueia a etapa E6.

O documento completo da cobrança está no repositório: 06_notas/cobranca-d4-d5-d6-consultor-2026-10-24.md. Se houver itens do pacote de 08/10 ainda sem confirmação documental (D1–D3), podem entrar na mesma emenda.

**Prazo sugerido: 31/10/2026.** É sugestão minha para não travar o ciclo semanal — a prioridade acordada em 08/10 permanece (D4/D2 antes das migrations; D3 antes das regras de transição; D5 antes da etapa de retorno).

Enquanto a devolutiva não chega, a Fase 3 avança pelas tasks não bloqueadas (F3-T12/T13 — Campanhas Meta), e as tasks dependentes da F3-T01 permanecem bloqueadas sem falha atribuída ao time. Sua resposta destrava em cascata o Funil.

Coloco-me à disposição para qualquer esclarecimento.

Abraço,
Luiz Carlos Manni
Diretor de Marketing e Finanças — Talent Group
www.talentgroup.com.br | 11 4052-4300

---
*Rascunho preparado pelo Maestro em 24/10/2026 com autorização documental do Champion. ENVIO SOMENTE APÓS APROVAÇÃO EXPRESSA DO CHAMPION (item 4 da decisão de 24/10). Conta de envio: luizcmanni@gmail.com (padrão do Luiz para gestão); a conta talentgroupepress@gmail.com é a oficial de automações/hooks.*