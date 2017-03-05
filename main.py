import radar
import medio
import blanco
from generador import Generador
import datetime
import detector
import numpy as np
import matplotlib.pyplot as pp
import scipy as sp
from scipy.misc import derivative

# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():
	
    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)
	
    import math
	# parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo generador de senales
    generador_seniales = Generador(amplitud, fase, frecuencia)
	
#    senial_generada = generador_seniales.generar(tiempo_inicial, tiempo_final)
	
    # print senial
	
    ### PARA PLOTEAR FUNCION #####
    #pp.figure()
    #pp.plot(senial)
    #pp.show()
    ##############################
	
    #TODO construir un detector
    mi_detector = detector.Detector()
	
    #TODO construir un nuevo radar
    mi_radar = radar.Radar(generador_seniales,mi_detector)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + amplitud*2 #cambio la amplitud de amplitud + 100 para que sea apreciable en la gráfica
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2) #si cambio el año a 2015 obtengo que no hay blanco detectado
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #TODO contruir un nuevo blanco
    nuevo_blanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)
    mis_blancos=[nuevo_blanco]

    #TODO contruir un medio
    mi_medio = medio.Medio(mis_blancos)

    #TODO construir un radar--- PONERLO A FUNCIONAR AL RADAR
    senial_emitida = generador_seniales.generar(tiempo_inicial, tiempo_final)
    resultado = mi_radar.detectar(mi_medio, tiempo_inicial, tiempo_final)
    
    print resultado
    ### PARA PLOTEAR FUNCION #####
    pp.figure()
    pp.plot(senial_emitida)
    pp.plot(resultado)
    pp.show()
    ##############################

if __name__ == "__main__":
    main()