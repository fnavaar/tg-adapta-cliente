# STATUS — Projeto TG Mais Serviços de Tecnologia e RH LTDA

> **Atualizado em:** 2026-09-22 · **Por:** Adapta / Champion  
> O painel do projeto: fase atual, progresso e o que precisa de atenção.

## Onde estamos

- **Fase atual:** 2 — Sistema de campanhas e experimentação de Growth Marketing (LIBERADA PARA EXECUÇÃO).
- **Task ativa:** F2-T09 — análise de elegibilidade concluída; aguardando autorização de implementação.
- **Task anterior:** F2-T08 concluída e validada em 2026-09-21.
- **Progresso:** 8 de 9 tasks concluídas (89%); F2-T09 elegível para implementação controlada, ainda não implementada.

## Reavaliação da F2-T09

- Gates 1 a 5 atendidos: ativos identificados; owner e acesso parcial de leitura comprovados; contrato de campos/política aprovados; chave `sistema_origem_tecnico + record_id` aprovada; payload sintético aprovado.
- T07 e T08 aceitas e preservadas.
- F2-T09 está **elegível**, mas a autorização de implementação ainda não foi concedida.
- CA-2-11 e CA-2-12 no recorte real continuam pendentes.

## Resultado preservado da F2-T08

- Relatório de fechamento: `05_entregas/fase-2/f2-t08/relatorio-fechamento.md`.
- Produto funcional: Skip v0.0.85, hash `25c717a`, preservado durante o fechamento.
- T04: 7/7; T08: 8/8; bateria humana: 5/5.
- Lote `META-F2-MANUAL-001`: 5 linhas, 100% sintético, `manual_export`, sem dados pessoais.
- Idempotência: replay `skip`; payload diferente com mesmo `batch_id` → conflito/bloqueio/decisão humana.
- Falhas 401/403/429/timeout/payload inválido simuladas, sem chamada externa, sem retry automático.
- `demandas`: 10 registros; migrations até 0020; collections preservadas.

## Gate atual

**Autorização de implementação ausente.** A única próxima ação é aguardar autorização expressa do Champion para executar o plano da F2-T09.

## Plano resumido aguardando autorização

- Reutilizar o núcleo T04/T08.
- Fazer uma única leitura Meta limitada, somente dos campos aprovados.
- Normalizar em dry-run com identidade `(meta_ads, record_id)`.
- Reconciliar quantidade, IDs, duplicidade, conflito e campos ausentes.
- Não escrever em `demandas`, não criar leads e não alterar campanhas, orçamento ou criativos.
- Executar QA, regressão e teste humano antes de qualquer conclusão.

## Pendências preservadas

- CA-2-11 e CA-2-12 real ainda não executados.
- Leitor dedicado tem acesso parcial na conta, mas controle total do portfólio; ressalva de governança registrada para rollback.
- Agência externa permanece com acesso de escrita na conta de anúncios.
- Nenhuma relação estrutural `demandas` ↔ `experimentos_f2` foi criada.
- F2-T09 não está concluída; aguarda autorização de implementação.
