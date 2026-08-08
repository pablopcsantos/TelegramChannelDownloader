import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: window
    width: 800
    height: 700
    minimumWidth: 600
    minimumHeight: 500
    visible: true
    title: backend.tr.title
    
    font.pixelSize: 13 

    property bool isDarkMode: true
    Material.theme: isDarkMode ? Material.Dark : Material.Light
    Material.accent: Material.Blue

    Component.onCompleted: {
        backend.initializeConfig()
    }

    function saveCurrentConfig() {
        backend.saveConfig({
            'api_id': apiIdField.text,
            'api_hash': apiHashField.text,
            'canal': channelField.text,
            'pasta': folderField.text,
            'sessao': sessionField.text
        })
    }

    // --- MENU SUPERIOR ---
    menuBar: MenuBar {
        Menu {
            title: backend.tr.menu_file
            MenuItem { 
                text: backend.tr.menu_save
                onTriggered: saveCurrentConfig()
            }
            MenuSeparator {}
            MenuItem { 
                text: backend.tr.menu_exit
                onTriggered: Qt.quit()
            }
        }
        Menu {
            title: backend.tr.menu_view
            MenuItem { 
                text: backend.tr.menu_theme_light
                onTriggered: window.isDarkMode = false
            }
            MenuItem { 
                text: backend.tr.menu_theme_dark
                onTriggered: window.isDarkMode = true
            }
        }
        Menu {
            title: backend.tr.menu_lang
            MenuItem { 
                text: "Português"
                onTriggered: backend.lang = 'pt'
            }
            MenuItem { 
                text: "English"
                onTriggered: backend.lang = 'en'
            }
        }
        Menu {
            title: backend.tr.menu_help
            MenuItem { 
                text: backend.tr.menu_tutorial
                onTriggered: tutorialDialog.open()
            }
            MenuItem { 
                text: backend.tr.menu_about
                onTriggered: aboutDialog.open()
            }
        }
    }

    Connections {
        target: backend

        function onConfigLoaded(config) {
            apiIdField.text = config.api_id || ""
            apiHashField.text = config.api_hash || ""
            channelField.text = config.canal || ""
            folderField.text = config.pasta || ""
            sessionField.text = config.sessao || ""
        }

        function onLogMessage(msg) { logArea.append(msg) }
        function onStatusChanged(status) { statusLabel.text = status }
        function onProgressChanged(val) { progressBar.value = val }
        function onFolderChanged(folder) { folderLabel.text = folder }
        
        function onRunStateChanged(running) {
            startBtn.enabled = !running
            stopBtn.enabled = running
            settingsGroup.enabled = !running
        }

        function onShowToast(title, msg) {
            toastDialog.title = title
            toastDialog.text = msg
            toastDialog.open()
        }

        function onRequestInput(id_req, title, msg, isPassword) {
            inputDialog.title = title
            inputLabel.text = msg
            inputField.text = ""
            inputField.echoMode = isPassword ? TextInput.Password : TextInput.Normal
            inputDialog.open()
        }

        function onRequestConflict(dados) {
            let msgStr = backend.tr.conflict_msg
            msgStr = msgStr.replace("{0}", dados.arquivo)
            msgStr = msgStr.replace("{1:.2f}", dados.tam_local.toFixed(2))
            msgStr = msgStr.replace("{2:.2f}", dados.tam_remoto.toFixed(2))
            
            conflictLabel.text = msgStr
            btnConflict4.visible = dados.iguais 
            conflictDialog.open()
        }
    }

    // --- DIALOGS E POPUPS DE AJUDA ---

    Dialog {
        id: tutorialDialog
        anchors.centerIn: parent
        width: Math.min(750, parent.width - 40)
        height: Math.min(600, parent.height - 40)
        modal: true
        title: backend.tr.menu_tutorial

        ScrollView {
            anchors.fill: parent
            clip: true
            
            Label {
                text: backend.tutorialText
                wrapMode: Label.Wrap
                textFormat: Label.RichText // Permite renderização HTML nativa
                font.pixelSize: 14
                width: parent.width
                onLinkActivated: function(link) { Qt.openUrlExternally(link) }
                
                MouseArea {
                    anchors.fill: parent
                    acceptedButtons: Qt.NoButton 
                    cursorShape: parent.hoveredLink ? Qt.PointingHandCursor : Qt.ArrowCursor
                }
            }
        }
        
        footer: DialogButtonBox {
            Button {
                text: "OK"
                DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
                onClicked: tutorialDialog.close()
            }
        }
    }

    Dialog {
        id: aboutDialog
        anchors.centerIn: parent
        width: 450
        modal: true
        title: backend.tr.about_title

        ColumnLayout {
            anchors.fill: parent
            spacing: 20

            Label {
                text: backend.tr.about_desc
                Layout.alignment: Qt.AlignHCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 13
            }
            
            Label {
                text: "<a href='http://lattes.cnpq.br/9500873674712528'>" + backend.tr.about_lattes + "</a>"
                Layout.alignment: Qt.AlignHCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 13
                font.underline: true
                onLinkActivated: Qt.openUrlExternally(link)
                
                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    acceptedButtons: Qt.NoButton 
                }
            }
        }
        
        footer: DialogButtonBox {
            Button {
                text: "OK"
                DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
                onClicked: aboutDialog.close()
            }
        }
    }

    Dialog {
        id: toastDialog
        anchors.centerIn: parent
        width: Math.min(400, parent.width - 40)
        modal: true
        closePolicy: Popup.NoAutoClose
        property alias text: toastLabel.text

        ColumnLayout {
            anchors.fill: parent
            Label {
                id: toastLabel
                wrapMode: Label.WordWrap
                Layout.fillWidth: true
            }
        }
        footer: DialogButtonBox {
            Button {
                text: "OK"
                DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
                Material.background: Material.accent
                Material.foreground: "white"
                onClicked: toastDialog.close()
            }
        }
    }

    Dialog {
        id: inputDialog
        anchors.centerIn: parent
        width: Math.min(400, parent.width - 40)
        modal: true
        closePolicy: Popup.NoAutoClose

        ColumnLayout {
            anchors.fill: parent
            spacing: 15
            Label {
                id: inputLabel
                wrapMode: Label.WordWrap
                Layout.fillWidth: true
            }
            TextField {
                id: inputField
                Layout.fillWidth: true
                selectByMouse: true
            }
        }
        footer: DialogButtonBox {
            Button {
                text: backend.tr.btn_confirm
                DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
                Material.background: Material.accent
                Material.foreground: "white"
            }
            Button {
                text: backend.tr.btn_cancel
                DialogButtonBox.buttonRole: DialogButtonBox.RejectRole
            }
            onAccepted: backend.submitInput(inputField.text.trim())
            onRejected: backend.submitInput("")
        }
    }

    Dialog {
        id: conflictDialog
        anchors.centerIn: parent
        width: Math.min(450, parent.width - 40)
        modal: true
        title: backend.tr.conflict_title
        closePolicy: Popup.NoAutoClose
        
        ColumnLayout {
            anchors.fill: parent
            spacing: 10

            Label {
                id: conflictLabel
                wrapMode: Label.WordWrap
                Layout.fillWidth: true
                Layout.bottomMargin: 10
            }

            Button {
                text: "1 - " + backend.tr.btn_new_name
                Layout.fillWidth: true
                onClicked: { conflictDialog.close(); backend.submitInput("1") }
            }
            Button {
                text: "2 - " + backend.tr.btn_ignore
                Layout.fillWidth: true
                onClicked: { conflictDialog.close(); backend.submitInput("2") }
            }
            Button {
                text: "3 - " + backend.tr.btn_replace
                Layout.fillWidth: true
                onClicked: { conflictDialog.close(); backend.submitInput("3") }
            }
            Button {
                id: btnConflict4
                text: "4 - " + backend.tr.btn_ignore_all
                Layout.fillWidth: true
                onClicked: { conflictDialog.close(); backend.submitInput("4") }
            }
        }
    }

    // --- INTERFACE PRINCIPAL ---

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15

        // Frame de Configurações
        GroupBox {
            id: settingsGroup
            title: backend.tr.settings
            Layout.fillWidth: true

            GridLayout {
                anchors.fill: parent
                columns: 3
                columnSpacing: 10
                rowSpacing: 5

                Label { text: backend.tr.api_id }
                TextField {
                    id: apiIdField
                    Layout.fillWidth: true
                    Layout.columnSpan: 2
                    selectByMouse: true
                }

                Label { text: backend.tr.api_hash }
                TextField {
                    id: apiHashField
                    Layout.fillWidth: true
                    echoMode: showHashCheck.checked ? TextInput.Normal : TextInput.Password
                    selectByMouse: true
                }
                CheckBox {
                    id: showHashCheck
                    text: "👁️"
                }

                Label { text: backend.tr.channel }
                TextField {
                    id: channelField
                    Layout.fillWidth: true
                    Layout.columnSpan: 2
                    selectByMouse: true
                }

                Label { text: backend.tr.dest_folder }
                TextField {
                    id: folderField
                    Layout.fillWidth: true
                    selectByMouse: true
                }
                Button {
                    text: backend.tr.browse
                    onClicked: {
                        var path = backend.chooseFolder()
                        if (path !== "") folderField.text = path
                    }
                }

                Label { text: backend.tr.session_name }
                TextField {
                    id: sessionField
                    Layout.fillWidth: true
                    Layout.columnSpan: 2
                    selectByMouse: true
                }
            }
        }

        // Botões de Ação
        RowLayout {
            Layout.fillWidth: true
            spacing: 10

            Button {
                id: startBtn
                text: backend.tr.btn_start
                font.bold: true
                Layout.fillWidth: true
                Material.background: "#2196F3"
                Material.foreground: "white"
                
                onClicked: {
                    logArea.text = ""
                    backend.startProcess(
                        apiIdField.text.trim(),
                        apiHashField.text.trim(),
                        channelField.text.trim(),
                        folderField.text.trim(),
                        sessionField.text.trim()
                    )
                }
            }

            Button {
                id: stopBtn
                text: backend.tr.btn_stop
                enabled: false
                font.bold: true
                Layout.fillWidth: true
                Material.background: Material.Red
                Material.foreground: "white"
                onClicked: backend.stopProcess()
            }
        }

        // Progresso e Status
        ColumnLayout {
            Layout.fillWidth: true
            spacing: 5

            Label {
                id: statusLabel
                text: backend.tr.status_ready
                font.bold: true
                elide: Label.ElideRight
                Layout.fillWidth: true
            }

            ProgressBar {
                id: progressBar
                from: 0
                to: 100
                value: 0
                Layout.fillWidth: true
            }

            Label {
                id: folderLabel
                text: backend.tr.curr_folder
                color: "gray"
                elide: Label.ElideRight
                Layout.fillWidth: true
            }
        }

        // Console de Logs
        GroupBox {
            title: backend.tr.log_title
            Layout.fillWidth: true
            Layout.fillHeight: true

            ScrollView {
                anchors.fill: parent
                TextArea {
                    id: logArea
                    readOnly: true
                    selectByMouse: true
                    font.family: "Consolas"
                    wrapMode: TextArea.Wrap
                    onTextChanged: cursorPosition = text.length
                }
            }
        }
    }
}