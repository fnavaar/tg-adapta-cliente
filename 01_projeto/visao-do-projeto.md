# Visão do projeto — TG Mais Serviços de Tecnologia e RH LTDA

> O mapa completo do programa: por que ele existe e o arco das 5 fases. O detalhe de cada fase
> chega em `04_fase-atual/` quando ela abre — uma por vez, por estratégia de implementação.
> Mantido pela consultoria. Atualizado em 22/10/2026.

## Por quê

- **Objetivo de negócio:** aumentar a geração de demanda e de vagas abertas (hoje 37; capacidade relatada de
  60–70), com um sistema que mostre de onde cada demanda vem, por onde passa e onde para.
- **Processo crítico atacado:** geração de demanda inbound/outbound, qualificação, proposta, vaga e
  passagem para a operação.
- **Onde o sistema vive:** projeto Skip **"repositório adapta"**, construído e operado a partir do
  **Maestro**.
- **Métrica de sucesso:** baseline relatado de 37 vagas abertas; alvo, fórmula e período dependem da
  decisão da direção (pendente).

## O arco das 5 fases

| Fase | Entrega (em uma linha) | O que vocês vão ver | Status |
|---|---|---|---|
| 1 | Dicionário, baseline e pipeline/painel mínimo | Painel com as demandas por etapa e origem | ✅ concluída (6/6) |
| 2 | Campanhas, experimentos, captura e atribuição | Cadastro de experimentos, decisão por qualidade e leitura de teste da Meta | ✅ concluída (9/9) |
| 3 | Funil, painéis e passagem entre áreas | Tela **Funil** (Kanban com origem e história de cada lead), tela **Campanhas** (Meta Ads), tela **Gargalos**, **Passagens pendentes** e área separada do DHO | 🟡 atual (13 tasks) |
| 4 | Otimização assistida e primeiro loop | Tela **Recomendações da semana**, gerada por automação semanal no Maestro, com aprovação humana; campanhas de LinkedIn/Google se o conector for validado | planejada |
| 5 | Aprendizagem, validação e segundo loop ponta a ponta | Roteiro visual para a diretoria (Funil → Campanhas → Recomendações → resultado) e validação de tudo | planejada |

O detalhe de cada fase (specs, tasks, critérios) é preparado pela consultoria **durante a fase
anterior**, incorporando o que o projeto aprendeu no caminho — por isso só a fase aberta tem
specs neste repositório. Integrações com RD Station, 1CRM e Omie não fazem parte deste projeto.
