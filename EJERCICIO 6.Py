#Nivel básico:
#Verificar si un número es positivo, negativo o cero
#Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

def evaluar_numero():
numero = int(input("ingrese un numero:"))

if numero > 1:
    return "positive"

else: 
    return "negative"

resultado = evaluar_numero()
print (resultado)
