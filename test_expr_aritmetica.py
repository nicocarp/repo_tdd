import unittest
import expr_aritmetica

class TestsExprAritmetica(unittest.TestCase):
	def setUp(self):
		self.expr  = expr_aritmetica.ExpresionAritmetica()

	def tearDown(self):
		pass

	def test_extraer_operador_operando_suma_2_y_2(self):
		self.failUnlessEqual({'operandos': [2, 2], 'operadores':['+']}, self.expr.parse("2 + 2"))

	def test_extraer_operador_operando_otro(self):
		self.failUnlessEqual({'operandos': [10, -5], 'operadores':['/']}, self.expr.parse("10 / -5"))

	def test_extraer_operador_operando_complejo(self):
		self.failUnlessEqual({'operandos': [10, 2, 3, 5], 'operadores':[ '*',  '+', '/']}, self.expr.parse("10 * 2 + 3 / 5"))