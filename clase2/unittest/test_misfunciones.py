from funciones import calcula_media
import unittest


'''
.assertEqual(a, b): Verifica la igualdad de ambos valores.
.assertTrue(x): Verifica que el valor es True.
.assertFalse(x): Verifica que el valor es False.
.assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
.assertIsNone(x): Verifica que el valor es None.
.assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
.assertIsInstance(a, b): Verifica que a es una instancia de b
.assertRaises(x): Verifica que se lanza una excepción.

'''

class Test_misfunciones(unittest.TestCase):
    
    def setUp(self):
        print("Entrando en setup")
    
    def tearDown(self):
        print("Entrando en setup")
    
    def test_1(self):
        resul = calcula_media([5,5,5])
        self.assertEqual(resul,5)
        
    def test_2(self):
        resul = calcula_media([5,5,5])
        self.assertEqual(resul,15)
    
    def test_3(self):
    
        self.assertIn(1,[11,2])

if __name__ == '__main__':   
    unittest.main()