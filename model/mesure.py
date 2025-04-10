

class Mesure:

    def __init__(self, dateHeureMesure, dataMesure):
        self.dataMesure = dataMesure
        self.dateHeureMesure = dateHeureMesure

    def __repr__(self):
        return f"Mesure(dateHeureMesure={self.dateHeureMesure}, dataMesure={self.dataMesure})"
    def afficherMesure(self):
        return f"Date et heure de la mesure: {self.dateHeureMesure} \nDistance: {self.dataMesure}"