import unittest
from Libreria1 import *

class TestStringMethods(unittest.TestCase):

    def test_sumaVect(self):
        a = [(1,3),(2,5),(4,2),(3,3)]
        b = [(2,2),(1,12),(5,1),(22,0)]
        self.assertEqual(sumaVect (a, b), [(3, 5), (3, 17), (9, 3), (25, 3)])
    def test_inversaVect(self):
        a = [(4,3),(2,0),(9,2),(6,3)]
        self.assertEqual(inversaVect (a), [(-4, -3), (-2, 0), (-9, -2), (-6, -3)])
    def test_productoEscalarV(self):
        a = [(3,4),(14,2),(25,10)]
        self.assertEqual(productoEscalarV(a, (1,0)), [(3,4),(14,2),(25,10)])
    def test_sumaMatrix(self):
        a = [[(6,10),(2,0),(2,2)],[(0,1),(10,10),(4,5)],[(8,16),(11,10),(21,0)]]
        b = [[(4,-10),(8,0),(2,4)],[(1,1),(1,1),(-4,-5)],[(0,-8),(0,-10),(0,21)]]
        self.assertEqual(sumaMatrix(a, b), [[(10,0),(10,0),(4,6)],[(1,2),(11,11),(0,0)],[(8,8),(11,0),(21,21)]])
    def test_inversaMatrix(self):
        a = [[(6,10),(2,0),(2,2)],[(0,1),(10,10),(4,5)],[(8,16),(11,10),(21,0)]]
        self.assertEqual(inversaMatrix(a), [[(-6,-10),(-2,0),(-2,-2)],[(0,-1),(-10,-10),(-4,-5)],[(-8,-16),(-11,-10),(-21,0)]])
    def test_multiescalarMatrix(self):
        a = [[(6,10),(2,0),(2,2)],[(0,1),(10,10),(4,5)],[(8,16),(11,10),(21,0)]]
        self.assertEqual(multiEscalarMatrix(a, (-1,0)), [[(-6,-10),(-2,0),(-2,-2)],[(0,-1),(-10,-10),(-4,-5)],[(-8,-16),(-11,-10),(-21,0)]])        
    def test_matrixTrans(self):
        a = [[(1,22),(35,55)],[(7,10),(1,1)]]
        self.assertEqual(matrixTrans(a), [[(1,22),(7,10)],[(35,55),(1,1)]])
    def test_matrixConj(self):
        a = [[(1,22),(35,55)],[(7,10),(1,1)]]
        self.assertEqual(matrixConj(a), [[(1,-22),(35,-55)],[(7,-10),(1,-1)]])
    def test_matrixAdj(self):
        a = [[(1,22),(35,55)],[(7,10),(1,1)]]
        self.assertEqual(matrixAdj(a), [[(1,-22),(7,-10)],[(35,-55),(1,-1)]])
    def test_multiMatrix(self):
        a = [[(1,0)],[(2,2)]]
        b = [[(3,2),(1,0)]]
        self.assertEqual(multiMatrix(b, a), [[(5, 4), (0, 0)]])
    def testAccion(self):
        a = [[(1,0),(3,1)],[(2,2),(1,1)]]
        b = [(1,0),(0,1)]
        self.assertEqual(Accion(a, b), [(0,3),(1,3)])
    def test_ProductIntVec(self):
        a = [(2,1),(3,2),(1,1)]
        b = [(5,6),(4,8),(16,1)]
        self.assertEqual(ProductIntVec(a, b), (61,8))
    def testNorma(self):
        a = [(2,1),(3,2),(1,1)]
        self.assertEqual(norma(a), 4.47)
    def testDistancia(self):
        a = [(2,1),(3,2),(1,1)]
        b = [(5,6),(4,8),(16,1)]
        self.assertEqual(distancia(a,b), 17.2)
    def testUni(self):
        a = [[(2,1),(3,2)],[(1,1),(4,1)]]
        self.assertEqual(Uni(a), False)
    def testHerm(self):
        a = [[(1,0),(3,20)],[(3,-20),(5,0)]]
        self.assertEqual(Herm(a), True)
    def testTensor(self):
        a = [[(0,0),(1,0)],[(1,0),(0,0)]]
        b = [[(4,0),(2,3),(1,1)],[(1,0),(0,1),(1,0)],[(2,2),(3,3),(4,4)]]
        self.assertEqual(Tensor(a,b), [[(0, 0), (0, 0), (0, 0), (4, 0), (2, 3), (1, 1)], [(0, 0), (0, 0), (0, 0), (4, 0), (2, 3), (1, 1)]])

if __name__ == '__main__': 
    unittest.main()
