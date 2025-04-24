from model.mesure import Mesure
from datetime import datetime
from view.view import View
import json, codecs
import time
class Controler:

    def __init__(self, platine):
        self.platine = platine
        self.systeme_actif = False
        self.view = View()
        self.compteur = 0
        self.distance = 0
        self.date_mesure = None
        self.tableau = []

    def demarrer_detecteur(self):
        try:
            self.view.afficher_message("En attente: ")
            print("Appuyer sur le premier bouton pour commencer le processus.")
            while not self.systeme_actif:
                if self.compteur == 0 and self.platine.bouton_demarrer.is_pressed:
                    self.view.clear()
                    self.view.afficher_message("Debut proc...")
                    self.systeme_actif = True
                    self.compteur = 1
                    time.sleep(1)
            print("Les mesures afficheront a chaque 5 secondes. Appuyer sur le deuxieme bouton pour capturer une certaine mesure souhaitee..")
            dernier_temps = time.time()
            while self.systeme_actif:
                temps_courant = time.time()
                if temps_courant - dernier_temps >= 5:
                    self.date_mesure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.distance = self.platine.bouton1_pressed()
                    self.mesure = Mesure(self.date_mesure, self.distance)
                    print(self.mesure.afficherMesure())
                    self.view.afficher_mesure(self.distance, self.date_mesure)
                    dernier_temps = temps_courant

                if self.platine.bouton_demarrer.is_pressed and self.compteur == 1:
                    print("Arret du systeme")
                    self.view.clear()
                    return
                if self.platine.bouton_detecter.is_pressed:
                    print("Capture!")
                    self.view.clear()
                    self.view.afficher_message("Capture!")
                    date_sauvegardee = self.date_mesure
                    mesure_sauvegardee = self.distance
                    capteur = {
                        "Date": date_sauvegardee,
                        "Distance": mesure_sauvegardee
                    }
                    self.tableau.append(capteur)
                    self.SauvegarderJson(self.tableau)
                    time.sleep(0.2)
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.view.clear()
    def SauvegarderJson(self, file):
        try:
            with codecs.open("resultats.json", "w", encoding="utf-8") as jsonFile:
                json.dump(file, jsonFile, ensure_ascii=False, indent=4, sort_keys=True)
        except FileNotFoundError:
            print("File not found")

                  