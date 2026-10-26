# Executa TODO o laboratório e salva a saída em evidencias\*.txt (PowerShell, Windows).
# Pré-requisito: Docker Desktop aberto. Rode na pasta do projeto:  .\lab.ps1
$ErrorActionPreference = "Continue"
New-Item -ItemType Directory -Force evidencias | Out-Null
function Log($arq, $cmd) {
  "`n> $cmd" | Tee-Object -FilePath "evidencias\$arq" -Append
  Invoke-Expression $cmd 2>&1 | Tee-Object -FilePath "evidencias\$arq" -Append
}
function Limpa { docker rm -f devops-api devops-api-staging devops-api-prod 2>$null | Out-Null }
Limpa; docker compose down 2>$null | Out-Null
Remove-Item evidencias\*.txt -ErrorAction SilentlyContinue

# --- 1.0.0 ---
Copy-Item versions\Program.1.0.0.cs Program.cs -Force
Log "01-imagens.txt" "docker build -t devops-webapi:1.0.0 ."
Log "01-imagens.txt" "docker images devops-webapi"

Log "02-staging-prod-1.0.0.txt" "docker run -d --name devops-api-staging -p 8081:8080 -e APP_ENVIRONMENT=staging -e APP_VERSION=1.0.0 devops-webapi:1.0.0"
Log "02-staging-prod-1.0.0.txt" "docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.0.0 devops-webapi:1.0.0"
Start-Sleep 4
Log "02-staging-prod-1.0.0.txt" "docker ps"
Log "02-staging-prod-1.0.0.txt" "curl.exe -s http://localhost:8081/"
Log "02-staging-prod-1.0.0.txt" "curl.exe -s http://localhost:8082/"

# --- 1.1.0 ---
Copy-Item versions\Program.1.1.0.cs Program.cs -Force
Log "01-imagens.txt" "docker build -t devops-webapi:1.1.0 ."
Log "01-imagens.txt" "docker images devops-webapi"

Log "03-staging-1.1.0.txt" "docker rm -f devops-api-staging"
Log "03-staging-1.1.0.txt" "docker run -d --name devops-api-staging -p 8081:8080 -e APP_ENVIRONMENT=staging -e APP_VERSION=1.1.0 devops-webapi:1.1.0"
Start-Sleep 4
Log "03-staging-1.1.0.txt" "curl.exe -f -s http://localhost:8081/health"
Log "03-staging-1.1.0.txt" "curl.exe -f -s http://localhost:8081/version"

Log "04-production-1.1.0.txt" "docker rm -f devops-api-prod"
Log "04-production-1.1.0.txt" "docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.1.0 devops-webapi:1.1.0"
Start-Sleep 4
Log "04-production-1.1.0.txt" "docker ps"
Log "04-production-1.1.0.txt" "curl.exe -f -s http://localhost:8082/health"

# --- 1.2.0 (falha proposital) ---
Copy-Item versions\Program.1.2.0.cs Program.cs -Force
Log "05-falha-1.2.0.txt" "docker build -t devops-webapi:1.2.0 ."
Log "05-falha-1.2.0.txt" "docker rm -f devops-api-staging"
Log "05-falha-1.2.0.txt" "docker run -d --name devops-api-staging -p 8081:8080 -e APP_ENVIRONMENT=staging -e APP_VERSION=1.2.0 devops-webapi:1.2.0"
Start-Sleep 4
Log "05-falha-1.2.0.txt" "curl.exe -f -s http://localhost:8081/health"
Log "05-falha-1.2.0.txt" "'exit code do curl: ' + `$LASTEXITCODE"
# simulação de incidente em produção
Log "05-falha-1.2.0.txt" "docker rm -f devops-api-prod"
Log "05-falha-1.2.0.txt" "docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.2.0 devops-webapi:1.2.0"
Start-Sleep 4
Log "05-falha-1.2.0.txt" "curl.exe -f -s http://localhost:8082/health"

# --- Rollback ---
Log "06-rollback.txt" "docker rm -f devops-api-prod"
Log "06-rollback.txt" "docker run -d --name devops-api-prod -p 8082:8080 -e APP_ENVIRONMENT=production -e APP_VERSION=1.1.0 devops-webapi:1.1.0"
Start-Sleep 4
Log "06-rollback.txt" "curl.exe -f -s http://localhost:8082/health"
Log "06-rollback.txt" "docker ps"

# --- Compose ---
Copy-Item versions\Program.1.1.0.cs Program.cs -Force   # estado final = 1.1.0
Limpa
Log "07-compose.txt" "docker compose config"
Log "07-compose.txt" "docker compose up -d"
Start-Sleep 20
Log "07-compose.txt" "docker compose ps"
Log "07-compose.txt" "curl.exe -f -s http://localhost:8081/health"
Log "07-compose.txt" "curl.exe -f -s http://localhost:8082/health"
Log "07-compose.txt" "docker compose down"
Write-Host "`nPronto. Logs em .\evidencias. Tire também os prints (docker images / docker ps / navegador)."
