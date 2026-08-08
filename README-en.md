# Telegram Channel Downloader

*Read this in other languages: [Português](README.md)*

---

*This program automates the download and organization of contents stored in Telegram channels. It reads the message history, converts structural texts into folders on the HD, and downloads all files, like videos and PDFs, directly to the correct folders, restoring the original structure.*

## 📂 TELEGRAM CHANNEL EXTRACTOR AND ORGANIZER

This graphical application automates the entire process of downloading and organizing files made available in Telegram channels. When executed, it scans the message history of the desired channel.

Every time it identifies a structural text (such as a topic or section title), it creates a corresponding folder on your hard drive. Then, it downloads all attached files, including videos, PDFs, spreadsheets, and compressed files, saving them directly into their respective folders. This ensures the restoration of the original content structure in a simple and automated way.

## ⚙️ KEY FEATURES

* **Graphical User Interface (GUI):** Easy-to-use interface with native support for themes (Light and Dark) and multiple languages (English and Portuguese).
* **Safe Exit:** Once the files have started downloading, the process can be stopped safely and immediately at any time by clicking the "STOP" button.
* **Smart Conflict Resolution:** If the script detects that a file with the same name already exists in your folder, it will pause the download and display the sizes of both files (the local one and the Telegram one). You can then choose between actions: download a new numbered copy, skip this download, overwrite the old local file with the new one, or automatically skip all identical files in that session.

## 🚀 TUTORIAL ON HOW TO USE THE COMPILED PROGRAM (.exe)

### Step 01 - Get Telegram Credentials

* Access the website `my.telegram.org` through your browser and log in using your mobile number.
* Click on the *API development tools* option.
* Fill in the `App title` and `Short name` fields with the name you desire. Under *Platform*, leave it as *Desktop*.
* Click the *Create application* button.
* On the next page, copy the values presented in `App api_id`, which is a sequence of numbers, and `App api_hash`, which is a sequence mixing letters and numbers. Save this data.

### Step 02 - Configure the Download

* Open the `TelegramChannelDownloader.exe` application (or run the python script via terminal using `python main.py`).
* In the **Session name** field, choose a name to save your login session (this prevents you from having to log in again in the future).
* Insert the values copied from Step 1 into the **API ID** and **API Hash** fields.
* In the **Channel** field, insert the link or the ID of the Telegram channel that contains the files (Ex: 't.me/channel_name').
* Select the full path of the folder on your computer or external HD where the contents should be saved by clicking **Browse...**.
* Click "Save Settings" in the File menu so you do not have to fill it in again next time.

### Step 03 - Start Download and Login

* Click the blue **START DOWNLOAD** button.
* As it will be the first time you run the program, it will ask you to confirm your identity. A pop-up window will ask you to enter your mobile number with the country code.
* Telegram will send a numeric verification code directly to the app on your cell phone.
* Type this code in the application's pop-up window.
* If you have Two-Step Verification (2FA) enabled, you will be prompted for your password.
* Done. From this moment on, the application will start working alone, creating the folders and downloading all the channel's materials to your computer.

## 🛠️ TUTORIAL ON HOW TO COMPILE THE PROGRAM FROM SOURCE CODE

For users who want to download the source code, install the dependencies, and generate the `.exe` file locally, the project uses a Python virtual environment (`venv`) named `env_downloader`.

> **Note:** The procedure below assumes that Python is installed and available through the `py` command, and that the project's necessary files, including `build.spec`, are present in the project folder.

### Step 01 - Download the Source Code

Clone the repository or download the project files, then open a terminal in the project's root folder.

In PowerShell or Command Prompt (CMD), navigate to the corresponding folder:

```powershell
cd "C:\Path\To\Your\Folder"
```

Replace the path with the location where the project was saved.

### Step 02 - Create the Virtual Environment

If the virtual environment hasn't been created yet, use Python's native initializer:

```powershell
py -m venv env_downloader
```

This command will create the `env_downloader` virtual environment inside the project folder.

### Step 03 - Activate the Virtual Environment

Activation depends on the terminal being used.

#### PowerShell

Run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\env_downloader\Scripts\Activate.ps1
```

#### Command Prompt (CMD)

Run:

```cmd
env_downloader\Scripts\activate.bat
```

After activation, the name of the virtual environment (`env_downloader`) should appear at the beginning of the command line.

### Step 04 - Install the Dependencies

With the virtual environment activated, install the dependencies needed to run and compile the program.

You can install them directly:

```powershell
pip install PySide6 telethon pyinstaller
```

Or, if the project contains a `requirements.txt` file, use:

```powershell
pip install -r requirements.txt
```

### Step 05 - Generate the `.exe` File

With the dependencies installed and the virtual environment still activated, run PyInstaller using the project's spec file:

```powershell
pyinstaller build.spec
```

PyInstaller will use the settings defined in `build.spec` to generate the executable.

Once the process is complete, the files generated by PyInstaller will be in the output folders specified by the build configuration.

### 👤 AUTHORSHIP AND DEVELOPMENT

Automation application independently developed by [**Pablo Phillipe Cândido dos Santos**](http://lattes.cnpq.br/9500873674712528), intended to download and organize files made available through Telegram channels, with automated restoration of the original structure of the materials.

The development process involved the use of generative artificial intelligence tools as an auxiliary resource, while the conception, implementation, integration, and verification of the project remained under the author's responsibility.
