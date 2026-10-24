# Cobrança formal — devolutiva do pacote D4/D5/D6 (F3-T01)

**Data:** 2026-10-24 · **De:** Champion/owner (Luiz Carlos Manni) via Maestro · **Para:** Ramon Pádua (consultor técnico da Adapta) · **Ciência:** Izabel (gestão do projeto) · João Paulo (Champion)

## Contexto

O pacote único de harmonizações da F3-T01 — `06_notas/f3-t01-pacote-harmonizacoes-2026-10-08.md` (commit `d691404`, encaminhado ao então consultor Navaar em 08/10/2026) — **está sem devolutiva há 16 dias**. Com a transição de consultoria (Ramon assume desde a 5ª call de 22/10, conforme assinatura do STATUS e publicações da call), esta cobrança transfere a responsabilidade da resposta ao consultor atual.

O Champion determinou em 24/10: o projeto não pode ficar parado aguardando indefinidamente as emendas. Enquanto a devolutiva não chega, a sequência da Fase 3 avança pelas tasks não bloqueadas (F3-T12/T13 — SPEC F3-006), e as tasks dependentes da F3-T01 permanecem bloqueadas.

## O que o consultor precisa responder (lote único, protocolo anti-trava)

### D4 — Persistência do "estado do retorno" (SPEC F3-001, contrato Operação → retorno, linha 43)

**Pergunta:** onde o "estado do retorno" persiste — campo da coleção (`propostas`/`vagas`) ou atributo do log de eventos?

**Impacto de estar pendente:** bloqueia a criação das coleções `propostas`/`vagas` (etapa E2-coleções da F3-T01) — risco alto de retrabalho de schema se criado sem a emenda. Em cascata, bloqueia **8 tasks**: F3-T10/T11 (Funil — a tela prioritária da direção), F3-T03/T04 (Gargalos), F3-T05/T06 (Handoff), F3-T07/T08 (DHO) e F3-T02.

### D5 — Encerramento do ciclo de substituição (estado do retorno)

**Pergunta:** como uma substituição concluída se encerra no "estado do retorno" — (a) valor adicional na lista fechada versionada (ex.: "Substituição encerrada", com motivo obrigatório distinguindo reposição efetivada de posição encerrada sem reposição) ou (b) outro mecanismo dentro dos campos e eventos existentes?

**Impacto de estar pendente:** bloqueia a etapa E5 da F3-T01 (retorno/escalonamento). Sem a emenda, uma substituição concluída permaneceria exibida indefinidamente como "Substituição em andamento".

### D6 — Regras de recuperação comercial (RN-F3-004)

**Pergunta:** incorporar à RN-F3-004 (ou regra correlata da SPEC F3-001) as regras decididas pelo Champion em 24/09/2026: recuperação limitada a 3 tentativas e 90 dias corridos; tentativa = ação humana registrada; ao atingir o limite, sugestão de "sem timing" com confirmação do Comercial (nunca encerramento automático); recusa explícita = "perdido" com motivo; resposta do cliente = Comercial encerra o escalonamento.

**Impacto de estar pendente:** bloqueia a etapa E6 da F3-T01 (recuperação de oportunidade parada). O fixture STUCK registra apenas pendência com dono provisório conforme a RN-F3-004 vigente.

## Prazo sugerido

Resposta em lote único (uma emenda datada respondendo D4, D5 e D6 — e, se aplicável, os demais itens D1–D3 do pacote de 08/10 que seguem sem confirmação documental) **até 31/10/2026**. A data é sugestão do Champion para não travar o ciclo semanal; a prioridade acordada em 08/10 permanece: D4/D2 antes das migrations; D3 antes das regras de transição; D5 antes da etapa de retorno.

## Consequência da não resposta

A sequência recomendada (F3-T12 → F3-T13) segue independentemente; F3-T01 e suas dependentes permanecem bloqueadas sem falha atribuída ao time. A devolutiva destrava em cascata o Funil — a entrega que a direção aguarda.

---
*Documento gerado pelo Maestro em 24/10/2026, com autorização documental do Champion (somente análise e planejamento). Registro correspondente no changelog em formato DÚVIDA ao consultor.*