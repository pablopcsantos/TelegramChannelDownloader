*Read this in other languages: [Português](README.md)*

---

*This program automates the download and organization of courses stored in Telegram channels. It reads the message history, converts structural texts into folders on the HD, and downloads all files, like videos and PDFs, directly to the correct modules, restoring the original structure.*

## TELEGRAM COURSE EXTRACTOR AND ORGANIZER

This graphical application automates the entire process of downloading and organizing course files made available in Telegram channels. When executed, it scans the message history of the desired channel.

Every time it identifies a structural text (such as a module title), it creates a corresponding folder on your hard drive. Then, it downloads all attached files, including videos, PDFs, spreadsheets, and compressed files, saving them directly into their respective folders. This ensures the restoration of the original course structure in a simple and automated way.

## KEY FEATURES

* **Graphical User Interface (GUI):** Easy-to-use interface with native support for themes (Light and Dark) and multiple languages (English and Portuguese).
* **Safe Exit:** Once the files have started downloading, the process can be stopped safely and immediately at any time by clicking the "STOP" button.
* **Smart Conflict Resolution:** If the script detects that a file with the same name already exists in your folder, it will pause the download and display the sizes of both files (the local one and the Telegram one). You can then choose between actions: download a new numbered copy, skip this download, overwrite the old local file with the new one, or automatically skip all identical files in that session.

## TUTORIAL ON HOW TO RUN THE APP

### STEP 1: GET TELEGRAM CREDENTIALS

* Access the website `my.telegram.org` through your browser and log in using your mobile number.
* Click on the *API development tools* option.
* Fill in the `App title` and `Short name` fields with the name you desire. Under *Platform*, leave it as *Desktop*.
* Click the *Create application* button.
* On the next page, copy the values presented in `App api_id`, which is a sequence of numbers, and `App api_hash`, which is a sequence mixing letters and numbers. Save this data.

### STEP 2: CONFIGURE THE DOWNLOAD

* Open the `TelegramChannelDownloader.exe` application (or run the python script via terminal using `python main.py`).
* In the **Session name** field, choose a name to save your login session (this prevents you from having to log in again in the future).
* Insert the values copied from Step 1 into the **API ID** and **API Hash** fields.
* In the **Channel** field, insert the link or the ID of the Telegram channel that contains the course (Ex: 't.me/channel_name').
* Select the full path of the folder on your computer or external HD where the course should be saved by clicking **Browse...**.
* Click "Save Settings" in the File menu so you do not have to fill it in again next time.

### STEP 3: START DOWNLOAD AND LOGIN

* Click the blue **START DOWNLOAD** button.
* As it will be the first time you run the program, it will ask you to confirm your identity. A pop-up window will ask you to enter your mobile number with the country code.
* Telegram will send a numeric verification code directly to the app on your cell phone.
* Type this code in the application's pop-up window.
* If you have Two-Step Verification (2FA) enabled, you will be prompted for your password.
* Done. From this moment on, the application will start working alone, creating the folders and downloading all the channel's materials to your computer.

### AUTHORSHIP AND DEVELOPMENT

Automation application independently developed by [**Pablo Phillipe Cândido dos Santos**](http://lattes.cnpq.br/9500873674712528), intended to download and organize files made available through Telegram channels, with automated restoration of the original structure of the materials.

The development process involved the use of generative artificial intelligence tools as an auxiliary resource, while the conception, implementation, integration, and verification of the project remained under the author's responsibility.
