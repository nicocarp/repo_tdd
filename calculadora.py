class Calculadora:
	def sumar(self, a, b):
		return a + b

	def restar(self, a, b):
		return a - b

	def dividir(self, a, b):
		if a % b != 0:
			raise ValueError
		
		return a / b

	def multiplicar(self, a, b):
		return a * b
