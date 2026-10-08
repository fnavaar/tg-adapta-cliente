# Pacote Único de Harmonizações — F3-T01

**Data:** 2026-10-08
**Origem:** Champion/owner da Talent Group — coleta de decisões de negócio da F3-T01 encerrada em 08/10/2026.
**Destinatário:** Consultor Adapta (Navaar).
**Protocolo:** resposta em **lote único**, mediante emenda datada à SPEC F3-001, conforme o protocolo anti-trava (AGENTS.md + Constituição, 07/10/2026). As decisões de produto pertencem à Talent Group e já estão registradas no changelog; este documento **consolida** as cinco solicitações documentais em uma única entrega — não são solicitações separadas. Nada foi implementado; a implementação da F3-T01 aguarda autorização expressa do Champion.

---

## D1 — Vocabulário de serviço ("R&S/Alocação/SOS")

- **Decidido (negócio, changelog 07/10):** `oferta_servico` mantém exclusivamente R&S / TMO / R&S + TMO (padrão homologado F1/F2). SOS = "Serviço Orientado a Substituições" (reposição em até 10 dias, HumanGuide, handover) — processo **dentro** da operação de alocação/terceirização, **não** é uma terceira oferta_servico.
- **Depende de confirmação documental:** harmonizar a redação "R&S/Alocação/SOS" (linhas 20, 29 e 41 da tabela de dados da SPEC F3-001): esses termos designam a **operação que devolve o retorno**, não valores do campo serviço.
- **Risco se não harmonizado:** fixtures e textos de TDD da etapa inicial usariam vocabulário divergente da SPEC.
- **Referência no changelog:** DÚVIDA de 2026-10-07.

## D2 — Definição do campo "área" e lista fechada v1

- **Decidido (negócio, changelog 07–08/10):** área = **departamento funcional do cargo da vaga** (não o segmento da empresa cliente, não a classificação composta do 1CRM). Lista fechada v1 versionada com 13 áreas: TI, Comercial/Vendas, Logística/Supply Chain, Projetos/PMO, Engenharia/Manutenção, Financeiro/Contábil, Administrativo, Marketing, Recursos Humanos, Operações/Produção, Educacional/Acadêmico, Auditoria/Riscos, Laboratorial/Saúde. "Não informado" = condição provisória de informação desconhecida (confirmação humana, sem inferência), não área funcional definitiva.
- **Depende de confirmação documental:** emenda incorporando à SPEC a definição do campo e a lista fechada v1 versionada (com "Não informado" como condição provisória).
- **Risco se não harmonizado:** campo/schema das coleções e formulários teriam de ser refeitos.
- **Referência no changelog:** DECISÃO de 2026-10-07, DÚVIDA de 2026-10-07, DECISÃO de 2026-10-08.

## D3 — RN-F3-002 × "Não informado"

- **Decidido (negócio, changelog 08/10):** área desconhecida é registrada como "Não informado" — sem inferência, sem bloquear o avanço do registro, sem criar mecanismo automático de pendência/escalonamento novo nesta T01; confirmação é responsabilidade humana.
- **Depende de confirmação documental:** a coluna de exceção da RN-F3-002 define pendência apenas para vaga sem número/serviço; a SPEC não define o comportamento com área ausente. Solicitamos harmonização da RN-F3-002 (ex.: "área informada ou Não informado") ou regra equivalente, sem pendência automática nova.
- **Risco se não harmonizado:** regras de transição e casos RED/GREEN do TDD ficariam ambíguos.
- **Referência no changelog:** DÚVIDA de 2026-10-08.

## D4 — Persistência do "estado do retorno" nas coleções propostas/vagas

- **Decidido (negócio, changelog 08/10):** "estado do retorno" (situação do trabalho da operação: Em andamento, Perfis apresentados, Aguardando retorno do cliente, Substituição em andamento) e "resultado" (desfecho efetivo: Sem desfecho, Sucesso, Sem sucesso) são **campos distintos**, conforme o contrato "Operação → retorno" (linha 42). O estado evolui por eventos no log append-only ("novo evento = novo registro"); ausência de retorno não gera evento artificial.
- **Depende de confirmação documental:** o contrato das coleções relacionadas (linha 43) lista nº/serviço/área/prazo operacional/resultado/motivo/evidência e **omite "estado do retorno"**. Solicitamos: (a) confirmar os dois campos no contrato de `propostas`/`vagas`; (b) definir onde o estado do retorno persiste — campo da coleção ou atributo do log de retornos.
- **Risco se não harmonizado:** **alto** — schema das coleções/migrations teria de ser refeito; a harmonização deve preceder a criação das coleções.
- **Referência no changelog:** citada na DÚVIDA de 2026-10-08 (lote único) e na DECISÃO consolidada de 2026-10-08; texto completo neste pacote.

## D5 — Encerramento do ciclo de substituição

- **Decidido (negócio, changelog 08/10):** substituição (garantia R&S / reposição SOS TMO) é acompanhada **na mesma vaga** por eventos históricos; o resultado original "Sucesso" permanece preservado; nada é criado automaticamente; nova posição comercial somente por decisão humana do Comercial; substituição não concluída = operação registra o ocorrido com motivo e evidência, sem reescrever o resultado histórico.
- **NÃO aprovado:** o valor adicional "Substituição encerrada" **permanece como dúvida** — não é regra definitiva.
- **Depende de confirmação documental:** a lista v1 de estado do retorno não possui valor de encerramento — uma substituição concluída (com ou sem êxito) permaneceria exibida indefinidamente como "Substituição em andamento". Solicitamos: (a) valor adicional na lista fechada versionada (ex.: "Substituição encerrada", com motivo obrigatório distinguindo "reposição efetivada" de "posição encerrada sem reposição") — valor de lista, não estrutura nova; ou (b) outro mecanismo dentro dos campos e eventos existentes, sem novas estruturas ou automações.
- **Risco se não harmonizado:** lógica de retorno/escalonamento e cenários de TDD do ciclo de substituição teriam de ser refeitos.
- **Referência no changelog:** DÚVIDA de 2026-10-08 + DECISÃO consolidada de 2026-10-08.

---

## Prioridade sugerida para a resposta em lote único

1. **D4 e D2 antes da criação das coleções** (migrations) — risco de retrabalho de schema.
2. **D3 antes das regras de transição e do TDD.**
3. **D1 antes da confecção dos fixtures.**
4. **D5 antes da etapa de retorno da operação/escalonamento** — ou instrução explícita de default conservador para o cenário de substituição, registrada como pendência visível.

Todas as cinco podem ser respondidas em uma única emenda à SPEC F3-001 (ou emenda + apêndice), preservando integralmente as decisões de produto já aprovadas. A decisão de produto pertence à Talent Group; a emenda documental é responsabilidade da consultoria conforme a Constituição do projeto.
