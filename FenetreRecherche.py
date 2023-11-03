# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fenetre_Recherche.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fenetre_Recherche(object):
    def setupUi(self, Fenetre_Recherche):
        Fenetre_Recherche.setObjectName("Fenetre_Recherche")
        Fenetre_Recherche.resize(1119, 694)
        self.Recherche_Instructions = QtWidgets.QTextBrowser(Fenetre_Recherche)
        self.Recherche_Instructions.setGeometry(QtCore.QRect(10, 40, 721, 231))
        self.Recherche_Instructions.setObjectName("Recherche_Instructions")
        self.Recherche_LogoBlink = QtWidgets.QLabel(Fenetre_Recherche)
        self.Recherche_LogoBlink.setGeometry(QtCore.QRect(770, 40, 341, 231))
        self.Recherche_LogoBlink.setText("")
        self.Recherche_LogoBlink.setPixmap(QtGui.QPixmap("Logo_Blink.jpeg"))
        self.Recherche_LogoBlink.setScaledContents(True)
        self.Recherche_LogoBlink.setObjectName("Recherche_LogoBlink")
        self.Recherche_Btn_ClassementClients = QtWidgets.QPushButton(Fenetre_Recherche)
        self.Recherche_Btn_ClassementClients.setGeometry(QtCore.QRect(400, 540, 321, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Recherche_Btn_ClassementClients.setFont(font)
        self.Recherche_Btn_ClassementClients.setAutoFillBackground(False)
        self.Recherche_Btn_ClassementClients.setDefault(False)
        self.Recherche_Btn_ClassementClients.setFlat(False)
        self.Recherche_Btn_ClassementClients.setObjectName("Recherche_Btn_ClassementClients")
        self.Recherche_Btn_VuesEnsemble = QtWidgets.QPushButton(Fenetre_Recherche)
        self.Recherche_Btn_VuesEnsemble.setGeometry(QtCore.QRect(90, 360, 141, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Recherche_Btn_VuesEnsemble.setFont(font)
        self.Recherche_Btn_VuesEnsemble.setObjectName("Recherche_Btn_VuesEnsemble")
        self.Recherche_Btn_ContratsEnCours = QtWidgets.QPushButton(Fenetre_Recherche)
        self.Recherche_Btn_ContratsEnCours.setGeometry(QtCore.QRect(880, 360, 141, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Recherche_Btn_ContratsEnCours.setFont(font)
        self.Recherche_Btn_ContratsEnCours.setObjectName("Recherche_Btn_ContratsEnCours")
        self.Recherche_Btn_ClientsCH = QtWidgets.QPushButton(Fenetre_Recherche)
        self.Recherche_Btn_ClientsCH.setGeometry(QtCore.QRect(880, 540, 141, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Recherche_Btn_ClientsCH.setFont(font)
        self.Recherche_Btn_ClientsCH.setObjectName("Recherche_Btn_ClientsCH")
        self.Recherche_Btn_ClassementPackages = QtWidgets.QPushButton(Fenetre_Recherche)
        self.Recherche_Btn_ClassementPackages.setGeometry(QtCore.QRect(400, 360, 321, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Recherche_Btn_ClassementPackages.setFont(font)
        self.Recherche_Btn_ClassementPackages.setObjectName("Recherche_Btn_ClassementPackages")
        self.Recherche_Btn_FacturesImpayees = QtWidgets.QPushButton(Fenetre_Recherche)
        self.Recherche_Btn_FacturesImpayees.setGeometry(QtCore.QRect(90, 540, 141, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Recherche_Btn_FacturesImpayees.setFont(font)
        self.Recherche_Btn_FacturesImpayees.setObjectName("Recherche_Btn_FacturesImpayees")

        self.retranslateUi(Fenetre_Recherche)
        QtCore.QMetaObject.connectSlotsByName(Fenetre_Recherche)

    def retranslateUi(self, Fenetre_Recherche):
        _translate = QtCore.QCoreApplication.translate
        Fenetre_Recherche.setWindowTitle(_translate("Fenetre_Recherche", "Form"))
        self.Recherche_Instructions.setHtml(_translate("Fenetre_Recherche", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Bienvenue dans la fenêtre recherche !</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Vous pouvez choisir, parmi les boutons ci-dessous, le type d\'information que vous souhaitez consulter dans la base de données de </span><span style=\" font-size:12pt; font-style:italic;\">Blink Digital Agency </span><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.Recherche_Btn_ClassementClients.setText(_translate("Fenetre_Recherche", "Classement des clients les plus lucratifs"))
        self.Recherche_Btn_VuesEnsemble.setText(_translate("Fenetre_Recherche", "Vues d\'ensemble"))
        self.Recherche_Btn_ContratsEnCours.setText(_translate("Fenetre_Recherche", "Contrats en cours"))
        self.Recherche_Btn_ClientsCH.setText(_translate("Fenetre_Recherche", "Clients en Suisse"))
        self.Recherche_Btn_ClassementPackages.setText(_translate("Fenetre_Recherche", "Classement des packages par prix décroissants"))
        self.Recherche_Btn_FacturesImpayees.setText(_translate("Fenetre_Recherche", "Factures impayées"))