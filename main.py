import os
import re
import json
import queue
import asyncio
import threading
import sys
from pathlib import Path

from PySide6.QtCore import QObject, Signal, Slot, Property, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle
from PySide6.QtWidgets import QApplication, QFileDialog

from telethon import TelegramClient
from telethon.errors import FileReferenceExpiredError

"""
TelegramChannelDownloader

Programa desenvolvido de forma independente por Pablo Phillipe Cândido dos Santos, destinado à automação do download de arquivos disponibilizados em canais do Telegram e à sua organização conforme a estrutura de origem.

Program independently developed by Pablo Phillipe Cândido dos Santos to automate the download of files made available in Telegram channels and organize them according to their original structure.

O desenvolvimento contou com ferramentas de inteligência artificial generativa como recurso auxiliar.
The development process involved the use of generative artificial intelligence tools as an auxiliary resource.

Currículo Lattes / Lattes Curriculum: [http://lattes.cnpq.br/9500873674712528](http://lattes.cnpq.br/9500873674712528)
"""

# ==========================================
# CONFIGURAÇÃO DE CAMINHOS PARA PYINSTALLER (.exe)
# ==========================================
if getattr(sys, 'frozen', False):
    # Se estiver rodando como executável compilado
    BASE_DIR = sys._MEIPASS # Pasta temporária onde o .exe extrai os arquivos (qml, ícone)
    EXEC_DIR = os.path.dirname(sys.executable) # Pasta real onde o .exe está localizado
else:
    # Se estiver rodando diretamente via Python no terminal
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    EXEC_DIR = BASE_DIR

# Salva o arquivo de configuração na mesma pasta do .exe (e não na pasta temporária)
CONFIG_PATH = os.path.join(EXEC_DIR, 'config_downloader.json')

