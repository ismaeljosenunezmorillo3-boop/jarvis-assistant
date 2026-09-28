# Instalación automática de JARVIS

## Windows

1. Instala Python 3.8 o superior desde [python.org](https://www.python.org/downloads/). Durante la instalación, marca **Add Python to PATH**.
2. Descarga o clona este repositorio.
3. Abre PowerShell dentro de la carpeta del proyecto y ejecuta:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install_windows.ps1
.\venv\Scripts\python.exe .\jarvis.py
```

Si descargaste el proyecto como ZIP, haz clic derecho en el archivo, selecciona **Extraer todo** y abre PowerShell dentro de la carpeta extraída.

## Linux y macOS

Necesitas Python 3 y un micrófono. Desde la carpeta del proyecto ejecuta:

```bash
chmod +x install_linux_mac.sh
./install_linux_mac.sh
./venv/bin/python jarvis.py
```

En Ubuntu/Debian, si la instalación de audio falla, instala primero:

```bash
sudo apt update
sudo apt install python3-venv portaudio19-dev python3-pyaudio
```

Los scripts crean una carpeta `venv` aislada e instalan las dependencias sin modificar el resto del sistema.
