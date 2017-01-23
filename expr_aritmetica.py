import string

class ExpresionAritmetica:

	def __es_numero__(self, cadena):
		try:
			string.atoi(cadena)
			return True
		except ValueError:
			return False
	
	def parse(self, expresion):
		operandos =  []
		operadores = []
		for palabra in expresion.split():
			if self.__es_numero__(palabra):
				operandos.append(string.atoi(palabra))
			else:				
				operadores.append(palabra)				
		return {'operandos': operandos, 'operadores':operadores}