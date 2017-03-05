class Detector(object):

    def __init__(self):
        #TODO: completar con la inicializacion de los parametros del objeto
        #self.umbral_deteccion = umbral_deteccion
        pass

    def detectar(self, senial, senial_generada):
        #TODO: Completar

        if max(senial) > max(senial_generada):
            print 'se detecto un blanco'
        else:
            print 'no se detecto nada'
		
        return senial
        
        pass