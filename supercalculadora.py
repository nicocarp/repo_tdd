import expr_aritmetica
import calculadora
class Supercalculadora:

	def __init__(self, expr):
		self.calc = calculadora.Calculadora()
		self.parser = expr

	def __operar__(self, expr_descompuesta):
		i = None
		res_intermedio = 0
		
		if '*' in expr_descompuesta['operadores']:
			i = expr_descompuesta['operadores'].index('*')
			res_intermedio = self.calc.multiplicar(expr_descompuesta['operandos'][i],expr_descompuesta['operandos'][i + 1])
		elif '/' in expr_descompuesta['operadores']:
			i = expr_descompuesta['operadores'].index('/')
			res_intermedio = self.calc.dividir(
			expr_descompuesta['operandos'][i],
			expr_descompuesta['operandos'][i + 1])
		elif '-' in expr_descompuesta['operadores']:
			i = expr_descompuesta['operadores'].index('-')
			res_intermedio = self.calc.restar(expr_descompuesta['operandos'][i], expr_descompuesta['operandos'][i + 1])
		elif '+' in expr_descompuesta['operadores']:
			i = expr_descompuesta['operadores'].index('+')
			res_intermedio = self.calc.sumar(expr_descompuesta['operandos'][i],expr_descompuesta['operandos'][i + 1])
		else:
			# Es un error, tenemos que decidir que hacer en los test
			# siguientes
			# Forzamos el error para que no haya problemas luego
			assert False		
		return (i, res_intermedio)

	def __simplificar__(self, expr_descompuesta):
		if expr_descompuesta['operadores'] == []:
			return expr_descompuesta		
		(i, res_intermedio) = self.__operar__(expr_descompuesta)
		expr_simplificada = expr_descompuesta
		expr_simplificada['operadores'].pop(i)
		expr_simplificada['operandos'].pop(i)
		expr_simplificada['operandos'].pop(i)
		expr_simplificada['operandos'].insert(i, res_intermedio)		
		return self.__simplificar__(expr_simplificada)

	def calcular(self, expresion):
		return self.__simplificar__(self.parser.parse(expresion))['operandos'][0]