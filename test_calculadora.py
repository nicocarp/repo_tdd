import unittest
import calculadora

class TestsCalculadora(unittest.TestCase):
	def setUp(self):
		self.calc = calculadora.Calculadora()
	
	def tearDown(self):
		pass

	def test_suma_2_y2(self):
		self.failUnlessEqual(4, self.calc.sumar(2,2))

	def test_suma_5_y_4(self):
		self.failUnlessEqual(9, self.calc.sumar(5,4))

	def test_suma_prop_conmutativa(self):
		self.failUnlessEqual(self.calc.sumar(5, 3), self.calc.sumar(3, 5))

	def test_resta_5_y_3(self):
		self.failUnlessEqual(self.calc.restar(5, 3), 2)

	def test_resta_3_y_5(self):
		self.failUnlessEqual(-2, self.calc.restar(3, 5))

	def test_resta_no_conmutativa(self):
		self.failIfEqual(self.calc.restar(5, 3), self.calc.restar(3, 5))

	def test_suma_negativos_5_y_2(self):
		self.failUnlessEqual(3, self.calc.sumar(5, -2))

	def test_resta_negativos(self):
		self.failUnlessEqual(-5, self.calc.restar(-7, -2))

	def test_division(self):
		self.failUnlessEqual(-2, self.calc.dividir(10, -5))

	def test_division_no_entera_excepcion(self):
		self.failUnlessRaises(ValueError, self.calc.dividir,2, 3)

	def test_division_por_cero_excepcion(self):
		self.failUnlessRaises(ZeroDivisionError, self.calc.dividir, 3,0)
		

if __name__ == '__main__':
	unittest.main()