# ==========================================
# TRADUÇÕES E TEXTOS
# ==========================================
TRANSLATIONS = {
    'pt': {
        'title': 'Telegram Channel Downloader',
        'menu_file': 'Arquivo', 'menu_save': 'Salvar Configurações', 'menu_exit': 'Sair',
        'menu_view': 'Visual', 'menu_theme_light': 'Modo Claro', 'menu_theme_dark': 'Modo Escuro',
        'menu_lang': 'Idioma',
        'menu_help': 'Ajuda', 'menu_tutorial': 'Tutorial Passo a Passo', 'menu_about': 'Sobre',
        'settings': 'Configurações',
        'api_id': 'API ID:',
        'api_hash': 'API Hash:',
        'channel': 'Canal (link ou @usuário):',
        'dest_folder': 'Pasta de destino:',
        'browse': 'Procurar...',
        'session_name': 'Nome da sessão:',
        'btn_start': 'INICIAR DOWNLOAD',
        'btn_stop': 'PARAR',
        'status_ready': 'Pronto para iniciar.',
        'curr_folder': 'Pasta atual: -',
        'log_title': 'Registro do Processo',
        'req_fields': 'Preencha API ID, API Hash, Canal e Pasta.',
        'invalid_api': 'O API ID deve ser um número.',
        'starting': 'Iniciando...',
        'canceling': 'Cancelando... aguardando arquivo atual.',
        'done': 'Concluído!',
        'error': 'Erro:',
        'canceled': 'Processo cancelado.',
        'about_title': 'Sobre',
        'about_desc': 'TelegramChannelDownloader\n\nPrograma para automatizar o download de arquivos\nde canais do Telegram e organizá-los conforme a estrutura\nde módulos do canal.\n\nDesenvolvido por Pablo Phillipe Cândido dos Santos.\n\nO desenvolvimento contou com ferramentas\nde IA generativa como recurso auxiliar.',
        'about_lattes': 'Acessar Currículo Lattes',
        'login_title': 'Login no Telegram',
        'phone_msg': 'Digite seu telefone (com código do país, ex: +5511...):',
        'code_msg': 'Digite o código de verificação do Telegram:',
        'pass_msg': 'Digite sua senha de duas etapas (deixe em branco se não usar):',
        'btn_confirm': 'Confirmar',
        'btn_cancel': 'Cancelar',
        'conflict_title': 'Conflito de Arquivo',
        'conflict_msg': "O arquivo '{0}' já existe na pasta.\n\nLocal: {1:.2f} MB\nTelegram: {2:.2f} MB",
        'btn_new_name': 'Baixar com novo nome',
        'btn_ignore': 'Ignorar este arquivo',
        'btn_replace': 'Substituir arquivo local',
        'btn_ignore_all': 'Ignorar idênticos nesta sessão'
    },
    'en': {
        'title': 'Telegram Channel Downloader',
        'menu_file': 'File', 'menu_save': 'Save Settings', 'menu_exit': 'Exit',
        'menu_view': 'View', 'menu_theme_light': 'Light Mode', 'menu_theme_dark': 'Dark Mode',
        'menu_lang': 'Language',
        'menu_help': 'Help', 'menu_tutorial': 'Step-by-Step Tutorial', 'menu_about': 'About',
        'settings': 'Settings',
        'api_id': 'API ID:',
        'api_hash': 'API Hash:',
        'channel': 'Channel (link or @user):',
        'dest_folder': 'Destination folder:',
        'browse': 'Browse...',
        'session_name': 'Session name:',
        'btn_start': 'START DOWNLOAD',
        'btn_stop': 'STOP',
        'status_ready': 'Ready to start.',
        'curr_folder': 'Current folder: -',
        'log_title': 'Process Log',
        'req_fields': 'Fill in API ID, Hash, Channel and Folder.',
        'invalid_api': 'API ID must be a number.',
        'starting': 'Starting...',
        'canceling': 'Canceling... waiting for current file.',
        'done': 'Done!',
        'error': 'Error:',
        'canceled': 'Process canceled.',
        'about_title': 'About',
        'about_desc': 'TelegramChannelDownloader\n\nProgram to automate downloading files from\nTelegram channels and organizing them according to\nthe channel\'s module structure.\n\nDeveloped by Pablo Phillipe Cândido dos Santos.\n\nDevelopment was assisted by generative AI tools.',
        'about_lattes': 'Access Lattes Curriculum',
        'login_title': 'Telegram Login',
        'phone_msg': 'Enter phone number (with country code, e.g. +1...):',
        'code_msg': 'Enter the verification code:',
        'pass_msg': 'Enter two-step password (leave blank if none):',
        'btn_confirm': 'Confirm',
        'btn_cancel': 'Cancel',
        'conflict_title': 'File Conflict',
        'conflict_msg': "File '{0}' already exists.\n\nLocal: {1:.2f} MB\nTelegram: {2:.2f} MB",
        'btn_new_name': 'Download with new name',
        'btn_ignore': 'Skip this file',
        'btn_replace': 'Replace local file',
        'btn_ignore_all': 'Skip identical (this session)'
    }
}

