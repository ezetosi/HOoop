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
        
        if self.tiempo_inicial > tiempo_inicial and tiempo_final > self.tiempo_inicial:
            
            senial_reflejada = [self.amplitud*sen for sen in senial]
            
        return senial_reflejada
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        pass
        
