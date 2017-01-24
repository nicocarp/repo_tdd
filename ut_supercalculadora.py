import unittest
import supercalculadora
import expr_aritmetica


class TestsSuperCalculadora(unittest.TestCase):
	def setUp(self):
		self.exp = expr_aritmetica.ExpresionAritmetica()
		self.su = supercalculadora.Supercalculadora(self.exp)

	def test_sumar(self):
		self.failUnlessEqual(4, self.su.calcular("2 + 2"))

	def test_otra_suma(self):
		self.failUnlessEqual(3, self.su.calcular("2 + 1"))

	def test_resta(self):
		self.failUnlessEqual(1, self.su.calcular("3 - 2"))

	def test_op_compleja_sin_parentesis_sin_precedencia(self):
		self.failUnlessEqual(5, self.su.calcular("3 + 4 - 2"))

	def test_op_compleja_sin_parentesis_con_precedencia(self):
		self.failUnlessEqual(4, self.su.calcular("3 + 4 / 2 - 1"))

	def test_otra_op_compleja_sin_parentesis_con_precedencia(self):
		self.failUnlessEqual(8, self.su.calcular("3 + 4 / 2 - 1 + 8 / 2"))

	def test_multiplicacion_simple(self):
		self.failUnlessEqual(2, self.su.calcular("2 * 1"))
		self.failUnlessEqual(12, self.su.calcular("4 * 3"))
	
	def test_multiplicacion_negativa(self):
		self.failUnlessEqual(-2, self.su.calcular("2 * -1"))

	def test_multiplicacion_negativa_compleja(self):
		self.failUnlessEqual(16, self.su.calcular("2 * 2 * 2 * 2"))

	def test_expr_compleja_todas_operaciones_sin_parentesis(self):
		self.failUnlessEqual(11, self.su.calcular("4 - -3 * 2 / 3 + 5"))