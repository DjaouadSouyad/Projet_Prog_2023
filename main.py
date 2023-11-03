import typing
from PyQt5 import QtCore, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
import sys
import sqlite3
from sqlite3 import Error
from FenetreAccueil import Ui_Page_Accueil
from PyQt5.uic import loadUi
# Importez les fenêtres dont vous avez besoin ici
from FenetreRecherche import Ui_Fenetre_Recherche
from FenetreAjout import Ui_Fenetre_Ajout
from FenetreSupprimer import Ui_Fenetre_Supprimer
from projet_db_blink import Gestion_BD


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    Page_Accueil = QtWidgets.QMainWindow()
    ui = Ui_Page_Accueil()
    ui.setupUi(Page_Accueil)
    Page_Accueil.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    database_handler = Gestion_BD(r"bd_projet_def.sqlite")
    run_app()