import unittest
import supercalculadora
import expr_aritmetica
import validador_expr_aritmetica
import mox

class TestsSuperCalculadora(unittest.TestCase):
	def setUp(self):
		self.exp = expr_aritmetica.ExpresionAritmetica()
		validador = validador_expr_aritmetica.ValidadorExprAritmetica()
		self.su = supercalculadora.Supercalculadora(self.exp, validador)

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

	"""Con este test creamos un stub al cual le indicamos que ante la invocacion indicada devuelve False
		Nos olvidamos de la implementacion real de validar() solo lo simulamos con el mock.
		El objetivo del test es verificar que realmente se realiza la llamada al metodo validar y que al devolver
		Falso el metodo calcular de supercalculadora devuelve una excepcion. Posteriormente a este test podemos comenzar
		a realizar los test correspondientes para la nueva clase creada ValidadorExprAritmetica
	"""
	def test_validador_expresion_invalida_stub(self):
		validador_stub = validador_expr_aritmetica.ValidadorExprAritmetica()
		validar_mock = mox.Mox()
		validar_mock.StubOutWithMock(validador_stub, 'validar')
		validador_stub.validar("2 ^ 3").AndReturn(False)
		validar_mock.ReplayAll()
		sc = supercalculadora.Supercalculadora(expr_aritmetica.ExpresionAritmetica(), validador_stub)
		self.failUnlessRaises(SyntaxError, sc.calcular, "2 ^ 3")
		validar_mock.UnsetStubs()
		validar_mock.VerifyAll()