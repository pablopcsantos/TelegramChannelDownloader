# Telegram Channel Downloader

*Read this in other languages: [English](README-en.md)*

---

*Este programa automatiza o download e a organização de conteúdos armazenados em canais do Telegram. Ele lê o histórico de mensagens, converte textos estruturais em pastas no HD e baixa todos os arquivos, como vídeos e PDFs, diretamente para as pastas corretas, restaurando a estrutura original.*

## Extrator e Organizador de Canais do Telegram

Este aplicativo com interface gráfica automatiza todo o processo de download e organização de arquivos disponibilizados em canais do Telegram. Ao ser executado, ele varre o histórico de mensagens do canal desejado.

Toda vez que identifica um texto estrutural (como o título de um tópico ou seção), ele cria uma pasta correspondente no seu disco rígido. Em seguida, ele baixa todos os arquivos anexados, incluindo vídeos, PDFs, planilhas e arquivos compactados, salvando-os diretamente nas respectivas pastas. Isso garante a restauração da estrutura original dos conteúdos de forma simples e automatizada.

## Principais Funcionalidades

* **Interface Gráfica (GUI):** Interface fácil de usar, com suporte nativo a temas (Claro e Escuro) e múltiplos idiomas (Português e Inglês).
* **Encerramento Seguro:** Após iniciado o download dos arquivos, o processo pode ser interrompido de forma segura e imediata a qualquer momento pressionando o botão "PARAR" na interface do aplicativo.
* **Resolução Inteligente de Conflitos:** Se o script detectar que um arquivo com o mesmo nome já existe na sua pasta, ele pausará o download e exibirá o tamanho de ambos os arquivos (o local e o do Telegram). Você poderá então escolher entre ações: baixar uma nova cópia numerada, pular este download, substituir o arquivo antigo local pelo novo, ou ignorar todos os arquivos idênticos daquela sessão.

## Tutorial de Como Utilizar

### Passo 1: Obter Credenciais do Telegram

* Acesse o site `my.telegram.org` através do seu navegador e faça login utilizando o seu número de celular.
* Clique na opção *API development tools*.
* Preencha os campos `App title` e `Short name` com o nome que desejar. Em *Platform*, deixe como *Desktop*.
* Clique no botão *Create application*.
* Na página seguinte, copie os valores apresentados em `App api_id`, que é uma sequência de números, e `App api_hash`, que é uma sequência misturando letras e números. Guarde esses dados.

### Passo 2: Configurar o Download

* Abra o aplicativo `TelegramChannelDownloader.exe` (ou execute o script Python através do comando `python main.py`).
* Em **Nome da sessão**, escolha um nome para salvar o seu acesso (isso evita que você precise fazer login novamente no futuro).
* Insira os dados copiados no Passo 1 nos campos de **API ID** e **API Hash**.
* No campo **Canal**, insira o link ou a identificação do canal do Telegram que contém os arquivos (Ex: 't.me/nome_do_canal').
* Escolha a pasta no seu computador ou HD externo onde o conteúdo deve ser salvo clicando no botão **Procurar...**.
* Clique em "Salvar Configurações" no menu de Arquivo para não precisar preencher novamente na próxima vez.

### Passo 3: Iniciar o Download e Login

* Clique no botão azul **INICIAR DOWNLOAD**.
* Como será a primeira vez que você roda o programa, ele pedirá que você confirme sua identidade. Uma janela aparecerá pedindo que digite seu número de celular com o código do país.
* O Telegram enviará um código numérico de verificação diretamente para o aplicativo no seu celular.
* Digite esse código na janela pop-up do aplicativo.
* Caso possua autenticação de duas etapas (2FA), a senha será solicitada.
* Pronto. A partir desse momento, o aplicativo começará a trabalhar sozinho, criando as pastas e baixando todos os materiais do canal para o seu computador.

### Autoria e Desenvolvimento

Aplicação de automação desenvolvida de forma independente por [**Pablo Phillipe Cândido dos Santos**](http://lattes.cnpq.br/9500873674712528), destinada ao download e à organização de arquivos disponibilizados em canais do Telegram, com restauração automatizada da estrutura de origem dos materiais.

O desenvolvimento contou com a utilização de ferramentas de inteligência artificial generativa como recurso auxiliar no processo de desenvolvimento, mantendo-se sob responsabilidade do autor a concepção, implementação, integração e verificação do projeto.
