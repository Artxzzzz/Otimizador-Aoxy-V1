#!/usr/bin/env python3
"""
Script de build automatizado para Otimizador Aoxy v1.0
Empacota o app com PyInstaller incluindo todos os recursos (fonts, images, config)
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Cores para output
class Cor:
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_info(msg):
    print(f"{Cor.AZUL}[*]{Cor.RESET} {msg}")

def print_sucesso(msg):
    print(f"{Cor.VERDE}[OK]{Cor.RESET} {msg}")

def print_erro(msg):
    print(f"{Cor.VERMELHO}[!]{Cor.RESET} {msg}")

def print_aviso(msg):
    print(f"{Cor.AMARELO}[⚠]{Cor.RESET} {msg}")

def main():
    print(f"{Cor.BOLD}{Cor.AZUL}")
    print("=" * 50)
    print("  Otimizador Aoxy v1.0 - Build Script")
    print("=" * 50)
    print(f"{Cor.RESET}\n")
    
    # Obter diretório do script
    script_dir = Path(__file__).parent.absolute()
    
    # Verificar se estamos no diretório correto
    if not (script_dir / 'build.spec').exists():
        print_erro("arquivo 'build.spec' não encontrado!")
        print_erro(f"Execute este script a partir de: {script_dir}")
        sys.exit(1)
    
    print_info("Verificando dependências...")
    
    # Lista de pacotes necessários
    packages = {
        'pyinstaller': 'PyInstaller',
        'tktooltip': 'tktooltip',
        'psutil': 'psutil',
    }
    
    for package, display_name in packages.items():
        try:
            __import__(package.replace('-', '_'))
            print_sucesso(f"{display_name} já instalado")
        except ImportError:
            print_aviso(f"{display_name} não encontrado, instalando...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print_sucesso(f"{display_name} instalado")
    
    print()
    print_info("Limpando builds antigos...")
    
    # Remover diretórios antigos
    dirs_to_remove = ['build', 'dist', '__pycache__', '.pytest_cache']
    for dir_name in dirs_to_remove:
        dir_path = script_dir / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print_sucesso(f"Removido: {dir_name}/")
    
    print()
    print_info("Executando PyInstaller...")
    print()
    
    # Executar PyInstaller
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'PyInstaller', '--clean', 'build.spec'],
            cwd=script_dir,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print_erro(f"Falha ao executar PyInstaller: {e}")
        sys.exit(1)
    
    print()
    
    # Verificar se o build foi bem-sucedido
    exe_path = script_dir / 'dist' / 'Otimizador-Aoxy-v1' / 'Otimizador-Aoxy-v1.exe'
    
    if exe_path.exists():
        print(f"{Cor.BOLD}{Cor.VERDE}")
        print("=" * 50)
        print("  BUILD CONCLUÍDO COM SUCESSO!")
        print("=" * 50)
        print(f"{Cor.RESET}")
        print()
        print_sucesso("Executável criado em:")
        print(f"   {exe_path}")
        print()
        print_info("Para executar o app:")
        print(f"   1. Navegue até: {script_dir / 'dist' / 'Otimizador-Aoxy-v1'}")
        print(f"   2. Clique com botão direito em 'Otimizador-Aoxy-v1.exe'")
        print(f"   3. Selecione 'Executar como administrador'")
        print()
        print_info("Ou via PowerShell (como admin):")
        print(f"   Start-Process -Verb RunAs '{exe_path}'")
        print()
    else:
        print_erro("Falha ao criar executável!")
        print_erro(f"Esperado: {exe_path}")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print_aviso("Build cancelado pelo usuário")
        sys.exit(130)
    except Exception as e:
        print_erro(f"Erro inesperado: {e}")
        sys.exit(1)
