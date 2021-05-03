def  estCondicional01 ():
  #Definir variables y otros
  print ( "Ejemplo estructura Condicional en Python" )
  montoP = 0
  #Datos de entrada
  cantidadX = int ( input ( "Ingrese la cantidad de lapices:" ))
  #Proceso
  si  cantidadX > = 1000 :        
    montoP = cantidadX * 0.80
  otra cosa :
    montoP = cantidadX * 0.90  
  #Datos de salida
  print ( "El monto a pagar es:" , montoP )
def  estCondicional02 ():
  #Definir variables y otros
  print ( "Ejercicio 02 Est. Condicional" )
  montoP = 0
  #Datos de entrada
  cantidadX = int ( input ( "Ingrese la cantidad de personas invitadas:" ))
  #Proceso
  si  cantidadX < 200 :
    montoP = cantidadX * 95
  elif  cantidadX > 200  y  cantidadX <= 300 :
    montoP = cantidadX * 85
  otra cosa :
    montoP = cantidadX * 75
  #Datos de salida
  print ( "La cantidad a pagar es:" , montoP )

# estCondicional01 ()
estCondicional02 () 