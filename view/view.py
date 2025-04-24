from LCD1602 import CharLCD1602
from model.mesure import Mesure

class View:
    #initialisation
    def __init__(self):
        self.lcd = CharLCD1602()
        self.lcd.init_lcd(0x27, 1)
        self.clear()
    #afficher un message
    def afficher_message(self, message):
        self.lcd.clear()
        self.lcd.write(0, 0, message)
    #afficher la mesure
    def afficher_mesure(self, mesure, date):
        self.lcd.clear()
        self.lcd.write(0, 0, date)
        self.lcd.write(0, 1, f"Mesure:{mesure}")
    #nettoyer le LCD
    def clear(self):
        self.lcd.clear()
    
