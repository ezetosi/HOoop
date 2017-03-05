class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
		#TODO: completar con la inicializacion de los parametros del objeto
		self.amplitud = amplitud
		self.tiempo_inicial = tiempo_inicial
		self.tiempo_final = tiempo_final
		pass
		
    def reflejar(self, senial, tiempo_inicial, tiempo_final):
		
		senial_reflejada = [0.]*len(senial)
		
		dt = (tiempo_final - tiempo_inicial).seconds / len(senial)
		
		si = (self.tiempo_inicial - tiempo_inicial).seconds
		sf = (self.tiempo_final - tiempo_inicial).seconds
		
		if (self.tiempo_inicial >= tiempo_inicial):
			ni = int(si/dt)
			if (self.tiempo_final <= tiempo_final):
				nf = int(sf/dt)
			else:
				nf = len(senial)
		else:
			ni = 0
			if (self.tiempo_final >= tiempo_inicial):
				if (self.tiempo_final <= tiempo_final):
					nf = int(sf/dt)
				else:
					nf = len(senial)
			else:
				nf = 0
		
		for i in range(ni,nf):
			senial_reflejada[i] = senial[i] * self.amplitud
            
		return senial_reflejada

		pass
        
