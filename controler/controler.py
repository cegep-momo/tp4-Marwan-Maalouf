from model.mesure import Mesure
from datetime import datetime
from view.view import View
import json, codecs
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
        self.view.afficher_message("En attente: ")
        print("Appuyer sur le premier bouton pour commencer le processus.")
        while not self.systeme_actif:
            if self.compteur == 0 and self.platine.bouton_demarrer.is_pressed:
                self.view.clear()
                self.view.afficher_message("Debut proc...")
                self.systeme_actif = True
                self.compteur = 1
        print("Les mesures afficheront a chaque 5 secondes. Appuyer sur le deuxieme bouton pour capturer une certaine mesure souhaitee..")
        while self.systeme_actif:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            distance = self.platine.bouton1_pressed()
            self.mesure = Mesure(date, distance)
            print(self.mesure.afficherMesure())
            self.view.afficher_mesure(distance, date)
            if self.platine.bouton_demarrer.is_pressed and self.compteur == 1:
                self.view.clear()
                return
            if self.platine.bouton_detecter.is_pressed:
                date_sauvegardee = date
                mesure_sauvegardee = distance
                capteur = {
                    "Date": date_sauvegardee,
                    "Distance": mesure_sauvegardee
                }
                self.tableau.append(capteur)
                self.SauvegarderJson(self.tableau)

    def SauvegarderJson(self, file):
        try:
            with codecs.open("resultats.json", "w", encoding="utf-8") as jsonFile:
                json.dump(file, jsonFile, ensure_ascii=False, indent=4, sort_keys=True)
        except FileNotFoundError:
            print("File not found")      