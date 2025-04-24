
from gpiozero import Button, DistanceSensor

class Platine:

    compteur = 0
    def __init__(self, bouton_demarrer, bouton_detecter, mouv_echo, mouv_trigger):
        self.bouton_demarrer = Button(bouton_demarrer)
        self.bouton_detecter= Button(bouton_detecter)
        self.capteur = DistanceSensor(echo=mouv_echo, trigger=mouv_trigger, max_distance=2)
    #mesurer
    def capture(self):
        distance = round(self.capteur.distance * 100, 2)
    #bouton demarrer
    def bouton1_pressed(self):
        distance = self.capture()
        return distance
    #bouton detecter
    def bouton2_pressed(self):
        self.capture()




