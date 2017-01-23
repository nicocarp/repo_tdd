import expr_aritmetica
import calculadora
class Supercalculadora:

	def __init__(self, expr):
		self.calc = calculadora.Calculadora()
		self.expr = expr_aritmetica.ExpresionAritmetica()

	def __resolver_precedencia__(self, exp):
		operadores = exp['operadores']
		operandos = exp['operandos']
		res_intermedio = 0
		nuevos_operandos = operandos
		nuevos_operadores = operadores
		eliminar = []
		res_intermedios = []
		for i in range(len(operadores)):
			if operadores[i] == '*':
				res_intermedio += self.calc.multiplicar(int(operandos[i]), int(operandos[i + 1]))
				res_intermedios.append(res_intermedio)
				eliminar.append(i)
				res_intermedio = 0
			elif operadores[i] == '/':
				res_intermedio += self.calc.dividir(int(operandos[i]), int(operandos[i + 1]))
				res_intermedios.append(res_intermedio)
				eliminar.append(i)
				res_intermedio = 0				
		
		delta =0
		for i in range(len(eliminar)):			
			operandos.pop(eliminar[i] - delta)
			operandos.pop(eliminar[i] - delta )
			operandos.insert(eliminar[i], res_intermedios[i])
			delta += 1

		while True:
			try:
				operadores.remove('*')
			except:
				break
		while True:
			try:
				operadores.remove('/')
			except:
				break
		return res_intermedio

	def calcular(self, expresion):
		exp_limpia = self.expr.parse(expresion)
		# nos encargamos de resolver primero las divisiones, luego las multiplicaciones y devolvemos resultado
		res_intermedio = self.__resolver_precedencia__(exp_limpia)
		res = 0
		for i in range(len(exp_limpia['operadores'])):
			if i == 0:
				res = exp_limpia['operandos'][0]
			if exp_limpia['operadores'][i] == '+':
				res = self.calc.sumar(res, exp_limpia['operandos'][i+1])
			if exp_limpia['operadores'][i] == '-':
				res = self.calc.restar(res, exp_limpia['operandos'][i+1])
		return res

if __name__ == '__main__':
	e = expr_aritmetica.ExpresionAritmetica()
	s = Supercalculadora(e)
