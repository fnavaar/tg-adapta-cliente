# Fixtures F3-T01 — Especificação dos cenários sintéticos (E1)

**Data:** 2026-10-09 · **Task:** F3-T01 · **Etapa:** E1 (autorizada pelo Champion em 09/10/2026 — início parcial)
**Natureza:** 100% sintética — empresas, pessoas, propostas e vagas fictícias; nenhum dado real, nenhuma integração externa, nenhuma publicação.
**Vocabulários:** exclusivamente os aprovados — `oferta_servico` ∈ {R&S, TMO, R&S + TMO} (default D1); `área` ∈ lista v1 de 13 áreas + "Não informado" provisório (default D2); estado do retorno ∈ {Em andamento, Perfis apresentados, Aguardando retorno do cliente, Substituição em andamento} (DECISÃO 08/10); resultado ∈ {Sem desfecho, Sucesso, Sem sucesso} (DECISÃO 08/10).
**Gate:** `lead qualificado` permanece BLOQUEADO (RN-F1-011/B3-MET-01) — os fixtures NÃO atravessam esse estado; a pendência é visível no card, jamais simulada como aprovada.
**Marco:** travessia `proposta → vaga aberta` exige `status_proposta=aceita` (F1-T04, inalterado); `data_conversao_comercial` autopreenchida e nunca sobrescrita.

---

## PIPE-F3-IN-001 — jornada inbound completa (R&S)

| Campo | Valor |
|---|---|
| record_id | PIPE-F3-IN-001 |
| tipo_origem | inbound |
| canal | site (fictício) |
| empresa | Serviços Delta Ltda. (fictícia) |
| contato | pessoa fictícia (sem dado pessoal real) |
| oferta_servico | R&S |
| estado inicial → final | suspect → prospect → oportunidade → proposta (aceita) → vaga aberta → ganho |
| handoff_status | pendente → aceito (suspect→prospect, conforme F1-T05) |
| icp_validado | sim (validação HUMANA simulada pelo papel GN — fixture) |
| lead_qualificado | NÃO atravessado — gate bloqueado; pendência visível registrada |
| responsável | GN fictício (dono provisório — B3-RACI-01) |
| proposta | nº PROP-IN-001; área = TI; serviço = R&S |
| vaga | nº VAGA-IN-001; área = TI; prazo operacional = data futura fictícia; capacidade = 1 |
| retorno da operação | eventos: Em andamento → Perfis apresentados (data fictícia) → Aguardando retorno do cliente → resultado Sucesso; motivo: contratação realizada (fictícia) |
| evidências por transição | dono, próxima ação, prazo e motivo em cada passo (RN-F1-007/008) |
| terminal | ganho com motivo e evidência de decisão (RN-F1-010 — nova evidência nesta atualização) |

## PIPE-F3-OUT-001 — jornada outbound completa (TMO)

| Campo | Valor |
|---|---|
| record_id | PIPE-F3-OUT-001 |
| tipo_origem | outbound |
| canal | linkedin (fictício) |
| empresa | Logística Ômega S.A. (fictícia) |
| contato | pessoa fictícia |
| oferta_servico | TMO |
| estado inicial → final | suspect → prospect → oportunidade → proposta (aceita) → vaga aberta → ganho |
| handoff_status | pendente → aceito |
| icp_validado | sim (humano, fixture) |
| lead_qualificado | NÃO atravessado — gate bloqueado; pendência visível |
| responsável | GN fictício (dono provisório) |
| proposta | nº PROP-OUT-001; área = Logística/Supply Chain; serviço = TMO |
| vaga | nº VAGA-OUT-001; área = Operações/Produção (área diferente da proposta — demonstra área por registro); prazo operacional = data futura fictícia; capacidade = 3 |
| retorno da operação | eventos: Em andamento → Perfis apresentados → resultado Sucesso; motivo: alocação efetivada (fictícia) |
| cenário de substituição (leitura, sem execução) | após o Sucesso, evento "Substituição em andamento" com motivo fictício de reposição SOS — resultado permanece Sucesso (DECISÃO 08/10); encerramento do ciclo NÃO simulado (D5 pendente) |
| terminal | ganho com motivo e evidência |

## PIPE-F3-STUCK-001 — oportunidade parada (escalonamento, leitura)

| Campo | Valor |
|---|---|
| record_id | PIPE-F3-STUCK-001 |
| tipo_origem | inbound |
| empresa | Consultoria Sigma Ltda. (fictícia) |
| oferta_servico | R&S |
| estado | oportunidade — sem resposta no prazo da próxima ação (vencido, data fictícia) |
| cenário previsto | pendência visível com dono provisório (Comercial/GN — B3-RACI-01) + caminho para terminal com motivo, conforme RN-F3-004 VIGENTE |
| limitação documental | as regras de recuperação do Champion (3 tentativas/90 dias/sugestão de sem timing — D6) NÃO constam da RN-F3-004; o fixture registra apenas a pendência com dono; NENHUMA lógica de tentativas/90 dias é implementada nesta etapa (E6 bloqueada) |
| terminal previsto | sem timing com motivo (após confirmação do Comercial — sem automação) |

---

## Cobertura dos cenários da SPEC (Resultado observável §1–3)

| Cenário da SPEC | Fixture | Status |
|---|---|---|
| §1 — caso inbound e outbound percorrem a jornada com dono/próxima ação/prazo/motivo | PIPE-F3-IN-001, PIPE-F3-OUT-001 | especificados |
| §2 — proposta/vaga devolve resultado da operação com estado, prazo/capacidade e motivo, origem rastreável | eventos de retorno nos dois fixtures | especificados (execução depende de E2/E5 — bloqueadas) |
| §3 — oportunidade parada tem prazo de escalonamento, estado e caminho terminal com motivo | PIPE-F3-STUCK-001 | especificado (execução depende de E6 — bloqueada) |

## Validações executadas nesta etapa (E1 — especificação)

1. **Vocabulários:** todos os valores usados pertencem às listas aprovadas (oferta_servico R&S/TMO; áreas da lista v1; estados do retorno e resultados da DECISÃO 08/10). ✔
2. **Gate lead qualificado:** nenhum fixture atravessa; pendência visível declarada em cada card. ✔
3. **Marco F1-T04:** travessia proposta→vaga exige status_proposta=aceita em ambos os fixtures; data_conversao_comercial autopreenchida. ✔
4. **Sem dado real:** empresas/pessoas/datas 100% fictícias; sem contato real, sem integração, sem publicação. ✔
5. **Sem estrutura nova:** nenhum campo/estado além dos já decididos; D4/D5/D6 sem default inseguro — as partes dependentes ficam apenas ESPECIFICADAS, não implementadas. ✔

## Pendências que estas especificações NÃO resolvem (por design)

- D4: onde "estado do retorno" persiste — os eventos acima são lógicos; a persistência física (coleção × log) aguarda emenda.
- D5: encerramento do ciclo de substituição — o cenário para em "Substituição em andamento" com motivo, sem valor de encerramento.
- D6: regras de recuperação — o fixture STUCK usa apenas a RN-F3-004 vigente (pendência + dono provisório + caminho terminal com motivo).
