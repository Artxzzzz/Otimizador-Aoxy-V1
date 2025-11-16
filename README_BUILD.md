# Otimizador Aoxy v1.0

Um aplicativo de otimização de sistemas Windows com interface gráfica moderna desenvolvido com Python e Tkinter.

## 📋 Sumário

- [Instalação](#instalação)
- [Executar como Script](#executar-como-script)
- [Empacotar com PyInstaller](#empacotar-com-pyinstaller)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Recursos](#recursos)

## Instalação

### Requisitos

- **Python 3.8+** (testado com Python 3.13)
- **pip** (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/Otimizador-Aoxy-V1.git
cd "Otimizador Aoxy v1"
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install tktooltip psutil pyinstaller
```

## Executar como Script

### Opção 1: PowerShell (Recomendado)

Abra o PowerShell **como Administrador** e execute:

```powershell
cd "c:\Users\larissa\OneDrive\Documentos\Meus projetos github\Otimizador Aoxy v1"
python meu_app\main\main.py
```

### Opção 2: Prompt de Comando

Abra o CMD **como Administrador** e execute:

```cmd
cd c:\Users\larissa\OneDrive\Documentos\Meus projetos github\Otimizador Aoxy v1
python meu_app\main\main.py
```

## Empacotar com PyInstaller

O projeto inclui scripts de build automatizados que geram um executável (.exe) com todos os recursos inclusos (fontes, imagens, configurações).

### Opção 1: Script Python (Recomendado)

```bash
cd "Otimizador Aoxy v1"
python build.py
```

Este script irá:
1. ✅ Verificar e instalar dependências necessárias
2. ✅ Limpar builds antigos
3. ✅ Gerar o executável com PyInstaller
4. ✅ Mostrar o caminho do arquivo final

### Opção 2: Script Batch (.bat)

```bash
cd "Otimizador Aoxy v1"
build.bat
```

### Opção 3: PyInstaller Direto

```bash
cd "Otimizador Aoxy v1"
python -m PyInstaller --onefile --windowed ^
  --add-data "meu_app/main/img;main/img" ^
  --add-data "meu_app/main/info;main/info" ^
  --add-data "meu_app/main/fonts;main/fonts" ^
  --icon "meu_app/main/img/icon.ico" ^
  --name "Otimizador-Aoxy-v1" ^
  meu_app/main/main.py
```

### Resultado

Após o build, o executável estará em:
```
dist/Otimizador-Aoxy-v1.exe
```

## Executar o Executável

### 1️⃣ Com Direitos de Administrador (Obrigatório)

**Via PowerShell:**
```powershell
Start-Process -Verb RunAs "dist\Otimizador-Aoxy-v1.exe"
```

**Manualmente:**
1. Navegue até `dist/`
2. Clique direito em `Otimizador-Aoxy-v1.exe`
3. Selecione **"Executar como administrador"**
4. Aceite o prompt do UAC

### 2️⃣ Criar um Atalho com Elevação

Para facilitar execuções futuras, crie um atalho que pede elevação automaticamente:

1. Clique direito em `Otimizador-Aoxy-v1.exe` > **Criar atalho**
2. Clique direito no atalho > **Propriedades**
3. Vá para a aba **Avançado** > Marque **"Executar como administrador"**
4. Clique **OK**

## Estrutura do Projeto

```
Otimizador Aoxy v1/
├── meu_app/
│   └── main/
│       ├── main.py                # Arquivo principal (interface Tkinter)
│       ├── funcoes.py             # Funções de otimização
│       ├── img/
│       │   ├── icon.ico           # Ícone da aplicação
│       │   └── fundo1.png         # Imagem de fundo
│       ├── info/
│       │   └── sobre.txt          # Informações do app
│       └── fonts/
│           ├── CaviarDreams.ttf
│           ├── CaviarDreams_Bold.ttf
│           └── Heavitas.ttf
├── build.py                        # Script de build (Python)
├── build.bat                       # Script de build (Batch)
├── build.spec                      # Configuração do PyInstaller
├── requirements.txt                # Dependências do projeto
├── README.md                       # Este arquivo
└── LICENSE                         # Licença do projeto
```

## Recursos

- ⚡ **Desativar Recursos** - Remove componentes desnecessários
- 🗑️ **Desinstalar Aplicativos** - Interface para desinstalar programas
- 🔄 **Atualizar Drivers** - Gerenciador de dispositivos
- 🧹 **Limpar Arquivos** - Remove temporários e cache
- ⚡ **Recursos de Energia** - Ajusta configurações de potência
- 🧹 **Limpar Cache** - Limpa cache do navegador Chrome
- 💽 **Desfragmentar Disco** - Otimiza a unidade C:
- 🎨 **Configurações Visuais** - Ajusta efeitos gráficos
- 🧹 **Limpar Prefetch/Temp** - Remove arquivos de pré-carregamento
- 🔄 **Apps de Inicialização** - Gerencia programas ao iniciar
- 🌡️ **Monitorar Temperatura** - Verifica saúde do hardware
- 💾 **Pontos de Restauração** - Cria/restaura snapshots do sistema

## Requisitos do Sistema

- **Windows 7+** (testado em Windows 10)
- **Python 3.8+** ou **Executável pré-compilado**
- **Privilégios de Administrador** (obrigatório para funcionar)
- **Pelo menos 50MB** de espaço em disco

## Solução de Problemas

### ❌ "Arquivo não encontrado" na aba Sobre

- Verifique se `meu_app/main/info/sobre.txt` existe
- Se empacotado com PyInstaller, certifique-se de que foi incluído no build

### ❌ Ícone não aparece

- Verifique se `meu_app/main/img/icon.ico` existe
- Se faltar, o app ainda funciona, mas sem ícone

### ❌ "Sem permissão" ao executar limpezas

- Execute como Administrador (obrigatório)
- O app pede elevação automaticamente, mas você precisa aceitar o UAC

### ❌ Dependências não encontradas

```bash
pip install --upgrade -r requirements.txt
```

## Desenvolvimento

### Editar o Código

1. Abra `meu_app/main/main.py` com seu editor favorito
2. Edite as funções em `meu_app/main/funcoes.py`
3. Teste executando como script (opção acima)
4. Após confirmado, faça novo build com `python build.py`

### Adicionar Novas Funções

1. Adicione a função em `funcoes.py`
2. Crie um handler em `main.py` que chama `run_and_capture(sua_funcao)`
3. Adicione um botão no menu lateral com o handler

## Licença

Este projeto está licenciado sob a MIT License. Veja `LICENSE` para detalhes.

## Autor

Desenvolvido por **Larissa** (lari-pnj)

---

**Última atualização:** 16 de Novembro de 2025
