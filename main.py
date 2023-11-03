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

class Gestion_BD:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """ Crée une connexion à une base de données SQLite """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
        return None

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()

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