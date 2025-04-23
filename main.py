from controler.controler import Controler
from model.platine import Platine
from view.view import View

class Main:
    if __name__ == "__main__":
        demarrer = 20
        catch = 21
        trigger = 17
        echo = 23
        platine = Platine(demarrer, catch, echo, trigger)
        app = Controler(platine)
        lcd = View()
        app.demarrer_detecteur()
        