TUTORIAL_TEXTS = {
    'pt': """
<p><strong>PASSO A PASSO: COMO BAIXAR ARQUIVOS DO TELEGRAM</strong></p>
<p>Este programa permite baixar automaticamente todos os arquivos de um canal do Telegram, organizando-os em pastas. Para começar, siga os passos abaixo:</p>
<p><strong>PASSO 1: OBTER SUAS CREDENCIAIS (API ID e API Hash)</strong><br>
Para o programa se comunicar com o Telegram em seu nome, ele precisa de uma autorização oficial. Você só precisa fazer isso uma vez.</p>
<ol>
    <li>Acesse o site oficial de desenvolvedores do Telegram: <a target="_blank" href="https://my.telegram.org">https://my.telegram.org</a></li>
    <li>Faça login colocando o seu número de telefone (com o código do país, ex: +5511999999999).</li>
    <li>O Telegram enviará um código de confirmação no seu aplicativo (não por SMS). Digite esse código no site.</li>
    <li>Clique na opção "API development tools".</li>
    <li>Preencha o formulário que aparecer (você pode colocar qualquer nome em "App title" e "Short name").</li>
    <li>Após criar, a página mostrará o seu "App api_id" (um número) e o "App api_hash" (um código longo misturando letras e números).</li>
    <li>Copie esses dois valores e cole-os aqui no programa nos campos "API ID" e "API Hash".</li>
</ol>
<p><strong>PASSO 2: CONFIGURAR O DOWNLOAD NO PROGRAMA</strong></p>
<ol>
    <li>Canal (link ou @usuário): Informe de onde você quer baixar. Você pode colar o link completo (ex: t.me/nome_do_canal) ou apenas o arroba (ex: @nome_do_canal).</li>
    <li>Pasta de destino: Clique em "Procurar..." e escolha em qual pasta do seu computador os arquivos deverão ser salvos.</li>
    <li>Nome da sessão: Deixe o padrão ou mude para um nome de sua escolha. Isso cria um arquivo que lembra o seu login para que você não precise digitar seu número de telefone de novo.</li>
</ol>
<p><strong>PASSO 3: INICIAR O PROCESSO</strong></p>
<ol>
    <li>Sugerimos clicar primeiro em "Salvar Configurações" no menu Arquivo, assim você não precisa preencher tudo de novo amanhã.</li>
    <li>Clique no botão "Iniciar Download".</li>
    <li>APENAS NA PRIMEIRA VEZ: Uma janela vai aparecer pedindo o seu número de telefone e o código de verificação enviado pelo Telegram no seu celular. Se você usa senha de duas etapas (2FA), ela também será pedida. Isso é normal e seguro, o login acontece diretamente nos servidores do Telegram.</li>
    <li>Pronto! O programa começará a baixar as mídias. Ele organiza as pastas usando as mensagens de texto do canal como nome das pastas.</li>
</ol>
<p><strong>ARQUIVOS REPETIDOS</strong><br>
Se o programa tentar baixar um arquivo que já existe na pasta, ele pausará e mostrará uma tela de conflito. Lá você pode escolher se quer renomear, ignorar, substituir o arquivo antigo, ou pedir para ele ignorar automaticamente todos os repetidos dali para frente.</p>""",

    'en': """
<p><strong>STEP BY STEP: HOW TO DOWNLOAD FILES FROM TELEGRAM</strong></p>
<p>This program allows you to automatically download all files from a Telegram channel, organizing them into folders. To get started, follow the steps below:</p>
<p><strong>STEP 1: GET YOUR CREDENTIALS (API ID and API Hash)</strong><br>
For the program to communicate with Telegram on your behalf, it needs official authorization. You only need to do this once.</p>
<ol>
    <li>Access the official Telegram developers website: <a target="_blank" href="https://my.telegram.org">https://my.telegram.org</a></li>
    <li>Log in by entering your phone number (with the country code, e.g., +1234567890).</li>
    <li>Telegram will send a confirmation code on your app (not via SMS). Enter this code on the website.</li>
    <li>Click on the "API development tools" option.</li>
    <li>Fill out the form that appears (you can put any name in "App title" and "Short name").</li>
    <li>After creating, the page will show your "App api_id" (a number) and "App api_hash" (a long code mixing letters and numbers).</li>
    <li>Copy these two values and paste them here in the program in the "API ID" and "API Hash" fields.</li>
</ol>
<p><strong>STEP 2: CONFIGURE THE DOWNLOAD IN THE PROGRAM</strong></p>
<ol>
    <li>Channel (link or @user): Enter where you want to download from. You can paste the full link (e.g., t.me/channel_name) or just the handle (e.g., @channel_name).</li>
    <li>Destination folder: Click "Browse..." and choose which folder on your computer the files should be saved to.</li>
    <li>Session name: Leave the default or change it to a name of your choice. This creates a file that remembers your login so you don't have to enter your phone number again.</li>
</ol>
<p><strong>STEP 3: START THE PROCESS</strong></p>
<ol>
    <li>We suggest clicking "Save Settings" first in the File menu, so you don't have to fill everything out again tomorrow.</li>
    <li>Click the "Start Download" button.</li>
    <li>FIRST TIME ONLY: A window will appear asking for your phone number and the verification code sent by Telegram to your phone. If you use a two-step password (2FA), it will also be requested. This is normal and safe, the login happens directly on Telegram's servers.</li>
    <li>Done! The program will start downloading the media. It organizes the folders using the text messages from the channel as folder names.</li>
</ol>
<p><strong>REPEATED FILES</strong><br>
If the program tries to download a file that already exists in the folder, it will pause and show a conflict screen. There you can choose whether you want to rename, ignore, replace the old file, or ask it to automatically ignore all repeated ones from then on.</p>"""
}

