"""
Define el simulador del Radar
"""
import matplotlib.pyplot as pp

class Radar(object):
	
	def __init__(self, generador, detector):
		self.generador = generador
		self.detector = detector

	def plot_senial(self, senial_emitida, resultado):
		pp.figure()
		pp.plot(senial_emitida, label = 'senial generada por el radar')
		pp.plot(resultado, label = 'senial detectada por el radar')
		pp.legend()
		pp.savefig('senial_radar.png')
		pp.show()
		
	def detectar(self, medio, tiempo_inicial, tiempo_final):

		"""
		Detecta si hay un blanco en un medio, en un intervalo de tiempo.
		"""
        
		una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
 
		una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, tiempo_final)

		self.plot_senial(una_senal, una_senal_reflejada)

		return self.detector.detectar(una_senal_reflejada, una_senal)


