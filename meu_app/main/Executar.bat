@echo off
REM Executa o script Python na mesma pasta do arquivo .bat
py "%~dp0app.py" %*
pause