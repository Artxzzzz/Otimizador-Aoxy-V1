@echo off
REM Executa o script Python na mesma pasta do arquivo .bat
python "%~dp0app.python" %*
pause