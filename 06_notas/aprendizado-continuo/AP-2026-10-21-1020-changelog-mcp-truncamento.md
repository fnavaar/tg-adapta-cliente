# AP-2026-10-21-1020 — Publicação de arquivo grande via mcp_github_create_or_update_file

**Data:** 2026-10-21T10:20-03:00 · **Contexto:** registro documental E1 (segregação sintético×produção, ETHOS 51414) · **Tipo:** padrão verificado

## O que aconteceu

Ao publicar o changelog.md (~36 KB) via conector MCP GitHub (`mcp_github_create_or_update_file`), a primeira publicação gravou apenas 3.801 bytes — o conteúdo enviado foi truncado ANTES de chegar ao GitHub (o payload que o servidor MCP enviou continha só cabeçalho + entrada nova, sem o histórico). A segunda tentativa, com conteúdo reconstruído "de cabeça", introduziu corrupção em entradas históricas (caracteres estranhos, palavras alteradas). Detectado porque o campo `size` da resposta NÃO bateu com o arquivo local (35.986 esperado).

## Padrão verificado

1. **O campo `size` da resposta do create_or_update_file é o detector primário.** Se `size` ≠ bytes do arquivo local, a publicação está truncada — parar e republicar, não seguir.
2. **Nunca reconstruir conteúdo "de cabeça".** Para arquivo grande, ler o arquivo local por completo (read_file) e copiar verbatim; a reconstrução de memória introduziu corrupção silenciosa em entradas históricas.
3. **Verificação em 3 pontos:** (a) `cmp` local base vs. remoto (get_file_contents) antes de publicar; (b) `size` da resposta vs. local; (c) `cmp` do remoto pós-publicação vs. local. Os três juntos pegaram os dois erros.
4. **O clone local é a fonte da verdade durante a publicação.** O commit local íntegro existia; o dano foi só no remoto e foi recuperável em 1 commit de correção.
5. **Limitação registrada:** para arquivos >30 KB, o conector MCP GitHub pode truncar o `content` no transporte (mesma família do gotcha skip_file_write ~30 KB). Alternativa segura: dividir a publicação em commits menores (anexar entrada por entrada) ou usar push_files com verificação.

## Evidência

- Commits: 0670430 (truncado, 3.801 B), f404651 (corrompido, 5.999 B), 2409160 (íntegro, 35.986 B = local byte a byte).
- Verificação final: `git show origin/main:changelog.md | cmp - changelog.md` → idêntico.
