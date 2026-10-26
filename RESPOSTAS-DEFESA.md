# Respostas para a defesa da atividade

1. **Imagem × container:** a imagem é um modelo imutável (filesystem, runtime, app, metadados); o container é uma instância em execução criada a partir dela. Uma imagem gera vários containers.
2. **Função do Dockerfile:** receita declarativa que descreve como construir a imagem (base, restore, publish, runtime, porta, ENTRYPOINT).
3. **`8081:8080`:** porta-host:porta-container. O que chega em `localhost:8081` é encaminhado para a porta 8080 dentro do container.
4. **Variáveis de ambiente:** separam configuração de código. A mesma imagem roda em staging e production mudando só `APP_ENVIRONMENT`/`APP_VERSION`, sem rebuild. (Segredos reais exigem gerenciador de secrets.)
5. **Multi-stage build:** o SDK, compiladores e código-fonte ficam só no stage `build`; a imagem final leva apenas o runtime ASP.NET e os arquivos publicados — menor, mais limpa e com menos superfície de ataque.
6. **Tags 1.0.0 / 1.1.0:** identificação, rastreabilidade, reprodutibilidade e possibilidade de rollback; evita depender de `latest`, que é ambígua.
7. **Staging primeiro:** valida a release (inicia? endpoints respondem? health OK?) antes de expô-la como produção — é o quality gate.
8. **Detecção da falha:** `/health` da 1.2.0 retorna HTTP 500; `curl -f` trata status ≥ 400 como erro (exit code ≠ 0), sinalizando FAIL e bloqueando a promoção.
9. **Rollback:** `docker rm -f devops-api-prod` e novo `docker run` com a imagem `devops-webapi:1.1.0`, que continuava disponível no host; depois, `curl -f` em `/health` confirmou a recuperação.
10. **GitHub Actions:** a cada push, um workflow faz build, testes e `docker build` com tag de versão, sobe/faz deploy em staging, roda o health check como gate (falhou → job falha e a promoção para production não ocorre) e só então promove a mesma imagem para production, mantendo as tags anteriores para rollback.

## Pergunta de fixação
**Interromper a promoção e investigar a causa.** O health check da 1.2.0 em staging retornou HTTP 500; promover uma versão reprovada ou gerar outra imagem sem investigar repete o problema. A 1.1.0 continua sendo a versão estável em production.
