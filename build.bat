@echo off
REM Script de build automatizado para Otimizador Aoxy v1.0 usando PyInstaller
REM Este script limpa builds antigos e cria um novo executável com todos os recursos

echo ========================================
echo Otimizador Aoxy v1.0 - Build Script
echo ========================================
echo.

REM Verifica se PyInstaller está instalado
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [!] PyInstaller não encontrado. Instalando...
    python -m pip install pyinstaller
) else (
    echo [OK] PyInstaller já instalado
)

REM Verifica se tktooltip está instalado
python -m pip show tktooltip >nul 2>&1
if errorlevel 1 (
    echo [!] tktooltip não encontrado. Instalando...
    python -m pip install tktooltip
) else (
    echo [OK] tktooltip já instalado
)

REM Verifica se psutil está instalado
python -m pip show psutil >nul 2>&1
if errorlevel 1 (
    echo [!] psutil não encontrado. Instalando...
    python -m pip install psutil
) else (
    echo [OK] psutil já instalado
)

echo.
echo [*] Limpando builds antigos...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "__pycache__" rmdir /s /q __pycache__
echo [OK] Pasta de build limpa

echo.
echo [*] Executando PyInstaller com spec...
pyinstaller --clean build.spec

echo.
if exist "dist\Otimizador-Aoxy-v1\Otimizador-Aoxy-v1.exe" (
    echo ========================================
    echo [SUCESSO] Build concluído!
    echo ========================================
    echo.
    echo Executável criado em:
    echo   dist\Otimizador-Aoxy-v1\Otimizador-Aoxy-v1.exe
    echo.
    echo Para executar:
    echo   1. Abra o Gerenciador de Tarefas (Ctrl+Shift+Esc)
    echo   2. Clique em "Arquivo" > "Executar nova tarefa"
    echo   3. Digite "Executar com privilégios de administrador"
    echo   4. Cole o caminho acima e execute
    echo.
    echo Ou simplesmente:
    echo   start dist\Otimizador-Aoxy-v1\Otimizador-Aoxy-v1.exe
    echo.
) else (
    echo [ERRO] Build falhou. Verifique os erros acima.
    pause
    exit /b 1
)

pause
