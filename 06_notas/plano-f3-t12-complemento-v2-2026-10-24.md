# Complemento do plano F3-T12 v2 — seções 10 a 14 · SPEC F3-006

**Data:** 2026-10-24 · **Arquivo principal:** 06_notas/plano-f3-t12-campanhas-meta-2026-10-24.md (seções 1–9) · **Status:** PLANO — não implementado; aguarda autorização específica de execução do Champion.

## 10. Inventário das funcionalidades do Hub 57113 — o que se preserva e o que se substitui

| Funcionalidade do Hub | O que faz hoje | Destino na F3-T12 |
|---|---|---|
| `meta_ads_sync` → `daily_metrics`/`campaigns`/`ad_sets`/`ads` | Sync de métricas (14d) e agregação 7d vs 7d anterior | **Substituído** pelo snapshot diário em `campanhas_meta`. A agregação comparativa 7d×7d NÃO faz parte da SPEC F3-006 |
| `maestro_daily` (cron 11h UTC / 08h BRT) | Relatório diário: recomendações determinísticas (ROAS<1 crítico, ROAS<2, CTR<1%, CPC>3, freq>3, ativa sem gasto) + e-mail HTML (manni+jpaulo) + post no chat do Genie + registro em `maestro_runs` | **Sem equivalente na SPEC F3-006** (somente leitura + tela). O relatório por e-mail e as recomendações exigem decisão do Champion antes de qualquer desligamento (critério 4 da §7) |
| `maestro_watchdog` (15min) | Aviso de recomendação pendente >60min (chat + e-mail 1x/dia) | **Sem equivalente** — funcionalidade do Maestro do Hub; decisão do Champion antes do desligamento |
| `MaestroCard` no Dashboard + `genie_history` | Aprovar/rejeitar recomendações e histórico no chat | **Sem equivalente** — otimização/escrita não faz parte da F3-T12 |
| `meta_connections` + token longo TalentGroup_01 | Conexão Meta server-side (token expira ~14/12/2026) | **Substituída** por `conexao_meta` OAuth do leitor dedicado (Opção A) no 51414 |
| Histórico: `maestro_runs`, `maestro_recommendations`, `daily_metrics` (163 duplicatas), `campaigns` | Histórico de execuções, recomendações e métricas | **PERMANECE no Hub como histórico** — nada migrado; validação cruzada opcional |
| `google_connections`, `calendar_events`, `gmail_messages` | Integrações Google/Calendar/Gmail | **FORA do escopo** da F3-T12 (SPEC só Meta) — permanecem no Hub |

**Conclusão:** a F3-T12 substitui o sync de métricas e a conexão Meta; NÃO substitui o relatório diário por e-mail, as recomendações determinísticas nem o watchdog — essas funcionalidades continuam existindo só no Hub e exigem decisão expressa do Champion antes de qualquer desligamento (§7, critério 4). Nada é apagado ou migrado do Hub.

## 11. Regras de conciliação com o Gerenciador de Anúncios

- **Período:** data de referência = **dia anterior completo (D-1)**. Execução manual pode capturar o dia corrente, sempre com a data de referência gravada; conciliação oficial só contra dia completo.
- **Fuso horário:** o fuso da CONTA Meta (TalentGroup_01 = America/Sao_Paulo; confirmar na implementação lendo `account_timezone` e registrando em `conexao_meta`). A API agrega dias no fuso da conta — a conciliação usa o mesmo fuso da conta, nunca o do servidor.
- **Atribuição:** volume (impressões, cliques, gasto) não depende de janela. "Resultados" depende — a janela usada é gravada no snapshot (`atribuicao_janela`); default **7d_click** (padrão unificado da Meta), ajustável se o Gerenciador usar outra na coluna; a conciliação compara sempre com a MESMA janela configurada nas colunas do Gerenciador.
- **Métricas:** gasto (spend, R$), impressões, cliques e resultados do objetivo; CTR/CPC/CPM são **derivados** (calculados de impressões/cliques/gasto) — não conciliados diretamente.
- **Nível de agregação:** por **campanha** (`level=campaign`, `time_increment=1`, `time_range` do dia de referência) — mesmo nível da tabela principal do Gerenciador.
- **Regra de divergência:** se o Gerenciador mostrar número diferente, verificar (a) data de referência e fuso, (b) janela de atribuição da coluna, (c) status efetivo da campanha. Conciliação aceita = valores iguais com os três parâmetros alinhados.

## 12. Política de credenciais Meta (armazenamento, acesso, expiração, renovação)

- **Armazenamento:** token server-side no backend do 51414, campo oculto (molde `meta_connections` do Hub). Nunca em chat, e-mail, changelog ou documento.
- **Acesso:** exclusivamente hooks/automações server-side do 51414; nenhum token exibido no frontend; logs mascarados (nunca imprimem o token).
- **Permissões:** leitor dedicado com "Ver desempenho" (ads_read); escopos OAuth somente leitura; sem qualquer escopo de escrita.
- **Expiração:** token de usuário Meta ~60 dias; `conexao_meta` registra status/desde/ultima_execucao; faixa de aviso + e-mail quando expirada.
- **Renovação:** o leitor dedicado refaz o consentimento OAuth na tela do sistema (login Meta → consentimento → callback server-side grava novo token); sem colar token no chat (condição da homologação da F3-T09); renovação testada antes de qualquer desligamento do Hub.
- **Revogação:** leitor desativado → conexão entra em estado "expirada" (faixa + e-mail), sem dado novo; último snapshot bom preservado.

## 13. Critérios objetivos — 3 dias consecutivos sem falha

Contador válido quando, em 3 dias consecutivos de execução agendada:

1. **3 execuções com status ok** (sem erro de API, timeout, conexão expirada ou gravação parcial);
2. **Data de referência correta** em cada snapshot (D-1 completo);
3. **0 duplicatas** (0 violações do índice único);
4. **`conexao_meta` ok** nas 3 execuções;
5. **0 e-mails de falha** nos 3 dias;
6. **Tela Campanhas** exibindo os dados das 3 execuções com hora de atualização correta.

**Evidência:** tabela das 3 execuções (data, status, campanhas gravadas, duplicatas, e-mail de falha) publicada na nota de verificação. **Qualquer falha zera o contador** (dias consecutivos). Definição de falha: qualquer execução com status ≠ ok.

## 14. Rollback e preservação do histórico do Hub

- **Hub intocado em qualquer cenário:** nada é apagado, modificado ou desligado no Hub sem aprovação expressa do Champion (ordem permanente). O rollback da F3-T12 não toca no Hub.
- **Histórico preservado:** `maestro_runs`, `maestro_recommendations`, `daily_metrics`, `campaigns` e demais coleções permanecem intactos no Hub, sem migração. Exportação/backup documental (CSV) é decisão futura do Champion — não faz parte do rollback nem do desligamento.
- **Rollback da F3-T12:** desligar a automação no Maestro (1 clique) + esconder a rota `campanhas` no 51414; coleções novas ficam como histórico (dados preservados, tela fora do ar); rollback da migration remove apenas as 2 coleções novas — `demandas` e o restante do projeto ficam intocados.
- **Meta:** nenhuma escrita em nenhum cenário — nada a reverter.
- **Registro:** todo rollback é documentado no changelog com evidência.

---
*Complemento do plano v2 preparado em 24/10/2026 pelo Maestro (somente planejamento). Nenhuma implementação iniciada. Aguarda autorização específica de execução.*