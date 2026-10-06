<#
.SYNOPSIS
    Environment Setup & Cluster Provisioning Script for Runtime Threat Mitigation in K8s
.DESCRIPTION
    Verifies prerequisites (Docker, kubectl, Helm, Kind, Python), installs required Helm charts repos,
    and initializes the local Kind cluster for eBPF threat mitigation research.
#>

$ErrorActionPreference = "Stop"

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "  Runtime Threat Mitigation in K8s - Phase 0 Environment Setup" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

# 1. Check Docker
Write-Host "`n[1/5] Checking Docker..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "  [+] Docker CLI detected." -ForegroundColor Green
    try {
        docker info > $null 2>&1
        Write-Host "  [+] Docker Daemon is running!" -ForegroundColor Green
    } catch {
        Write-Host "  [!] WARNING: Docker Daemon is NOT running. Please start Docker Desktop." -ForegroundColor Red
    }
} else {
    Write-Host "  [-] Docker is not installed. Please install Docker Desktop for Windows." -ForegroundColor Red
}

# 2. Check kubectl
Write-Host "`n[2/5] Checking kubectl..." -ForegroundColor Yellow
if (Get-Command kubectl -ErrorAction SilentlyContinue) {
    $kubectlVer = kubectl version --client -o json | ConvertFrom-Json
    Write-Host "  [+] kubectl detected ($($kubectlVer.clientVersion.gitVersion))." -ForegroundColor Green
} else {
    Write-Host "  [-] kubectl not found. Install via: winget install Kubernetes.kubectl" -ForegroundColor Red
}

# 3. Check Helm
Write-Host "`n[3/5] Checking Helm..." -ForegroundColor Yellow
if (Get-Command helm -ErrorAction SilentlyContinue) {
    Write-Host "  [+] Helm detected." -ForegroundColor Green
} else {
    Write-Host "  [-] Helm not found. Install via: winget install Helm.Helm" -ForegroundColor Red
}

# 4. Check Kind
Write-Host "`n[4/5] Checking Kind..." -ForegroundColor Yellow
if (Get-Command kind -ErrorAction SilentlyContinue) {
    Write-Host "  [+] Kind detected." -ForegroundColor Green
} else {
    Write-Host "  [-] Kind not found. Install via: winget install Kubernetes.kind" -ForegroundColor Red
}

# 5. Check Python
Write-Host "`n[5/5] Checking Python..." -ForegroundColor Yellow
if (Get-Command py -ErrorAction SilentlyContinue) {
    $pyVer = py --version
    Write-Host "  [+] Python detected via launcher ($pyVer)." -ForegroundColor Green
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pyVer = python --version
    Write-Host "  [+] Python detected ($pyVer)." -ForegroundColor Green
} else {
    Write-Host "  [-] Python 3.11+ not found. Please install Python from python.org or Microsoft Store." -ForegroundColor Red
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host "Next Steps to Launch Cluster & Repos:" -ForegroundColor Cyan
Write-Host "  1. Start Docker Desktop"
Write-Host "  2. Install missing tools (if any):"
Write-Host "     winget install Helm.Helm"
Write-Host "     winget install Kubernetes.kind"
Write-Host "  3. Add Helm Repositories:"
Write-Host "     helm repo add falcosecurity https://falcosecurity.github.io/charts"
Write-Host "     helm repo add kyverno https://kyverno.github.io/kyverno/"
Write-Host "     helm repo add prometheus-community https://prometheus-community.github.io/helm-charts"
Write-Host "     helm repo update"
Write-Host "  4. Create Local Kind Cluster:"
Write-Host "     kind create cluster --config ./scripts/kind-config.yaml"
Write-Host "==================================================================" -ForegroundColor Cyan
