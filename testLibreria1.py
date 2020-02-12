import unittest
from Libreria1 import *

class TestStringMethods(unittest.TestCase):

    def testSuma(self):
        a = (2,3)
        b = (3,1)
        self.assertEqual(Suma (a, b), (5,4))
    def testMultip (self):
        s = (3,-2)
        d = (1,2)
        self.assertEqual(multiplicacion (s, d), (7,4))
    def testResta(self):
        p = (3,-2)
        t = (1,2)
        self.assertEqual(resta (p, t), (2, -4))
    def testConj(self):
        a = (2,3)
        self.assertEqual(conj (a), (2, -3))
    def testDiv(self):
        a = (-2,1)
        b = (1,2)
        self.assertEqual(div (a, b), (0,1))
    def testModulo(self):
        a = (1, -1)
        self.assertEqual(modulo (a), 1.41)
    def testPolar(self):
        a = (1,1)
        self.assertEqual(Polar (a), (1.41,0.79))
    def testFase (self):
        a = (1,1)
        self.assertEqual(Fase (a), 0.79)
    def test_sumaVect(self):
        a = [(1,3),(2,5),(4,2),(3,3)]
        b = [(2,2),(1,12),(5,1),(22,0)]
        self.assertEqual(sumaVect (a, b), [(3, 5), (3, 17), (9, 3), (25, 3)])
    def test_inversaVect(self):
        a = [(4,3),(2,0),(9,2),(6,3)]
        self.assertEqual(inversaVect (a), [(-4, -3), (-2, 0), (-9, -2), (-6, -3)])
    
if __name__ == '__main__':
    unittest.main()
