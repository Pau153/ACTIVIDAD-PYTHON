# if condicional si es o no mayo de 18

#edad = int(input("ingrese su edad:"))
#if edad >= 18:
  #  print("eres mayor de edad")
    
#if edad <18:
   # print("eres menor de edad")
    
    
    
    
    
#else y eliF condicional si es mayor de edad o no 
#edad = int(input("ingrese su edad:"))
#if edad >= 18:
 #   print("eres mayor de edad")


#elif edad ==18:
 #   print("tenes 18 años")

#else:
    #print("eres menor de edad")
    
    



#return
def es_mayor_de_edad(edad):
 if edad >= 18:
    return True 
 else:
    return False


edad_usuario =15
resultado = es_mayor_de_edad(edad_usuario)
print ("¿es mayor de edad?" , resultado)