def  paquetesJECH ():
  #Definir Variables
  resultPaqueteDmp = ""
  #Datos de entrada
  montoRvDiDmpc = float ( input ( "Ingrese el monto que recibe en diciembre:" ))
  #Proceso
  si  montoRvDiDmpc > = 50000 :
    resultPaqueteDmp = "Paquete A"
  elif  montoRvDiDmpc > = 20000  y  resultPaqueteDmp < 50000 :
    resultPaqueteDmp = "Paquete B"
  elif  montoRvDiDmpc > = 10000  y  montoRvDiDmpc < 20000 :
    resultPaqueteDmp = "Paquete C"
  otra cosa :
    resultPaqueteDmp = "Paquete D"
  #Datos de salida
  print ( "La persona comprara el:" , resultPaqueteDmp )

def  paquetes ():
  #Definir Variables
  resultPaquete = ""
  #Datos de entrada
  montoRvDic = float ( input ( "Ingrese el monto que recibe en diciembre:" ))
  #Proceso
  si  montoRvDic > = 50000 :
    resultPaquete = "Paquete A"
  elif  montoRvDic > = 20000  y  montoRvDic < 50000 :
    resultPaquete = "Paquete B"
  elif  montoRvDic > = 10000  y  montoRvDic < 20000 :
    resultPaquete = "Paquete C"
  otra cosa :
    resultPaquete = "Paquete D"
  #Datos de salida
  print ( "La persona comprara el:" , resultPaquete )


# estCondicional02 ()
# estCondicional01 ()
#bonoDocente ()

paquetesJECH ()