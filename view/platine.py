import LCD1602
from gpiozero import Button, DistanceSensor
import threading

class Platine:

    compteur = 0
    def __init__(self, bouton_demarrer, bouton_detecter, mouv_echo, mouv_trigger):
        self.bouton1 = Button(bouton_demarrer)
        self.bouton2 = Button(bouton_detecter)
        self.capteur = DistanceSensor(echo=mouv_echo, trigger=mouv_trigger, max_distance=2)

    def start_measuring(self, compte):
        pass
    def capture(self):
        pass
    def destroy(self):
        LCD1602.lcd1602.clear()

    def afficher_message(self, text):
        LCD1602.lcd1602.write(0, 0, f"Distance: {text}")

    def bouton1_pressed(self):
        self.start_measuring(self.compteur)
        self.compteur += 1

    def bouton2_pressed(self):
        self.capture()
