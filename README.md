# Telegram Channel Downloader

*Read this in other languages: [English](README-en.md)*

---

*Este programa automatiza o download e a organização de conteúdos armazenados em canais do Telegram. Ele lê o histórico de mensagens, converte textos estruturais em pastas no HD e baixa todos os arquivos, como vídeos e PDFs, diretamente para as pastas corretas, restaurando a estrutura original.*

## 📂 EXTRATOR E ORGANIZADOR DE CANAIS DO TELEGRAM

Este aplicativo com interface gráfica automatiza todo o processo de download e organização de arquivos disponibilizados em canais do Telegram. Ao ser executado, ele varre o histórico de mensagens do canal desejado.

Toda vez que identifica um texto estrutural (como o título de um tópico ou seção), ele cria uma pasta correspondente no seu disco rígido. Em seguida, ele baixa todos os arquivos anexados, incluindo vídeos, PDFs, planilhas e arquivos compactados, salvando-os diretamente nas respectivas pastas. Isso garante a restauração da estrutura original dos conteúdos de forma simples e automatizada.

## ⚙️ PRINCIPAIS FUNCIONALIDADES

* **Interface Gráfica (GUI):** Interface fácil de usar, com suporte nativo a temas (Claro e Escuro) e múltiplos idiomas (Português e Inglês).
* **Encerramento Seguro:** Após iniciado o download dos arquivos, o processo pode ser interrompido de forma segura e imediata a qualquer momento pressionando o botão "PARAR" na interface do aplicativo.
* **Resolução Inteligente de Conflitos:** Se o script detectar que um arquivo com o mesmo nome já existe na sua pasta, ele pausará o download e exibirá o tamanho de ambos os arquivos (o local e o do Telegram). Você poderá então escolher entre ações: baixar uma nova cópia numerada, pular este download, substituir o arquivo antigo local pelo novo, ou ignorar todos os arquivos idênticos daquela sessão.

## 🚀 TUTORIAL DE COMO UTILIZAR O PROGRAMA COMPILADO (.exe)

### Passo 01 - Obter Credenciais do Telegram

* Acesse o site `my.telegram.org` através do seu navegador e faça login utilizando o seu número de celular.
* Clique na opção *API development tools*.
* Preencha os campos `App title` e `Short name` com o nome que desejar. Em *Platform*, deixe como *Desktop*.
* Clique no botão *Create application*.
* Na página seguinte, copie os valores apresentados em `App api_id`, que é uma sequência de números, e `App api_hash`, que é uma sequência misturando letras e números. Guarde esses dados.

### Passo 02 - Configurar o Download

* Abra o aplicativo `TelegramChannelDownloader.exe` (ou execute o script Python através do comando `python main.py`).
* Em **Nome da sessão**, escolha um nome para salvar o seu acesso (isso evita que você precise fazer login novamente no futuro).
* Insira os dados copiados no Passo 1 nos campos de **API ID** e **API Hash**.
* No campo **Canal**, insira o link ou a identificação do canal do Telegram que contém os arquivos (Ex: 't.me/nome_do_canal').
* Escolha a pasta no seu computador ou HD externo onde o conteúdo deve ser salvo clicando no botão **Procurar...**.
* Clique em "Salvar Configurações" no menu de Arquivo para não precisar preencher novamente na próxima vez.

### Passo 03 - Iniciar o Download e Login

* Clique no botão azul **INICIAR DOWNLOAD**.
* Como será a primeira vez que você roda o programa, ele pedirá que você confirme sua identidade. Uma janela aparecerá pedindo que digite seu número de celular com o código do país.
* O Telegram enviará um código numérico de verificação diretamente para o aplicativo no seu celular.
* Digite esse código na janela pop-up do aplicativo.
* Caso possua autenticação de duas etapas (2FA), a senha será solicitada.
* Pronto. A partir desse momento, o aplicativo começará a trabalhar sozinho, criando as pastas e baixando todos os materiais do canal para o seu computador.

## 🛠️ TUTORIAL DE COMO COMPILAR O PROGRAMA A PARTIR DO CÓDIGO-FONTE

Para usuários que desejam baixar o código-fonte, instalar as dependências e gerar o arquivo `.exe` localmente, o projeto utiliza um ambiente virtual Python (`venv`) denominado `env_downloader`.

> **Nota:** O procedimento abaixo pressupõe que o Python esteja instalado e disponível por meio do comando `py` e que os arquivos necessários do projeto, incluindo `build.spec`, estejam presentes na pasta do projeto.

### Passo 01 - Baixe o código-fonte

Clone o repositório ou baixe os arquivos do projeto e abra um terminal na pasta raiz do projeto.

No PowerShell ou no Prompt de Comando (CMD), navegue até a pasta correspondente:

```powershell
cd "C:\Caminho\Para\A\Sua\Pasta"
```

Substitua o caminho pelo local onde o projeto foi salvo.

### Passo 02 - Crie o ambiente virtual

Caso o ambiente virtual ainda não tenha sido criado, utilize o inicializador nativo do Python:

```powershell
py -m venv env_downloader
```

Esse comando criará o ambiente virtual `env_downloader` dentro da pasta do projeto.

### Passo 03 - Ative o ambiente virtual

A ativação depende do terminal utilizado.

#### PowerShell

Execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\env_downloader\Scripts\Activate.ps1
```

#### Prompt de Comando (CMD)

Execute:

```cmd
env_downloader\Scripts\activate.bat
```

Após a ativação, o nome do ambiente virtual (`env_downloader`) deverá aparecer no início da linha de comando.

### Passo 04 - Instale as dependências

Com o ambiente virtual ativado, instale as dependências necessárias para executar e compilar o programa.

Você pode instalá-las diretamente:

```powershell
pip install PySide6 telethon pyinstaller
```

Ou, caso o projeto contenha o arquivo `requirements.txt`, utilize:

```powershell
pip install -r requirements.txt
```

### Passo 05 - Gere o arquivo `.exe`

Com as dependências instaladas e o ambiente virtual ainda ativado, execute o PyInstaller utilizando o arquivo de especificação do projeto:

```powershell
pyinstaller build.spec
```

O PyInstaller utilizará as configurações definidas em `build.spec` para gerar o executável.

Após a conclusão do processo, os arquivos gerados pelo PyInstaller estarão nas pastas de saída especificadas pela configuração de build.

### 👤 AUTORIA E DESENVOLVIMENTO

Aplicação de automação desenvolvida de forma independente por [**Pablo Phillipe Cândido dos Santos**](http://lattes.cnpq.br/9500873674712528), destinada ao download e à organização de arquivos disponibilizados em canais do Telegram, com restauração automatizada da estrutura de origem dos materiais.

O desenvolvimento contou com a utilização de ferramentas de inteligência artificial generativa como recurso auxiliar no processo de desenvolvimento, mantendo-se sob responsabilidade do autor a concepção, implementação, integração e verificação do projeto.
