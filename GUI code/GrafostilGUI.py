# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\_Macuzic\Projekat Grafostil\Python source code\GUI code\ars.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from   PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import arsGrafostilBiblioteka as ars

#GUI CLASS
class Ui_MainWindow(object):
    # Properties
        # IP camera
            # ipAdresaKamere = 'rtsp://admin:password@IP_addrss:port/cam/realmonitor?channel=1@subtype=1'
            # ipAdresaKamere = 'rtsp://admin:password@IP_addrss:port/cam/realmonitor?channel=1@subtype=0' #shape:(2160, 3840, 3)
        # USB camera
            # ipAdresaKamere = 0
    _ipAdressOfIpCameras = [0, 1, 2, 3, 4] # USB cameras id currently, replace them with IP following pattern above
    _Warehouse           = ars.Warehouse(_ipAdressOfIpCameras)

    # Konstruktor za dodavanje pojedinacnih kontrola u GUI -----------------------------------------------------------------------------
    def setupUi(self, MainWindow):
        import ctypes
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        scaleX = screensize[0]/1113
        scaleY = (screensize[1]/660)*0.93 # zbog toolbara
        scaleXY = (scaleX+scaleY)/2 # za Font

        MainWindow.setObjectName("Grafostil")
        MainWindow.resize(scaleX*1113, scaleY*660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # root Tab widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(scaleX*0, scaleY*10, scaleX*311, scaleY*601))
        self.tabWidget.setObjectName("tabWidget")
        self.tabGenerateQR = QtWidgets.QWidget()
        # Tab za generisanje QR koda ----------------------------------------------------------------------------------------------------
        # checkBox koji kontrolise da li treba stampati 1 ili sve tabake u RN
        self.tabGenerateQR.setObjectName("tabGenerateQR")
        self.ckeckBox__GenerateQR_PrintAll = QtWidgets.QCheckBox(self.tabGenerateQR)
        self.ckeckBox__GenerateQR_PrintAll.setGeometry(QtCore.QRect(scaleX*10, scaleY*170, scaleX*160, scaleY*23))
        self.ckeckBox__GenerateQR_PrintAll.setObjectName("ckeckBox__GenerateQR_PrintAll")
        self.ckeckBox__GenerateQR_PrintAll.setText("Print QRs for each tab in the WO.")
        # 
        self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll = QtWidgets.QPushButton(self.tabGenerateQR)
        self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll.setGeometry(QtCore.QRect(scaleX*195, scaleY*170, scaleX*75, scaleY*23))
        self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll.setObjectName("ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll")
        self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll.clicked.connect(self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll_clicked)
        self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll.setSizePolicy
        # 
        self.label = QtWidgets.QLabel(self.tabGenerateQR)
        self.label.setGeometry(QtCore.QRect(scaleX*10, scaleY*30, scaleX*121, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_GenerateQR_IdWorkorder = QtWidgets.QLineEdit(self.tabGenerateQR)
        self.lineEdit_GenerateQR_IdWorkorder.setGeometry(QtCore.QRect(scaleX*140, scaleY*30, scaleX*131, scaleY*31))
        self.lineEdit_GenerateQR_IdWorkorder.setObjectName("lineEdit_GenerateQR_IdWorkorder")
        self.lineEdit_GenerateQR_IdWorkorder.textChanged.connect(lambda: self.allowOnlyNumbers(self.lineEdit_GenerateQR_IdWorkorder.text(), 4))
        self.label_2 = QtWidgets.QLabel(self.tabGenerateQR)
        self.label_2.setGeometry(QtCore.QRect(scaleX*10, scaleY*80, scaleX*121, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_GenerateQR_IdTab = QtWidgets.QLineEdit(self.tabGenerateQR)
        self.lineEdit_GenerateQR_IdTab.setGeometry(QtCore.QRect(scaleX*140, scaleY*80, scaleX*131, scaleY*31))
        self.lineEdit_GenerateQR_IdTab.setObjectName("lineEdit_GenerateQR_IdTab")
        self.lineEdit_GenerateQR_IdTab.textChanged.connect(lambda: self.allowOnlyNumbers(self.lineEdit_GenerateQR_IdTab.text(), 2))
        self.lineEdit_GenerateQR_TotalTabs = QtWidgets.QLineEdit(self.tabGenerateQR)
        self.lineEdit_GenerateQR_TotalTabs.setGeometry(QtCore.QRect(scaleX*140, scaleY*130, scaleX*131, scaleY*31))
        self.lineEdit_GenerateQR_TotalTabs.setObjectName("lineEdit_GenerateQR_TotalTabs")
        self.lineEdit_GenerateQR_TotalTabs.textChanged.connect(lambda: self.allowOnlyNumbers(self.lineEdit_GenerateQR_TotalTabs.text(), 2))
        self.label_8 = QtWidgets.QLabel(self.tabGenerateQR)
        self.label_8.setGeometry(QtCore.QRect(scaleX*10, scaleY*130, scaleX*121, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tabGenerateQR, "")
        # Tab za pregled stanja na skladistu ------------------------------------------------------------------------------------------
        self.tab_WarehouseInventoryView = QtWidgets.QWidget()
        self.tab_WarehouseInventoryView.setObjectName("tab_WarehouseInventoryView")
        self.SearchForParticularTab = QtWidgets.QGroupBox(self.tab_WarehouseInventoryView)
        self.SearchForParticularTab.setGeometry(QtCore.QRect(scaleX*10, scaleY*10, scaleX*281, scaleY*131))
        self.SearchForParticularTab.setObjectName("SearchForParticularTab")
        self.label_3 = QtWidgets.QLabel(self.SearchForParticularTab)
        self.label_3.setGeometry(QtCore.QRect(scaleX*10, scaleY*20, scaleX*121, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_InventoryView_IdWorkOrder = QtWidgets.QLineEdit(self.SearchForParticularTab)
        self.lineEdit_InventoryView_IdWorkOrder.setGeometry(QtCore.QRect(scaleX*140, scaleY*20, scaleX*131, scaleY*31))
        self.lineEdit_InventoryView_IdWorkOrder.setObjectName("lineEdit_InventoryView_IdWorkOrder")
        self.lineEdit_InventoryView_IdWorkOrder.textChanged.connect(lambda: self.allowOnlyNumbers(self.lineEdit_InventoryView_IdWorkOrder.text(), 4))
        self.label_4 = QtWidgets.QLabel(self.SearchForParticularTab)
        self.label_4.setGeometry(QtCore.QRect(scaleX*10, scaleY*60, scaleX*121, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_InventoryView_IdTab = QtWidgets.QLineEdit(self.SearchForParticularTab)
        self.lineEdit_InventoryView_IdTab.setGeometry(QtCore.QRect(scaleX*140, scaleY*60, scaleX*131, scaleXY*31))
        self.lineEdit_InventoryView_IdTab.setObjectName("lineEdit_InventoryView_IdTab")
        self.lineEdit_InventoryView_IdTab.textChanged.connect(lambda: self.allowOnlyNumbers(self.lineEdit_InventoryView_IdTab.text(), 2))
        self.pushButton_InventoryView_FindTab = QtWidgets.QPushButton(self.SearchForParticularTab)
        self.pushButton_InventoryView_FindTab.setGeometry(QtCore.QRect(scaleX*190, scaleY*100, scaleX*75, scaleY*23))
        self.pushButton_InventoryView_FindTab.setObjectName("pushButton_InventoryView_FindTab_clickedEvent")
        self.pushButton_InventoryView_FindTab.clicked.connect(self.pushButton_InventoryView_FindTab_clickedEvent)
        self.listWidget_InventoryView_ListOfDetectedTabs = QtWidgets.QListWidget(self.tab_WarehouseInventoryView)
        self.listWidget_InventoryView_ListOfDetectedTabs.setGeometry(QtCore.QRect(scaleX*10, scaleY*210, scaleX*281, scaleY*321))
        self.listWidget_InventoryView_ListOfDetectedTabs.setObjectName("listWidget_InventoryView_ListOfDetectedTabs")
        self.listWidget_InventoryView_ListOfDetectedTabs.clicked.connect(self.listWidget_InventoryView_ListOfDetectedTabs_cliclkedEvent)
        self.label_5 = QtWidgets.QLabel(self.tab_WarehouseInventoryView)
        self.label_5.setGeometry(QtCore.QRect(scaleX*10, scaleY*170, scaleX*261, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        #
        self.pushButton_InventoryView_RefreshTabList = QtWidgets.QPushButton(self.tab_WarehouseInventoryView)
        self.pushButton_InventoryView_RefreshTabList.setGeometry(QtCore.QRect(scaleX*210, scaleY*540, scaleX*75, scaleY*23))
        self.pushButton_InventoryView_RefreshTabList.setObjectName("pushButton_InventoryView_RefreshTabList")
        self.pushButton_InventoryView_RefreshTabList.clicked.connect(self.pushButton_WarehouseInventory_RefreshData_event)
        #
        self.pushButton_InventoryView_GenerateWordDocx = QtWidgets.QPushButton(self.tab_WarehouseInventoryView)
        self.pushButton_InventoryView_GenerateWordDocx.setGeometry(QtCore.QRect(scaleX*10, scaleY*540, scaleX*80, scaleY*23))
        self.pushButton_InventoryView_GenerateWordDocx.setObjectName("pushButton_InventoryView_GenerateWordDocx")
        self.pushButton_InventoryView_GenerateWordDocx.clicked.connect(self.pushButton_InventoryView_GenerateWordDocx_Event)
        self.tabWidget.addTab(self.tab_WarehouseInventoryView, "")
        # Tab za inspekciju RN --------------------------------------------------------------------------------------------------------
        self.tab_InspectionOfWorkOrder = QtWidgets.QWidget()
        self.tab_InspectionOfWorkOrder.setObjectName("tab_InspectionOfWorkOrder")
        self.groupBox_InspectionOfWorkOrder = QtWidgets.QGroupBox(self.tab_InspectionOfWorkOrder)
        self.groupBox_InspectionOfWorkOrder.setGeometry(QtCore.QRect(scaleX*10, scaleY*20, scaleX*281, scaleY*541))
        self.groupBox_InspectionOfWorkOrder.setObjectName("groupBox_InspectionOfWorkOrder")
        self.label_10 = QtWidgets.QLabel(self.groupBox_InspectionOfWorkOrder)
        self.label_10.setGeometry(QtCore.QRect(scaleX*10, scaleY*20, scaleX*166, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_InspectionOfWorkOrder_IdWorkOrder = QtWidgets.QLineEdit(self.groupBox_InspectionOfWorkOrder)
        self.lineEdit_InspectionOfWorkOrder_IdWorkOrder.setGeometry(QtCore.QRect(scaleX*140, scaleY*20, scaleX*131, scaleY*31))
        self.lineEdit_InspectionOfWorkOrder_IdWorkOrder.setObjectName("lineEdit_InspectionOfWorkOrder_IdWorkOrder") # (Radni nalog...: INPUT)
        self.lineEdit_InspectionOfWorkOrder_IdWorkOrder.textChanged.connect(lambda: self.allowOnlyNumbers(self.lineEdit_InspectionOfWorkOrder_IdWorkOrder.text(), 4))
        
        # Button za pretragu
        # stampanje u wordu
        self.pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx = QtWidgets.QPushButton(self.groupBox_InspectionOfWorkOrder)
        self.pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx.setGeometry(QtCore.QRect(scaleX*11, scaleY*60, scaleX*82, scaleY*23))
        self.pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx.setObjectName("pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx")
        # btn provera RN
        self.pushButton_InspectionOfWorkOrder_CheckWorkOrder = QtWidgets.QPushButton(self.groupBox_InspectionOfWorkOrder)
        self.pushButton_InspectionOfWorkOrder_CheckWorkOrder.setGeometry(QtCore.QRect(scaleX*190, scaleY*60, scaleX*75, scaleY*23))
        self.pushButton_InspectionOfWorkOrder_CheckWorkOrder.setObjectName("pushButton_InspectionOfWorkOrder_CheckWorkOrder_")
        self.tabWidget.addTab(self.tab_InspectionOfWorkOrder, "")
        # Lista RN 
        self.label_9 = QtWidgets.QLabel(self.groupBox_InspectionOfWorkOrder)
        self.label_9.setGeometry(QtCore.QRect(scaleX*10, scaleY*85, scaleX*261, scaleY*31))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        # Lista
        self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders = QtWidgets.QListWidget(self.groupBox_InspectionOfWorkOrder)
        self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders.setGeometry(QtCore.QRect(scaleX*5, scaleY*115, scaleX*270, scaleY*210))
        self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders.setObjectName("listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders")
        self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders.clicked.connect(self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders_cliclkedEvent)
        # Lista tabaka u RN 
        # txt lable
        self.label_11 = QtWidgets.QLabel(self.groupBox_InspectionOfWorkOrder)
        self.label_11.setGeometry(QtCore.QRect(scaleX*10, scaleY*333, scaleX*263, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11") # tabaci u selektovanom RN
        #  Lista
        self.listWidget_InventoryView_ListOfDetectedTabsWO = QtWidgets.QListWidget(self.groupBox_InspectionOfWorkOrder)
        self.listWidget_InventoryView_ListOfDetectedTabsWO.setGeometry(QtCore.QRect(scaleX*5, scaleY*363, scaleX*10270, scaleY*170))
        self.listWidget_InventoryView_ListOfDetectedTabsWO.setObjectName("listWidget_InventoryView_ListOfDetectedTabsWO")
        self.listWidget_InventoryView_ListOfDetectedTabsWO.clicked.connect(self.listWidget_InventoryView_ListOfDetectedTabsWO_cliclkedEvent)
     
 # Desna strana GUI-a. Ima dva widget-a: 1) widgetPanorama 2) widgetCurrentCamera
        self.toolBox_CameraView = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox_CameraView.setGeometry(QtCore.QRect(scaleX*320, scaleY*10, scaleX*781, scaleY*603))
        self.toolBox_CameraView.setObjectName("toolBox_CameraView")
    # widgetPanorama - sadrzi samo sliku panorame
        self.widgetPanorama = QtWidgets.QWidget()
        self.widgetPanorama.setGeometry(QtCore.QRect(scaleX*0, scaleY*0, scaleX*781, scaleY*547))
        self.widgetPanorama.setObjectName("widgetPanorama")
        self.pyplot_Panorama = ars.PlotCanvas(self.widgetPanorama, width=scaleX*7.81, height=scaleY*5.51)
        self.pyplot_Panorama.setObjectName("pyplot_Panorama")
        self.toolBox_CameraView.addItem(self.widgetPanorama, "")
        self.toolBox_CameraView.setCurrentIndex(1)
    # widgetCurrentCamera - sadrzi sliku sa leve strane, i dva listWidget-a sa desne strane
        self.widgetCurrentCamera = QtWidgets.QWidget()
        self.widgetCurrentCamera.setGeometry(QtCore.QRect(scaleX*0, scaleY*0, scaleX*781, scaleY*547))
        self.widgetCurrentCamera.setObjectName("widgetCurrentCamera")
        self.listWidget_CameraView_ListaOfAvailableCameras = QtWidgets.QListWidget(self.widgetCurrentCamera)
        self.listWidget_CameraView_ListaOfAvailableCameras.setGeometry(QtCore.QRect(scaleX*580, scaleY*50, scaleX*201, scaleY*161))
        self.listWidget_CameraView_ListaOfAvailableCameras.setObjectName("listWidget_CameraView_ListaOfAvailableCameras")
        self.listWidget_CameraView_ListaOfAvailableCameras.currentItemChanged.connect(self.listWidget_CameraView_ListaOfAvailableCamerasEvent)
        self.label_6 = QtWidgets.QLabel(self.widgetCurrentCamera)
        self.label_6.setGeometry(QtCore.QRect(scaleX*580, scaleY*20, scaleX*211, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.listWidget_CameraView_ListaOfTabsVisibleOnCamera = QtWidgets.QListWidget(self.widgetCurrentCamera)
        self.listWidget_CameraView_ListaOfTabsVisibleOnCamera.setGeometry(QtCore.QRect(scaleX*580, scaleY*290, scaleX*201, scaleY*251))
        self.listWidget_CameraView_ListaOfTabsVisibleOnCamera.setObjectName("listWidget_CameraView_ListaOfTabsVisibleOnCamera")
        self.listWidget_CameraView_ListaOfTabsVisibleOnCamera.clicked.connect(self.listWidget_CameraView_ListaOfTabsVisibleOnCamera_cickedEvent)
        self.label_7 = QtWidgets.QLabel(self.widgetCurrentCamera)
        self.label_7.setGeometry(QtCore.QRect(scaleX*580, scaleY*260, scaleX*211, scaleY*31))
        font = QtGui.QFont()
        font.setPointSize(scaleXY*12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pyplot_Camera = ars.PlotCanvas(self.widgetCurrentCamera, width=scaleX*5.71, height=scaleY*5.41)
        self.pyplot_Camera.setObjectName("pyplot_Camera")
        self.toolBox_CameraView.addItem(self.widgetCurrentCamera, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.toolBox_CameraView.setCurrentIndex(0)        
        self.toolBox_CameraView.currentChanged['int'].connect(self.toolBox_CameraView.setCurrentIndex)
        self.listWidget_CameraView_ListaOfAvailableCameras.pressed['QModelIndex'].connect(self.listWidget_CameraView_ListaOfAvailableCameras.update)
        self.pushButton_InspectionOfWorkOrder_CheckWorkOrder.clicked.connect(self.pushButton_InspectionOfWorkOrder_CheckWorkOrder_clickEvent)
        self.pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx.clicked.connect(self.pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx_clickEvent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll.setText(_translate("MainWindow", "Print"))
        self.label.setText(_translate("MainWindow", "Work order......:"))
        self.label_2.setText(_translate("MainWindow", "Tab..............:"))
        self.label_8.setText(_translate("MainWindow", "Total tabs.:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGenerateQR), _translate("MainWindow", "Generate QR"))
        self.SearchForParticularTab.setTitle(_translate("MainWindow", "Search for particular Tab"))
        self.label_3.setText(_translate("MainWindow", "Work order....:"))
        self.label_4.setText(_translate("MainWindow", "Tab...............:"))
        self.pushButton_InventoryView_FindTab.setText(_translate("MainWindow", "Search"))
        self.label_5.setText(_translate("MainWindow", "List of detected tabs............:"))
        self.pushButton_InventoryView_RefreshTabList.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_InventoryView_GenerateWordDocx.setText(_translate("MainWindow", "Print MS Word"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_WarehouseInventoryView), _translate("MainWindow", "Inspection of tabs"))
        self.groupBox_InspectionOfWorkOrder.setTitle(_translate("MainWindow", "Detection of tabs"))
        self.label_10.setText(_translate("MainWindow", "Work order.....:"))
        self.label_11.setText(_translate("MainWindow", "List of tabs in the selected work order......:"))
        self.pushButton_InspectionOfWorkOrder_CheckWorkOrder.setText(_translate("MainWindow", "Inspect"))
        self.pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx.setText(_translate("MainWindow", "Print MS Word"))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_InspectionOfWorkOrder), _translate("MainWindow", "Print MS Word"))
        self.toolBox_CameraView.setItemText(self.toolBox_CameraView.indexOf(self.widgetPanorama), _translate("MainWindow", "Inpsection of Work order"))
        self.label_6.setText(_translate("MainWindow", "Available cameras..............:"))
        self.label_7.setText(_translate("MainWindow", "Detected tabs ............:"))
        self.toolBox_CameraView.setItemText(self.toolBox_CameraView.indexOf(self.widgetCurrentCamera), _translate("MainWindow", "View from specific IP camera"))
        self.label_9.setText(_translate("MainWindow", "List of detected RN......................:"))
        self.refresh_listWidget_CameraView_ListaOfAvailableCameras()

    # Functions restrict inputs to numeric numbers only (non numeric keyboard inputs are instantly removed)
    # INPUTS
        #self - Ui_MainWindow
        #text - current text in a line box
    def allowOnlyNumbers(self, text, maxNumbers=1):
        text = ''.join(c for c in text if c.isdigit()) 
        if len(text)>maxNumbers:
            text = text[0:maxNumbers]
        txtBoxSender = MainWindow.sender()
        txtBoxSender.setText(text)

    # Func is called by clicking on the ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll button
    # Func prits QR code with respect to data entered into : 1) lineEdit_GenerateQR_IdTab and 2) lineEdit_GenerateQR_TotalTabs
    # this is done by calling the func arsGrafostilBiblioteka.generateQR
    # func checsk validity of QR code - and prevents printing of incorrect or unavailable tab/qr
    # INPUTS (inputs are structures)
        # IdWorkOrder - self.lineEdit_GenerateQR_IdWorkorder
        # IdTa        - self.lineEdit_GenerateQR_IdTab
        # TotalTabs   - self.lineEdit_GenerateQR_TotalTabs
    def ckeckBox__GenepushButton_GenerisateQR_PrintQRrateQR_PrintAll_clicked(self, MainWindow):
        #sprecavanje errora
        if self.lineEdit_GenerateQR_IdWorkorder.text() == '' or self.lineEdit_GenerateQR_IdTab.text() == '' or self.lineEdit_GenerateQR_TotalTabs.text() == '':
            self.statusbar.clearMessage()
            self.statusbar.showMessage('Niste uneli ID radnog naloga, ID tabaka i ukupan br tabaka?')
            return
        #textForGenerationOfQR= "id radnog naloga", "id tabaka" / "ukupno tabaka u radnom nalogu"
        IdWorkOrder    = int(self.lineEdit_GenerateQR_IdWorkorder.text())
        IdTab           = int(self.lineEdit_GenerateQR_IdTab.text())
        TotalTabs      = int(self.lineEdit_GenerateQR_TotalTabs.text())
        # If IdTa> TotalTabs user made a mistake - prevent further execution 
        if IdTab > TotalTabs:
            self.statusbar.clearMessage()
            self.statusbar.showMessage('ID of Tab must be lower than total number of tabs in Work order!!!')
            return            
        # If user wants to print QR codes for all tabs in Work order   
        IdTabs = [IdTab] 
        if self.ckeckBox__GenerateQR_PrintAll.checkState():
            IdTabs = []
            for i in range(1,TotalTabs+1):
                IdTabs.append(i)
        # Printing of QRs
        for IdTab in IdTabs:    
            debugMode = False
            textForGenerationOfQR = '{:04d},{:02d}/{:02d}'.format(IdWorkOrder, IdTab, TotalTabs)
            # Check if the tab already exists in the Warehouse
            postojiNePostoji, tab = self._Warehouse.checkIfThereIsAlreadySuchQrCodeOnInventory(textForGenerationOfQR)
            if postojiNePostoji or IdTab>TotalTabs:
                msg = Qt.QMessageBox() 
                msg.setIcon(Qt.QMessageBox.Warning)
                msg.setText("There is some conflict!")
                msg.setInformativeText("QR code :" + textForGenerationOfQR + " is not valid.")
                msg.setWindowTitle("Printing of QR code")
                msg.setDetailedText("Can errors occur if the tab ID is greater than the total number of tabs? Or if there is already such a KR code in storage?")
                msg.setStandardButtons(Qt.QMessageBox.Ok | Qt.QMessageBox.Cancel)
                retval = msg.exec_()
                continue
            # stampaj QR kod
            imgQR = ars.generateQR(textForGenerationOfQR, debugMode)
            ars.printQqCodeOnWinPrinter(imgQR, debugMode)
            self.statusbar.clearMessage()
            self.statusbar.showMessage('QR code: ' + textForGenerationOfQR  + ' is printed.')

    # Write strings into QListWidget
    # Step 1 - Take list of available cameras
    # Step 2 - Write list into listWidget_CameraView_ListaOfAvailableCameras
    def refresh_listWidget_CameraView_ListaOfAvailableCameras(self):
        images, availableCameras = self._Warehouse.getImagesFromIpCameras()
        self.listWidget_CameraView_ListaOfAvailableCameras.addItems(availableCameras)
    
    # Fcn is called as an event - when one select IP camera in the list of available cameras 
    # it reads images from a camera; reads QR , draw images and QR on the views and writes findigns into corresponding listboxes
    def listWidget_CameraView_ListaOfAvailableCamerasEvent(self):
        id          = self.listWidget_CameraView_ListaOfAvailableCameras.currentRow()
        img         = self._Warehouse.ipCameras[id].img
        qrData      = self._Warehouse.ipCameras[id].qrData
        qrLocations = self._Warehouse.ipCameras[id].qrLocations
        self.pyplot_Camera.drawImage([img], qrLocations, qrData)
        self.listWidgetFcn_FillWithData(self.listWidget_CameraView_ListaOfTabsVisibleOnCamera, qrData, True, [])
        self.statusbar.showMessage('Image cames from IP camera: ' + self._Warehouse.ipCameras[id].status)

    # Fcn refreshes data acquisition from cameras
    #1 - Collect camera images
    #2 - Process each image separately
    #3 - Panorama - Find the homography matrices of individual panorama cameras
    #4 - Show results
    def pushButton_WarehouseInventory_RefreshData_event(self):
        self.statusbar.showMessage('Panorama generation....in progress.') 
        # refresh warehouse structures / data
        self._Warehouse.refreshDataFromIpCameras()
        # refresh the panorama image
        if self._Warehouse.panorama != []:
            self.pyplot_Panorama.drawImage(self._Warehouse.panorama, qrLocations, qrData)
        # refresh the list of found tabs
        qrData, qrDataIsValid = self._Warehouse.getStringListuQrData()
        self.listWidgetFcn_FillWithData(self.listWidget_InventoryView_ListOfDetectedTabs, qrData, qrDataIsValid, [])
        self.statusbar.showMessage('Panorama is shown')
        # refresh the list of found work orders
        stringListOfWorkOrders, boolListaRN_validnostRN, boolListaRN_kompletnostRN = self._Warehouse.getStringListOfWorkOrders()
        self.listWidgetFcn_FillWithData(self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders, stringListOfWorkOrders, boolListaRN_validnostRN, boolListaRN_kompletnostRN)
        self.listWidget_InventoryView_ListOfDetectedTabsWO.clear()

    # Fcn is invoked when someone in the Tab Inspection tab clicks a list of found tabs
    #INPUTS (uzimaju se iz struktura)
        # current Tab
    #OUTPUTS
        # ACTIONS
            # in the tab of WO inspection the camera ID and QR code ID are selected
            # selected QR/tab is focused
    def listWidget_InventoryView_ListOfDetectedTabs_cliclkedEvent(self):
        id = self.listWidget_InventoryView_ListOfDetectedTabs.currentRow() # id reda u UI kontroli
        currentTab = self._Warehouse.detectedTabs[id]                      # trenutni tab sadrzi ID kamere i svoj ID QR koda na toj kameri
        self.listWidget_CameraView_ListaOfAvailableCameras.setCurrentRow(currentTab.qrCamera) 
        self.listWidget_CameraView_ListaOfTabsVisibleOnCamera.setCurrentRow(currentTab.idQrCode)
        self.listWidget_CameraView_ListaOfTabsVisibleOnCamera_cickedEvent()

    # Fcnja draws an image from a specific camera that the user has selected
    # INPUTS (structures/classes)
        # tab id 
        # camera id
        # img
        # qrLocations i qrData to be drawn over image 
    #ACTIONS
        # draws data over image
    def listWidget_CameraView_ListaOfTabsVisibleOnCamera_cickedEvent(self):
        IdTab       = self.listWidget_CameraView_ListaOfTabsVisibleOnCamera.currentRow()
        idCamera    = self.listWidget_CameraView_ListaOfAvailableCameras.currentRow()
        img         = self._Warehouse.ipCameras[idCamera].img
        qrLocations = self._Warehouse.ipCameras[idCamera].qrLocations[IdTab]
        qrData      = self._Warehouse.ipCameras[idCamera].qrData[IdTab]
        self.pyplot_Camera.drawImage([img], [qrLocations], [qrData])

    def pushButton_InventoryView_FindTab_clickedEvent(self):
        IdWorkOrder = self.lineEdit_InventoryView_IdWorkOrder.text()
        IdTa       = self.lineEdit_InventoryView_IdTab.text()
        # if some field is empty - prevent error
        if IdTa == '' or IdWorkOrder == '':
            self.statusbar.clearMessage()
            self.statusbar.showMessage('Niste uneli ID radnog naloga i ID tabaka? ')
            return
        # if the search list is empty
        if self._Warehouse.detectedTabs == []:
            self.statusbar.clearMessage()
            self.statusbar.showMessage('Lista pronađenih tabaka je prazna. Kliknite na dugme Osveži?')
            return
        for i, tab in enumerate(self._Warehouse.detectedTabs):
            if int(IdWorkOrder) == int(tab.qrData[0:4]) and int(IdTa) == int(tab.qrData[5:7]):
                self.listWidget_InventoryView_ListOfDetectedTabs.setCurrentRow(i)
                self.listWidget_InventoryView_ListOfDetectedTabs_cliclkedEvent()             
                self.listWidget_CameraView_ListaOfTabsVisibleOnCamera_cickedEvent()
                self.statusbar.clearMessage()
                self.statusbar.showMessage('Detected Tab: ' + tab.qrData)  
                return
        self.statusbar.clearMessage()
        self.statusbar.showMessage('Tab is not detected.') 
    
    # Check if the Work order is complete
    def pushButton_InspectionOfWorkOrder_CheckWorkOrder_clickEvent(self):
        IdWorkOrder = self.lineEdit_InspectionOfWorkOrder_IdWorkOrder.text()
        self.statusbar.clearMessage()
        if IdWorkOrder == '':
            self.statusbar.showMessage('Work order ID is missing? ')
            return
        if self._Warehouse.detectedTabs == []:            
            self.statusbar.showMessage('The list of found tabs is empty. Click Refresh?')
            return
        for idRN, RN in zip(range(len(self._Warehouse.workOrders)), self._Warehouse.workOrders):
            if RN.IdWorkOrder == int(IdWorkOrder):
                self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders.setCurrentRow(idRN)
                self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders_cliclkedEvent()
                self.statusbar.showMessage('Work order: ' + '{:04d}'.format(int(IdWorkOrder)) + ' is found.')
                return
        self.statusbar.showMessage('Work order is not found: ' + '{:04d}'.format(int(IdWorkOrder)) + '.')
        self.listWidget_InventoryView_ListOfDetectedTabsWO.clear()
    
    # Fnc generate DOCX 
    def pushButton_InspectionOfWorkOrder_CheckWO_GenerateWordDocx_clickEvent(self):
        IdWorkOrder = self.lineEdit_InspectionOfWorkOrder_IdWorkOrder.text()
        if IdWorkOrder == '':
            self.statusbar.showMessage('Work order ID is missing? ')
            return
        if self._Warehouse.detectedTabs == []:            
            self.statusbar.showMessage('List of detected tabs is empty. Click Refresh?')
            return
        for RN in self._Warehouse.workOrders:
            if RN.IdWorkOrder == int(IdWorkOrder):
                self.statusbar.showMessage('Work order: ' + '{:04d}'.format(int(IdWorkOrder)) + ' is found.')
                RN.PrintMsWordReport()
                return
        self.statusbar.showMessage('Work order: ' + '{:04d}'.format(int(IdWorkOrder)) + ' is found.')

    def listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders_cliclkedEvent(self):
        idWO       = self.listWidget_InspectionOfWorkOrder_ListOfDetectedWorkOrders.currentRow()
        workOrder  = self._Warehouse.workOrders[idWO]
        stringListOfTabsWO, stringListOfTabsValidity, _ = workOrder.getListuTabakaKaoString()
        self.listWidgetFcn_FillWithData(self.listWidget_InventoryView_ListOfDetectedTabsWO, stringListOfTabsWO, stringListOfTabsValidity)
        
    # Fja 
    def listWidgetFcn_FillWithData(self, listWidget, qrData, qrDataValidity=[], qrDataCompletness=[]):
        listWidget.clear()
        if qrData != []:
            if qrDataValidity == True: # automatic (qrDataValidity and  qrDataCompletness have  default values obtained from the qrData)
                qrDataValidity =[]
                tab = ars.QrTabak()
                for qrData in qrData:
                    tab.qrData = qrData # pom obj
                    qrDataValidity.append(tab.checkQrDataFormat(qrData))
            if qrDataCompletness == []:
                qrDataCompletness = qrDataValidity
            for qrData, qrDataValidnost, qrDataKompletnost in zip(qrData, qrDataValidity, qrDataCompletness):
                # lista boja
                       #      validan i kompletan    GREEN      validan i nekompletan  YELLOW         nevalidan i kompletan  DARKRED     nevalidan i nekompletan  RED  
                boje = dict([ ('TrueTrue', Qt.QColor(0,255,0)), ('TrueFalse', Qt.QColor(255,255,51)), ('FalseTrue', Qt.QColor(123,0,0)), ('FalseFalse', Qt.QColor(255,0,0)) ])
                item = QtWidgets.QListWidgetItem(qrData)
                if qrDataValidity != []:                 # ako qrDataValidity nije posledjen znaci da boja treba biti bela  
                    bojaPozadine = boje[str(qrDataValidnost)+str(qrDataKompletnost)]            
                    item.setBackground(bojaPozadine)
                listWidget.addItem(item)   

    def listWidget_InventoryView_ListOfDetectedTabsWO_cliclkedEvent(self):
        qrCode = self.listWidget_InventoryView_ListOfDetectedTabsWO.currentItem().text()
        detectedTabak, CurrentTab = self._Warehouse.checkIfThereIsAlreadySuchQrCodeOnInventory(qrCode)
        if detectedTabak:
            self.listWidget_CameraView_ListaOfAvailableCameras.setCurrentRow(CurrentTab.qrCamera) 
            self.listWidget_CameraView_ListaOfTabsVisibleOnCamera.setCurrentRow(CurrentTab.idQrCode)
            self.listWidget_CameraView_ListaOfTabsVisibleOnCamera_cickedEvent()
    
    def pushButton_InventoryView_GenerateWordDocx_Event(self):
        self._Warehouse.PrintMsWordReport()
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())