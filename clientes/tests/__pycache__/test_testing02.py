import unittest
from math import pi

# Código original que vamos a probar
def area(r):
    areaC = pi*(r**2)
    return areaC

class TestAreaCirculo(unittest.TestCase):
    def test_area_positivos(self):
        # Arrange (Preparar)
        radio = 1
        resultado_esperado = pi * (radio**2)
        
        # Act (Actuar)
        resultado = area(radio)
        
        # Assert (Afirmar)
        self.assertEqual(resultado, resultado_esperado)
    
    def test_area_cero(self):
        self.assertEqual(area(0), 0)
    
    def test_area_negativos(self):
        # Debería manejar números negativos
        with self.assertRaises(ValueError):
            area(-1)
    
    def test_area_tipos_invalidos(self):
        # Debería manejar tipos no numéricos
        with self.assertRaises(TypeError):
            area("Hola")
        with self.assertRaises(TypeError):
            area(True)

if __name__ == '__main__':
    unittest.main()