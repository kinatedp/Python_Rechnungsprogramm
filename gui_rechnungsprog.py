# Form implementation generated from reading ui file 'gui_rechnungsprog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog.resize(1728, 962)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1271, 921))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.cbClients = QtWidgets.QComboBox(self.tab)
        self.cbClients.setGeometry(QtCore.QRect(10, 20, 281, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbClients.setFont(font)
        self.cbClients.setEditable(False)
        self.cbClients.setObjectName("cbClients")
        self.cbClients.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(910, 10, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(910, 30, 241, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 110, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tbRechNummer = QtWidgets.QLineEdit(self.tab)
        self.tbRechNummer.setGeometry(QtCore.QRect(910, 282, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tbRechNummer.setFont(font)
        self.tbRechNummer.setInputMask("9999-999")
        self.tbRechNummer.setClearButtonEnabled(False)
        self.tbRechNummer.setObjectName("tbRechNummer")
        self.tbAuftragsort = QtWidgets.QLineEdit(self.tab)
        self.tbAuftragsort.setGeometry(QtCore.QRect(180, 110, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tbAuftragsort.setFont(font)
        self.tbAuftragsort.setObjectName("tbAuftragsort")
        self.tbAuftragsdatum = QtWidgets.QDateEdit(self.tab)
        self.tbAuftragsdatum.setGeometry(QtCore.QRect(680, 110, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tbAuftragsdatum.setFont(font)
        self.tbAuftragsdatum.setObjectName("tbAuftragsdatum")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(510, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(510, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tbRechDatum = QtWidgets.QDateEdit(self.tab)
        self.tbRechDatum.setGeometry(QtCore.QRect(680, 80, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tbRechDatum.setFont(font)
        self.tbRechDatum.setObjectName("tbRechDatum")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 160, 881, 781))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.twPositionen = QtWidgets.QTableWidget(self.tab_3)
        self.twPositionen.setGeometry(QtCore.QRect(0, 10, 871, 671))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.twPositionen.setFont(font)
        self.twPositionen.setObjectName("twPositionen")
        self.twPositionen.setColumnCount(5)
        self.twPositionen.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twPositionen.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPositionen.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPositionen.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPositionen.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPositionen.setHorizontalHeaderItem(4, item)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.twAbzuege = QtWidgets.QTableWidget(self.tab_4)
        self.twAbzuege.setGeometry(QtCore.QRect(0, 10, 871, 701))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.twAbzuege.setFont(font)
        self.twAbzuege.setObjectName("twAbzuege")
        self.twAbzuege.setColumnCount(5)
        self.twAbzuege.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twAbzuege.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAbzuege.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAbzuege.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAbzuege.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAbzuege.setHorizontalHeaderItem(4, item)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(900, 260, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnSave = QtWidgets.QPushButton(self.tab)
        self.btnSave.setEnabled(False)
        self.btnSave.setGeometry(QtCore.QRect(900, 490, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.tbAuftragsnummer = QtWidgets.QLineEdit(self.tab)
        self.tbAuftragsnummer.setGeometry(QtCore.QRect(180, 80, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tbAuftragsnummer.setFont(font)
        self.tbAuftragsnummer.setPlaceholderText("")
        self.tbAuftragsnummer.setObjectName("tbAuftragsnummer")
        self.lCustomer_street = QtWidgets.QLabel(self.tab)
        self.lCustomer_street.setGeometry(QtCore.QRect(300, 16, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lCustomer_street.setFont(font)
        self.lCustomer_street.setObjectName("lCustomer_street")
        self.lCustomer_city = QtWidgets.QLabel(self.tab)
        self.lCustomer_city.setGeometry(QtCore.QRect(300, 40, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lCustomer_city.setFont(font)
        self.lCustomer_city.setObjectName("lCustomer_city")
        self.teCurrRechSum = QtWidgets.QLineEdit(self.tab)
        self.teCurrRechSum.setGeometry(QtCore.QRect(910, 362, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.teCurrRechSum.setFont(font)
        self.teCurrRechSum.setAutoFillBackground(False)
        self.teCurrRechSum.setStyleSheet("background-color: rgb(210,210,210);")
        self.teCurrRechSum.setInputMask("")
        self.teCurrRechSum.setReadOnly(True)
        self.teCurrRechSum.setObjectName("teCurrRechSum")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(900, 340, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lMsgNoRechOutputDir = QtWidgets.QLabel(self.tab)
        self.lMsgNoRechOutputDir.setGeometry(QtCore.QRect(900, 550, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lMsgNoRechOutputDir.setFont(font)
        self.lMsgNoRechOutputDir.setStyleSheet("color: rgb(255,0,0);")
        self.lMsgNoRechOutputDir.setObjectName("lMsgNoRechOutputDir")
        self.chk_OpenFileAfterCreation = QtWidgets.QCheckBox(self.tab)
        self.chk_OpenFileAfterCreation.setGeometry(QtCore.QRect(950, 570, 181, 21))
        self.chk_OpenFileAfterCreation.setChecked(True)
        self.chk_OpenFileAfterCreation.setObjectName("chk_OpenFileAfterCreation")
        self.btnResetGUI = QtWidgets.QPushButton(self.tab)
        self.btnResetGUI.setGeometry(QtCore.QRect(1190, 0, 75, 24))
        self.btnResetGUI.setObjectName("btnResetGUI")
        self.chk_AddTaxes = QtWidgets.QGroupBox(self.tab)
        self.chk_AddTaxes.setGeometry(QtCore.QRect(910, 410, 191, 71))
        self.chk_AddTaxes.setCheckable(True)
        self.chk_AddTaxes.setObjectName("chk_AddTaxes")
        self.label_12 = QtWidgets.QLabel(self.chk_AddTaxes)
        self.label_12.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label_12.setObjectName("label_12")
        self.teCurrRechSumWithTax = QtWidgets.QLineEdit(self.chk_AddTaxes)
        self.teCurrRechSumWithTax.setGeometry(QtCore.QRect(110, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teCurrRechSumWithTax.setFont(font)
        self.teCurrRechSumWithTax.setAutoFillBackground(False)
        self.teCurrRechSumWithTax.setStyleSheet("background-color: rgb(210,210,210);")
        self.teCurrRechSumWithTax.setInputMask("")
        self.teCurrRechSumWithTax.setReadOnly(True)
        self.teCurrRechSumWithTax.setObjectName("teCurrRechSumWithTax")
        self.teCurrRechTax = QtWidgets.QLineEdit(self.chk_AddTaxes)
        self.teCurrRechTax.setGeometry(QtCore.QRect(110, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.teCurrRechTax.setFont(font)
        self.teCurrRechTax.setAutoFillBackground(False)
        self.teCurrRechTax.setStyleSheet("background-color: rgb(210,210,210);")
        self.teCurrRechTax.setInputMask("")
        self.teCurrRechTax.setReadOnly(True)
        self.teCurrRechTax.setObjectName("teCurrRechTax")
        self.label_14 = QtWidgets.QLabel(self.chk_AddTaxes)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lE_pathRechnungen_auswert = QtWidgets.QLineEdit(self.tab_5)
        self.lE_pathRechnungen_auswert.setGeometry(QtCore.QRect(10, 30, 511, 22))
        self.lE_pathRechnungen_auswert.setReadOnly(True)
        self.lE_pathRechnungen_auswert.setObjectName("lE_pathRechnungen_auswert")
        self.btnSelDirRechAuswert = QtWidgets.QPushButton(self.tab_5)
        self.btnSelDirRechAuswert.setGeometry(QtCore.QRect(540, 30, 161, 26))
        self.btnSelDirRechAuswert.setObjectName("btnSelDirRechAuswert")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 981, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 981, 21))
        self.label_11.setObjectName("label_11")
        self.lCnt_FilesForAuswert = QtWidgets.QLabel(self.tab_5)
        self.lCnt_FilesForAuswert.setGeometry(QtCore.QRect(130, 60, 981, 21))
        self.lCnt_FilesForAuswert.setObjectName("lCnt_FilesForAuswert")
        self.btn_ErstelleAuswertung = QtWidgets.QPushButton(self.tab_5)
        self.btn_ErstelleAuswertung.setEnabled(False)
        self.btn_ErstelleAuswertung.setGeometry(QtCore.QRect(10, 100, 211, 41))
        self.btn_ErstelleAuswertung.setObjectName("btn_ErstelleAuswertung")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 981, 16))
        self.label_7.setObjectName("label_7")
        self.lE_path2ConfigDir = QtWidgets.QLineEdit(self.tab_2)
        self.lE_path2ConfigDir.setEnabled(False)
        self.lE_path2ConfigDir.setGeometry(QtCore.QRect(10, 30, 511, 22))
        self.lE_path2ConfigDir.setReadOnly(True)
        self.lE_path2ConfigDir.setObjectName("lE_path2ConfigDir")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 370, 981, 16))
        self.label_8.setObjectName("label_8")
        self.lE_path2Output_rechnungen = QtWidgets.QLineEdit(self.tab_2)
        self.lE_path2Output_rechnungen.setGeometry(QtCore.QRect(10, 390, 511, 22))
        self.lE_path2Output_rechnungen.setReadOnly(True)
        self.lE_path2Output_rechnungen.setObjectName("lE_path2Output_rechnungen")
        self.btnSelDirConfig = QtWidgets.QPushButton(self.tab_2)
        self.btnSelDirConfig.setEnabled(False)
        self.btnSelDirConfig.setGeometry(QtCore.QRect(530, 30, 161, 26))
        self.btnSelDirConfig.setObjectName("btnSelDirConfig")
        self.btnSelDirOutputRech = QtWidgets.QPushButton(self.tab_2)
        self.btnSelDirOutputRech.setGeometry(QtCore.QRect(530, 390, 161, 26))
        self.btnSelDirOutputRech.setObjectName("btnSelDirOutputRech")
        self.btnOpenPosWithApp = QtWidgets.QPushButton(self.tab_2)
        self.btnOpenPosWithApp.setGeometry(QtCore.QRect(40, 280, 201, 41))
        self.btnOpenPosWithApp.setObjectName("btnOpenPosWithApp")
        self.btnOpenAbzWithApp = QtWidgets.QPushButton(self.tab_2)
        self.btnOpenAbzWithApp.setGeometry(QtCore.QRect(260, 280, 201, 41))
        self.btnOpenAbzWithApp.setObjectName("btnOpenAbzWithApp")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 511, 71))
        self.groupBox.setObjectName("groupBox")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(120, 20, 51, 16))
        self.label_13.setObjectName("label_13")
        self.chkShowLog = QtWidgets.QCheckBox(self.groupBox)
        self.chkShowLog.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.chkShowLog.setObjectName("chkShowLog")
        self.dsbTaxRate = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.dsbTaxRate.setGeometry(QtCore.QRect(120, 40, 62, 22))
        self.dsbTaxRate.setMaximum(999.99)
        self.dsbTaxRate.setObjectName("dsbTaxRate")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 511, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lFName_PathToRechOutputDir = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_PathToRechOutputDir.setGeometry(QtCore.QRect(190, 40, 201, 16))
        self.lFName_PathToRechOutputDir.setObjectName("lFName_PathToRechOutputDir")
        self.lFName_RechNr = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_RechNr.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.lFName_RechNr.setObjectName("lFName_RechNr")
        self.lFName_Positionen = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_Positionen.setGeometry(QtCore.QRect(190, 60, 191, 16))
        self.lFName_Positionen.setObjectName("lFName_Positionen")
        self.lFName_Abzuege = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_Abzuege.setGeometry(QtCore.QRect(410, 60, 71, 16))
        self.lFName_Abzuege.setObjectName("lFName_Abzuege")
        self.lFName_LastRechYear = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_LastRechYear.setGeometry(QtCore.QRect(410, 40, 191, 16))
        self.lFName_LastRechYear.setObjectName("lFName_LastRechYear")
        self.lFName_Template_RechAuswertung = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_Template_RechAuswertung.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.lFName_Template_RechAuswertung.setObjectName("lFName_Template_RechAuswertung")
        self.lFName_Customer = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_Customer.setGeometry(QtCore.QRect(190, 80, 191, 16))
        self.lFName_Customer.setObjectName("lFName_Customer")
        self.lFName_PathToConfigDir = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_PathToConfigDir.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.lFName_PathToConfigDir.setObjectName("lFName_PathToConfigDir")
        self.lFName_UstSatz = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_UstSatz.setGeometry(QtCore.QRect(10, 80, 191, 16))
        self.lFName_UstSatz.setObjectName("lFName_UstSatz")
        self.lFName_Rechnungsmuster = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_Rechnungsmuster.setGeometry(QtCore.QRect(190, 20, 161, 16))
        self.lFName_Rechnungsmuster.setObjectName("lFName_Rechnungsmuster")
        self.lFName_ShowLog = QtWidgets.QLabel(self.groupBox_2)
        self.lFName_ShowLog.setGeometry(QtCore.QRect(410, 20, 191, 16))
        self.lFName_ShowLog.setObjectName("lFName_ShowLog")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(570, 80, 341, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnResetRechNumToOne = QtWidgets.QPushButton(self.groupBox_3)
        self.btnResetRechNumToOne.setGeometry(QtCore.QRect(10, 40, 161, 26))
        self.btnResetRechNumToOne.setObjectName("btnResetRechNumToOne")
        self.btnChangeRechNum = QtWidgets.QPushButton(self.groupBox_3)
        self.btnChangeRechNum.setGeometry(QtCore.QRect(170, 40, 161, 26))
        self.btnChangeRechNum.setObjectName("btnChangeRechNum")
        self.sbRechNumToSet = QtWidgets.QSpinBox(self.groupBox_3)
        self.sbRechNumToSet.setGeometry(QtCore.QRect(220, 20, 71, 22))
        self.sbRechNumToSet.setMaximum(999)
        self.sbRechNumToSet.setProperty("value", 1)
        self.sbRechNumToSet.setObjectName("sbRechNumToSet")
        self.tabWidget.addTab(self.tab_2, "")
        self.pTE_Logger = QtWidgets.QPlainTextEdit(Dialog)
        self.pTE_Logger.setEnabled(True)
        self.pTE_Logger.setGeometry(QtCore.QRect(1290, 60, 431, 871))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pTE_Logger.setFont(font)
        self.pTE_Logger.setAutoFillBackground(False)
        self.pTE_Logger.setStyleSheet("background-color: rgb(240,240,240);")
        self.pTE_Logger.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.pTE_Logger.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.pTE_Logger.setUndoRedoEnabled(False)
        self.pTE_Logger.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap)
        self.pTE_Logger.setReadOnly(True)
        self.pTE_Logger.setCenterOnScroll(True)
        self.pTE_Logger.setObjectName("pTE_Logger")
        self.lLogHeader = QtWidgets.QLabel(Dialog)
        self.lLogHeader.setGeometry(QtCore.QRect(1290, 40, 49, 16))
        self.lLogHeader.setObjectName("lLogHeader")
        self.label_4.setBuddy(self.calendarWidget)
        self.label_6.setBuddy(self.tbAuftragsnummer)
        self.label.setBuddy(self.tbAuftragsort)
        self.label_2.setBuddy(self.tbAuftragsdatum)
        self.label_3.setBuddy(self.tbRechDatum)
        self.label_5.setBuddy(self.tbRechNummer)
        self.label_9.setBuddy(self.teCurrRechSum)
        self.lMsgNoRechOutputDir.setBuddy(self.btnSave)
        self.label_12.setBuddy(self.teCurrRechSumWithTax)
        self.label_14.setBuddy(self.teCurrRechTax)
        self.label_10.setBuddy(self.lE_pathRechnungen_auswert)
        self.label_7.setBuddy(self.lE_path2ConfigDir)
        self.label_8.setBuddy(self.lE_path2Output_rechnungen)
        self.label_13.setBuddy(self.dsbTaxRate)
        self.lLogHeader.setBuddy(self.pTE_Logger)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.cbClients)
        Dialog.setTabOrder(self.cbClients, self.tbAuftragsnummer)
        Dialog.setTabOrder(self.tbAuftragsnummer, self.tbRechDatum)
        Dialog.setTabOrder(self.tbRechDatum, self.tbAuftragsort)
        Dialog.setTabOrder(self.tbAuftragsort, self.tbAuftragsdatum)
        Dialog.setTabOrder(self.tbAuftragsdatum, self.calendarWidget)
        Dialog.setTabOrder(self.calendarWidget, self.btnSave)
        Dialog.setTabOrder(self.btnSave, self.twPositionen)
        Dialog.setTabOrder(self.twPositionen, self.twAbzuege)
        Dialog.setTabOrder(self.twAbzuege, self.tabWidget_2)
        Dialog.setTabOrder(self.tabWidget_2, self.pTE_Logger)
        Dialog.setTabOrder(self.pTE_Logger, self.teCurrRechSum)
        Dialog.setTabOrder(self.teCurrRechSum, self.tbRechNummer)
        Dialog.setTabOrder(self.tbRechNummer, self.teCurrRechTax)
        Dialog.setTabOrder(self.teCurrRechTax, self.teCurrRechSumWithTax)
        Dialog.setTabOrder(self.teCurrRechSumWithTax, self.chk_OpenFileAfterCreation)
        Dialog.setTabOrder(self.chk_OpenFileAfterCreation, self.btnResetGUI)
        Dialog.setTabOrder(self.btnResetGUI, self.lE_pathRechnungen_auswert)
        Dialog.setTabOrder(self.lE_pathRechnungen_auswert, self.btnSelDirRechAuswert)
        Dialog.setTabOrder(self.btnSelDirRechAuswert, self.btn_ErstelleAuswertung)
        Dialog.setTabOrder(self.btn_ErstelleAuswertung, self.lE_path2ConfigDir)
        Dialog.setTabOrder(self.lE_path2ConfigDir, self.lE_path2Output_rechnungen)
        Dialog.setTabOrder(self.lE_path2Output_rechnungen, self.btnSelDirConfig)
        Dialog.setTabOrder(self.btnSelDirConfig, self.btnSelDirOutputRech)
        Dialog.setTabOrder(self.btnSelDirOutputRech, self.btnResetRechNumToOne)
        Dialog.setTabOrder(self.btnResetRechNumToOne, self.btnChangeRechNum)
        Dialog.setTabOrder(self.btnChangeRechNum, self.btnOpenPosWithApp)
        Dialog.setTabOrder(self.btnOpenPosWithApp, self.btnOpenAbzWithApp)
        Dialog.setTabOrder(self.btnOpenAbzWithApp, self.chkShowLog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rechnungsprogramm"))
        self.cbClients.setItemText(0, _translate("Dialog", "Femo GmbH"))
        self.label_4.setText(_translate("Dialog", "Leistungsdatum auswählen:"))
        self.label_6.setText(_translate("Dialog", "Auftragsnummer"))
        self.label.setText(_translate("Dialog", "Auftragsort"))
        self.tbAuftragsort.setText(_translate("Dialog", "platzhalter"))
        self.label_2.setText(_translate("Dialog", "Leistungsdatum"))
        self.label_3.setText(_translate("Dialog", "Rechnungsdatum"))
        item = self.twPositionen.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Pos.Nr."))
        item = self.twPositionen.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Position"))
        item = self.twPositionen.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Einheit"))
        item = self.twPositionen.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Preis"))
        item = self.twPositionen.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Menge"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Dialog", "Positionen"))
        item = self.twAbzuege.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.twAbzuege.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Position"))
        item = self.twAbzuege.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Einheit"))
        item = self.twAbzuege.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Preis"))
        item = self.twAbzuege.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Menge"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Dialog", "Abzüge"))
        self.label_5.setText(_translate("Dialog", "Rechnungsnummer"))
        self.btnSave.setText(_translate("Dialog", "Erstelle Rechnung"))
        self.tbAuftragsnummer.setText(_translate("Dialog", "platzhalter"))
        self.lCustomer_street.setText(_translate("Dialog", "Teststraße 0815"))
        self.lCustomer_city.setText(_translate("Dialog", "12345 Testortname"))
        self.teCurrRechSum.setText(_translate("Dialog", "0.00"))
        self.label_9.setText(_translate("Dialog", "Nettosumme"))
        self.lMsgNoRechOutputDir.setText(_translate("Dialog", "Ausgabe-Ordner unter \"Einstellungen\" angegeben."))
        self.chk_OpenFileAfterCreation.setText(_translate("Dialog", "Öffne Datei nach Erstellen"))
        self.btnResetGUI.setText(_translate("Dialog", "Reset"))
        self.chk_AddTaxes.setTitle(_translate("Dialog", "Berechne Ust."))
        self.label_12.setText(_translate("Dialog", "Bruttosumme"))
        self.teCurrRechSumWithTax.setText(_translate("Dialog", "1000.00"))
        self.teCurrRechTax.setText(_translate("Dialog", "1000.00"))
        self.label_14.setText(_translate("Dialog", "Ust.-Betrag"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Rechnung erstellen"))
        self.btnSelDirRechAuswert.setText(_translate("Dialog", "Ordner auswählen"))
        self.label_10.setText(_translate("Dialog", "Pfad zu Ausgabe-Ordner für Rechnungen"))
        self.label_11.setText(_translate("Dialog", "Anzahl Rechnungen:"))
        self.lCnt_FilesForAuswert.setText(_translate("Dialog", "x"))
        self.btn_ErstelleAuswertung.setText(_translate("Dialog", "Erstelle Auswertung"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Rechnungen auswerten"))
        self.label_7.setText(_translate("Dialog", "Pfad zu Config und Templates:"))
        self.lE_path2ConfigDir.setText(_translate("Dialog", "C:\\Users\\PatrickKinateder\\Documents\\PRIVAT\\RePro"))
        self.label_8.setText(_translate("Dialog", "Pfad zu Ausgabe-Ordner für Rechnungen"))
        self.btnSelDirConfig.setText(_translate("Dialog", "Ordner auswählen"))
        self.btnSelDirOutputRech.setText(_translate("Dialog", "Ordner auswählen"))
        self.btnOpenPosWithApp.setText(_translate("Dialog", "Positionen öffnen + ändern"))
        self.btnOpenAbzWithApp.setText(_translate("Dialog", "Abzüge öffnen + ändern"))
        self.groupBox.setTitle(_translate("Dialog", "Folgende Anpassungen werden ohne Bestätigung gespeichert"))
        self.label_13.setText(_translate("Dialog", "Ust.-Satz"))
        self.chkShowLog.setText(_translate("Dialog", "Log anzeigen?"))
        self.groupBox_2.setTitle(_translate("Dialog", "Soll-Dateien im Config-Ordner"))
        self.lFName_PathToRechOutputDir.setText(_translate("Dialog", "PathToRechOutputDir.ini"))
        self.lFName_RechNr.setText(_translate("Dialog", "LastRechNmbr.ini"))
        self.lFName_Positionen.setText(_translate("Dialog", "Positionen.csv"))
        self.lFName_Abzuege.setText(_translate("Dialog", "Abzuege.csv"))
        self.lFName_LastRechYear.setText(_translate("Dialog", "LastRechYear.ini"))
        self.lFName_Template_RechAuswertung.setText(_translate("Dialog", "Template_Auswertung.xlsx"))
        self.lFName_Customer.setText(_translate("Dialog", "Kunden.csv"))
        self.lFName_PathToConfigDir.setText(_translate("Dialog", "PathToConfigDir.ini"))
        self.lFName_UstSatz.setText(_translate("Dialog", "TaxRate.ini"))
        self.lFName_Rechnungsmuster.setText(_translate("Dialog", "Rechnungsmuster_v2.xlsx"))
        self.lFName_ShowLog.setText(_translate("Dialog", "ShowLog.ini"))
        self.groupBox_3.setTitle(_translate("Dialog", "Anpassung der Rech.Nr."))
        self.btnResetRechNumToOne.setText(_translate("Dialog", "Rechnum = 1"))
        self.btnChangeRechNum.setText(_translate("Dialog", "Ändere RechNum"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Einstellungen"))
        self.lLogHeader.setText(_translate("Dialog", "Log:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
