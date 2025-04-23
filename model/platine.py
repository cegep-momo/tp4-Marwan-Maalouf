
from gpiozero import Button, DistanceSensor
from time import sleep

class Platine:

    compteur = 0
    def __init__(self, bouton_demarrer, bouton_detecter, mouv_echo, mouv_trigger):
        self.bouton_demarrer = Button(bouton_demarrer)
        self.bouton_detecter= Button(bouton_detecter)
        self.capteur = DistanceSensor(echo=mouv_echo, trigger=mouv_trigger, max_distance=2)

    def start_measuring(self):
            distance = round(self.capteur.distance * 100, 2)
            print(distance)
            sleep(5)
    def capture(self):
        distance = round(self.capteur.distance * 100, 2)
        return distance

    def bouton1_pressed(self):
        self.start_measuring()

    def bouton2_pressed(self):
        self.capture()




