from operator import add

class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
	
		senal_reflejada = [0.]*len(una_senal)
		
		for blanco in self.blancos:
			senal_blanco = blanco.reflejar(una_senal, tiempo_inicial, tiempo_final)
			senal_reflejada = map(add, senal_reflejada,senal_blanco)
			
		return senal_reflejada
		
		pass