def limpar_nome_pasta(nome):
    nome = nome.replace('\n', ' ').strip()
    nome = nome[:50]
    return re.sub(r'[\\/*?:"<>|]', "", nome)

def carregar_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def salvar_config(dados):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

class DownloadCancelado(Exception):
    pass

# ==========================================
# PONTE QML <-> PYTHON (BACKEND)
# ==========================================
class DownloaderBackend(QObject):
    logMessage = Signal(str)
    statusChanged = Signal(str)
    progressChanged = Signal(int)
    folderChanged = Signal(str)
    runStateChanged = Signal(bool)
    langChanged = Signal()
    configLoaded = Signal(dict)
    
    requestInput = Signal(str, str, str, bool) 
    requestConflict = Signal(dict)
    showToast = Signal(str, str)

    def __init__(self):
        super().__init__()
        self._lang = 'pt'
        self.rodando = False
        self.cancelar_evento = threading.Event()
        self.fila_input = queue.Queue(maxsize=1)
        self.loop = None
        self.client = None
        self.thread_trabalho = None  # Armazena referência da thread para limpeza segura
        
        config = carregar_config()
        self._lang = config.get('idioma', 'pt')

    @Property(dict, notify=langChanged)
    def tr(self):
        return TRANSLATIONS.get(self._lang, TRANSLATIONS['pt'])

    @Property(str, notify=langChanged)
    def tutorialText(self):
        return TUTORIAL_TEXTS.get(self._lang, TUTORIAL_TEXTS['pt'])

    @Property(str, notify=langChanged)
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, value):
        if value in TRANSLATIONS and self._lang != value:
            self._lang = value
            self.langChanged.emit()

    @Slot()
    def initializeConfig(self):
        config = carregar_config()
        if not config.get('sessao'):
            config['sessao'] = 'minha_sessao_telegram'
        self.configLoaded.emit(config)

    @Slot(dict)
    def saveConfig(self, dados):
        dados['idioma'] = self._lang
        salvar_config(dados)
        self.showToast.emit("Sucesso", "Configurações salvas.")

    @Slot(result=str)
    def chooseFolder(self):
        pasta = QFileDialog.getExistingDirectory(None, "Escolher Pasta de Destino")
        return pasta if pasta else ""

    @Slot(str)
    def submitInput(self, valor):
        try:
            self.fila_input.put_nowait(valor)
        except queue.Full:
            pass

    @Slot()
    def stopProcess(self):
        if self.rodando:
            self.cancelar_evento.set()
            self.statusChanged.emit(self.tr['canceling'])
            try:
                self.fila_input.put_nowait(None)
            except queue.Full:
                pass

    @Slot()
    def shutdown(self):
        """Slot chamado ao encerrar o aplicativo, forçando uma finalização segura das threads."""
        self.stopProcess()
        
        # Desconecta o cliente forçadamente pela thread que comanda o EventLoop
        if self.loop and self.loop.is_running() and self.client:
            try:
                asyncio.run_coroutine_threadsafe(self.client.disconnect(), self.loop)
            except Exception:
                pass
                
        # Aguarda a finalização limpa da thread de trabalho (máximo 3 segundos para não congelar)
        if self.thread_trabalho and self.thread_trabalho.is_alive():
            self.thread_trabalho.join(timeout=3.0)

    @Slot(str, str, str, str, str)
    def startProcess(self, api_id, api_hash, canal, pasta, sessao):
        if self.rodando: return

        if not api_id or not api_hash or not canal or not pasta:
            self.showToast.emit("Erro", self.tr['req_fields'])
            return

        try:
            api_id_int = int(api_id)
        except ValueError:
            self.showToast.emit("Erro", self.tr['invalid_api'])
            return

        self.cancelar_evento.clear()
        self.rodando = True
        self.runStateChanged.emit(True)
        self.progressChanged.emit(0)
        self.statusChanged.emit(self.tr['starting'])
        self.folderChanged.emit(self.tr['curr_folder'])
        
        self.saveConfig({'api_id': api_id, 'api_hash': api_hash, 'canal': canal, 'pasta': pasta, 'sessao': sessao})
        
        # A sessão também é salva na pasta de execução para não se perder caso rode o executável noutra pasta
        caminho_sessao = os.path.join(EXEC_DIR, sessao)

        self.thread_trabalho = threading.Thread(
            target=self._executar_loop,
            args=(api_id_int, api_hash, canal, pasta, caminho_sessao),
            daemon=True
        )
        self.thread_trabalho.start()

    def _executar_loop(self, api_id, api_hash, canal, pasta, caminho_sessao):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_until_complete(self._processo_principal(api_id, api_hash, canal, pasta, caminho_sessao))
        except Exception as e:
            self.logMessage.emit(f"Erro fatal: {str(e)}")
        finally:
            self.loop.close()
            self.loop = None
            self.rodando = False
            self.runStateChanged.emit(False)

    def _pedir_input(self, tipo_requisicao):
        while not self.fila_input.empty():
            self.fila_input.get()
            
        t = self.tr
        if tipo_requisicao == 'telefone':
            self.requestInput.emit('telefone', t['login_title'], t['phone_msg'], False)
        elif tipo_requisicao == 'codigo':
            self.requestInput.emit('codigo', t['login_title'], t['code_msg'], False)
        elif tipo_requisicao == 'senha':
            self.requestInput.emit('senha', t['login_title'], t['pass_msg'], True)
            
        resposta = self.fila_input.get()
        if self.cancelar_evento.is_set() or resposta is None:
            raise DownloadCancelado()
        return resposta

    async def _processo_principal(self, api_id, api_hash, canal_alvo, pasta_base, sessao):
        self.logMessage.emit(f"--> Conectando em {canal_alvo}")
        os.makedirs(pasta_base, exist_ok=True)

        self.client = TelegramClient(sessao, api_id, api_hash)

        try:
            await self.client.start(
                phone=lambda: self._pedir_input('telefone'),
                code_callback=lambda: self._pedir_input('codigo'),
                password=lambda: self._pedir_input('senha'),
            )
        except DownloadCancelado:
            self._finalizar_com_mensagem(self.tr['canceled'])
            return
        except Exception as e:
            self.logMessage.emit(f"Erro de Conexão/Auth: {e}")
            self._finalizar_com_mensagem(f"{self.tr['error']} {e}")
            return

        pasta_atual = os.path.join(pasta_base, "00_Sem_Modulo")
        pular_identicos = False

        try:
            async for mensagem in self.client.iter_messages(canal_alvo, reverse=True):
                if self.cancelar_evento.is_set():
                    self._finalizar_com_mensagem(self.tr['canceled'])
                    return

                if mensagem.text and not mensagem.media:
                    nome_limpo = limpar_nome_pasta(mensagem.text)
                    if nome_limpo:
                        pasta_atual = os.path.join(pasta_base, nome_limpo)
                        os.makedirs(pasta_atual, exist_ok=True)
                        self.folderChanged.emit(self.tr['curr_folder'].replace("-", nome_limpo))
                        self.logMessage.emit(f"[+] Diretório: {nome_limpo}")

                elif mensagem.media and hasattr(mensagem, 'file') and mensagem.file:
                    os.makedirs(pasta_atual, exist_ok=True)
                    nome_arquivo = mensagem.file.name or f"file_{mensagem.id}{mensagem.file.ext or '.bin'}"
                    caminho_esperado = os.path.join(pasta_atual, nome_arquivo)
                    caminho_final = caminho_esperado
                    tamanho_remoto = mensagem.file.size or 0
                    pular_arquivo = False

                    if os.path.exists(caminho_esperado):
                        tamanho_local = os.path.getsize(caminho_esperado)
                        tamanhos_iguais = tamanho_local == tamanho_remoto

                        if pular_identicos and tamanhos_iguais:
                            continue

                        while not self.fila_input.empty():
                            self.fila_input.get()
                            
                        dados_conflito = {
                            'arquivo': nome_arquivo,
                            'tam_local': tamanho_local / (1024*1024),
                            'tam_remoto': tamanho_remoto / (1024*1024),
                            'iguais': tamanhos_iguais
                        }
                        self.requestConflict.emit(dados_conflito)
                        
                        escolha = self.fila_input.get() 
                        if escolha is None or self.cancelar_evento.is_set():
                            raise DownloadCancelado()

                        if escolha == '1': 
                            base, ext = os.path.splitext(nome_arquivo)
                            contador = 2
                            caminho_final = os.path.join(pasta_atual, f"{base} ({contador}){ext}")
                            while os.path.exists(caminho_final):
                                contador += 1
                                caminho_final = os.path.join(pasta_atual, f"{base} ({contador}){ext}")
                        elif escolha == '2': 
                            pular_arquivo = True
                        elif escolha == '3': 
                            os.remove(caminho_esperado)
                        elif escolha == '4': 
                            pular_identicos = True
                            pular_arquivo = True

                    if pular_arquivo:
                        continue

                    self.statusChanged.emit(nome_arquivo)
                    self.logMessage.emit(f"Baixando: {nome_arquivo}")

                    ultimo_pct = [-1]
                    def progresso(recebido, total, _ultimo=ultimo_pct):
                        if self.cancelar_evento.is_set():
                            raise DownloadCancelado()
                        pct = int(recebido * 100 / total) if total else 0
                        if pct != _ultimo[0]:
                            _ultimo[0] = pct
                            self.progressChanged.emit(pct)

                    try:
                        await self.client.download_media(mensagem, file=caminho_final, progress_callback=progresso)
                        self.progressChanged.emit(0)
                    except FileReferenceExpiredError:
                        msg_att = await self.client.get_messages(canal_alvo, ids=mensagem.id)
                        await self.client.download_media(msg_att, file=caminho_final, progress_callback=progresso)
                        self.progressChanged.emit(0)
                    except DownloadCancelado:
                        raise

            self._finalizar_com_mensagem(self.tr['done'])

        except DownloadCancelado:
            self._finalizar_com_mensagem(self.tr['canceled'])
        except Exception as e:
            self.logMessage.emit(f"Erro no fluxo: {e}")
            self._finalizar_com_mensagem(f"{self.tr['error']} {e}")
        finally:
            await self.client.disconnect()

    def _finalizar_com_mensagem(self, msg):
        self.statusChanged.emit(msg)
        self.logMessage.emit(f"--- {msg} ---")
        self.progressChanged.emit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Busca o icon.ico na pasta do executável, com fallback para icon.png
    icon_path = os.path.join(BASE_DIR, "icon.ico")
    if not os.path.exists(icon_path):
        icon_path = os.path.join(BASE_DIR, "icon.png")

    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    QQuickStyle.setStyle("Material")

    engine = QQmlApplicationEngine()
    backend = DownloaderBackend()
    engine.rootContext().setContextProperty("backend", backend)

    # Conecta o sinal de encerramento do app à rotina de limpeza de threads
    app.aboutToQuit.connect(backend.shutdown)

    qml_file = os.path.join(BASE_DIR, "main.qml")
    engine.load(QUrl.fromLocalFile(qml_file))

    if not engine.rootObjects():
        sys.exit(-1)

    ret = app.exec()
    del engine
    sys.exit(ret)
