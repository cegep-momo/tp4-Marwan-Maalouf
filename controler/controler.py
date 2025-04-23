from view.view import View


class Controler:

    def __init__(self, platine):
        self.platine = platine
        self.view = View()
        self.systeme_actif = False
        self.compteur = 0

    def demarrer_detecteur(self):
        self.view.afficher_message("En attente: ")
        print("Appuyer sur le premier bouton pour commencer le processus.")
        while not self.systeme_actif:
            if self.compteur == 0 and self.platine.bouton_demarrer.is_pressed:
                self.platine.bouton1_pressed()
                self.view.clear()
                self.view.afficher_message("Debut proc...")
                self.systeme_actif = True
                self.compteur = 1
        print("Les mesures afficheront a chaque 5 secondes. Appuyer sur le deuxieme bouton pour capturer une certaine mesure souhaitee..")
        while self.systeme_actif:
            self.platine.bouton1_pressed()
            if self.platine.bouton_demarrer.is_pressed and self.compteur == 1:
                return
            if self.platine.bouton_detecter.is_pressed:
                print('test')