# Constituição do projeto — TG Mais Serviços de Tecnologia e RH LTDA

> Regras estáveis deste projeto. Valem em todas as fases e só mudam por decisão registrada da
> consultoria (emenda datada na seção final). Mantida pela consultoria — dúvida vira registro
> no `changelog.md`, não edição. (Conceito adaptado do Spec Kit, decisão D18.)

## Papéis

- **Champion:** João Paulo — executa as tasks da fase atual e valida com evidência.
- **Consultor Adapta:** equipe Adapta — define escopo, SPECs e critérios; fecha as fases.
- **Agente (Claude):** guia a execução dentro destas regras; não legisla sobre escopo.

## Stack e ferramentas permitidas

- CRM atual e seus dados autorizados; arquivos CSV/planilhas de fallback; canais e fontes de demanda
  somente quando aprovados para a task.
- Dependência ou ferramenta nova só entra por decisão do consultor — registre `DÚVIDA:` antes.

## O que o champion pode e não pode tocar

- **Pode:** `04_fase-atual/` conforme as instruções da task, evidências autorizadas e a superfície de
  registro validada para a fase.
- **Não pode:** specs, `fase.md` (além de marcar tasks), `01_projeto/`,
  sistemas de produção críticos ou dados pessoais fora do recorte autorizado.

## A SPEC é lei

Toda implementação segue o critério de aceite e o TDD da SPEC — nem menos (critério reprovado),
nem mais (**o aceite é teto**: código além do aceite é superfície não verificada, D17). O que
não está na SPEC da fase não se implementa: vira `DÚVIDA:` para o consultor decidir.

## Linha vermelha (nunca simplificar)

Validação de entrada em fronteira de confiança; tratamento de erro que evita perda de dados;
segurança; acessibilidade; LGPD/dados pessoais. Corte nessas áreas reprova a task — sem exceção e
sem julgamento de mérito (D17).

## Dívida deliberada

Simplificação intencional leva marca no ponto exato da decisão:
`adapta-divida: <teto atual>; <upgrade quando gatilho>`. O consultor acompanha essas marcas na
sincronização — é o combinado do método.

## Dúvidas e insumos — nunca travam (protocolo anti-trava, 2026-10-07)

- Uma ambiguidade da SPEC **não congela a task**: o agente registra `DÚVIDA:` no `changelog.md`,
  adota o **default conservador documentado na própria task** (massa sintética, sem dado real,
  sem integração externa, sem conceito novo de negócio) e continua a execução até onde a SPEC
  permite.
- A **resposta do Champion** (registrada no `changelog.md`) é **final e definitiva**, mesmo quando
  a origem da informação for outra pessoa — não se exige confirmação da fonte.
- **Insumo faltante vira pergunta embutida no card da task** dirigida ao Champion, nunca um
  bloqueio que para o projeto.
- **Emendas documentais** continuam sendo responsabilidade da consultoria, publicadas **em lote
  único** por rodada (com varredura das SPECs afetadas), não uma emenda por dúvida.
- Continuam parando de verdade apenas: linha vermelha; exigência de dado real sem autorização;
  integração externa; mudança de escopo/critério/aceite; e ação externa (produção, push,
  publicação).

## Emendas

| Data | O que mudou | Decisão/motivo |
|---|---|---|
| 2026-10-07 | Protocolo anti-trava (dúvidas/insumos nunca congelam task; resposta do Champion é final; pergunta embutida no card; emendas em lote) | Decisão do consultor (Navaar), 07/10/2026 — encerrar ciclo de validações repetidas na F3 |
| 2026-10-07 | Emendas E-F3-001-02 (prazos sem SLA autônomo) e E-F3-003-01 (prazo de aceite do handoff) publicadas nas SPECs F3 | Resposta à DÚVIDA de 06/10 + varredura preventiva das 4 SPECs da F3 |
