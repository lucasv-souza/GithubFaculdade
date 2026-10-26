# Laboratório Docker — Integração DevOps (Unidade 3)

API ASP.NET Core (.NET 10) empacotada em Docker, com versionamento de imagens,
ambientes staging/production, health check, rollback e Docker Compose.

> No Linux/macOS use `curl`; no Windows use `curl.exe`.

## Execução local (sem Docker)
dotnet run

## Construção
docker build -t devops-webapi:1.0.0 .
docker images

## Execução (primeiro container)
docker run -d --name devops-api -p 8080:8080 devops-webapi:1.0.0
docker ps
docker logs devops-api
docker stop devops-api
docker rm devops-api

## Staging
docker run -d --name devops-api-staging -p 8081:8080 -e APP_ENVIRONMENT=staging -e APP_VERSION=1.0.0 devops-webapi:1.0.0

## Production
docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.0.0 devops-webapi:1.0.0

## Health Check
curl.exe -f http://localhost:8081/health
curl.exe -f http://localhost:8082/health

## Nova versão (1.1.0)
docker build -t devops-webapi:1.1.0 .
docker rm -f devops-api-staging
docker run -d --name devops-api-staging -p 8081:8080 -e APP_ENVIRONMENT=staging -e APP_VERSION=1.1.0 devops-webapi:1.1.0
# após validar em staging:
docker rm -f devops-api-prod
docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.1.0 devops-webapi:1.1.0

## Falha controlada (1.2.0)
O endpoint /health foi alterado para retornar HTTP 500 (propositalmente).
docker build -t devops-webapi:1.2.0 .
docker rm -f devops-api-staging
docker run -d --name devops-api-staging -p 8081:8080 -e APP_ENVIRONMENT=staging -e APP_VERSION=1.2.0 devops-webapi:1.2.0
curl.exe -f http://localhost:8081/health   # falha -> NÃO promover

## Rollback
docker rm -f devops-api-prod
docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.1.0 devops-webapi:1.1.0
curl.exe -f http://localhost:8082/health

## Docker Compose
docker compose up -d
docker compose ps
docker compose logs
docker compose config
docker compose down

## Healthcheck no Compose
A imagem `aspnet` não inclui `curl`. O `compose.yaml` usa `bash` + `/dev/tcp`
para fazer `GET /health` e exigir HTTP 200. Alternativa: instalar curl no
Dockerfile (`apt-get install -y curl`), ao custo de uma imagem maior.

## Limpeza
docker compose down
docker rmi devops-webapi:1.0.0 devops-webapi:1.1.0 devops-webapi:1.2.0
