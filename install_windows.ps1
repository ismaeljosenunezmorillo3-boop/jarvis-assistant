# JARVIS Assistant - Instalación automática para Windows
$ErrorActionPreference = "Stop"

Write-Host "🤖 Instalador de JARVIS Assistant" -ForegroundColor Cyan
Write-Host "================================="

# Comprobar Python
try {
    $pythonVersion = & py --version 2>&1
    Write-Host "Python detectado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "No se encontró Python." -ForegroundColor Red
    Write-Host "Instálalo desde https://www.python.org/downloads/ y marca 'Add Python to PATH'."
    exit 1
}

# Crear entorno virtual
if (-not (Test-Path "venv")) {
    Write-Host "Creando entorno virtual..."
    & py -m venv venv
}

$python = Join-Path $PSScriptRoot "venv\Scripts\python.exe"

Write-Host "Actualizando pip..."
& $python -m pip install --upgrade pip

Write-Host "Instalando dependencias..."
& $python -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")

Write-Host ""
Write-Host "✅ Instalación terminada correctamente." -ForegroundColor Green
Write-Host "Para iniciar JARVIS, ejecuta:"
Write-Host "  .\venv\Scripts\python.exe .\jarvis.py" -ForegroundColor Yellow
