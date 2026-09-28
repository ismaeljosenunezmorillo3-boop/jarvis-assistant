#!/usr/bin/env bash
set -e

echo "🤖 Instalador de JARVIS Assistant"
echo "================================="

if ! command -v python3 >/dev/null 2>&1; then
  echo "No se encontró Python 3. Instálalo usando el administrador de paquetes de tu sistema."
  exit 1
fi

echo "Python detectado: $(python3 --version)"

if [ ! -d "venv" ]; then
  echo "Creando entorno virtual..."
  python3 -m venv venv
fi

echo "Actualizando pip..."
./venv/bin/python -m pip install --upgrade pip

echo "Instalando dependencias..."
./venv/bin/python -m pip install -r requirements.txt

echo ""
echo "✅ Instalación terminada correctamente."
echo "Para iniciar JARVIS, ejecuta:"
echo "  ./venv/bin/python jarvis.py"
