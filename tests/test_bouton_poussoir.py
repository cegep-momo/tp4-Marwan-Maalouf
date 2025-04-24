import unittest
from unittest.mock import MagicMock
from model.platine import Platine

class Tester(unittest.TestCase):
    def setUp(self):
        #broche GPIO 20 pour tester
        self.platine = Platine(bouton_demarrer=20, bouton_detecter=21, mouv_echo=23, mouv_trigger=17)
        # Remplacement des vrais boutons par des mocks
        self.platine.bouton_detecter = MagicMock()

    def test_bouton_detecter_pressed(self):
        # Simuler que le bouton de capture est presse
        self.platine.bouton_detecter.is_pressed = True

        # Capture doit retourner une valeur float
        result = self.platine.capture()
        self.assertIsInstance(result, float)
    
    if __name__ == '__main__':
        unittest.main()
