#Teniendo como entrada dos strings, mostrar como salida dos nuevas palabras.
#Los dos strings que se reciban como entrada deben dividirse a la mitad. 
# Si el número de caracteres es impar, la primera mitad se quedará con el carácter de en medio. 
# Si, por ejemplo, la palabra tiene 5 caracteres, la primera mitad se quedará con tres caracteres y 
# la segunda con dos.
#Se desplegarán dos nuevos strings combinando las mitades de cada palabra recibida.

#Entrada:
#Dos strings que representan dos palabras, cada uno en un renglón.
#Salida:
#Dos strings que se forman de la combinación de las palabras recibidas como entrada. Los strings se despliegan cada uno en un renglón.
#La primera palabra de salida debe comenzar con la primera mitad del primer string y terminar con la segunda mitad del segundo string.
#La segunda palabra de salida debe comenzar con la segunda mitad del primer string y terminar con la primera mitad del segundo string.

def main():
    palabra1 = input()
    palabra2 = input()

    # // es división entera: al sumar 1 antes, la primera mitad recibe
    # también el carácter central cuando la palabra tiene longitud impar.
    
    mitad1 = (len(palabra1) + 1) // 2
    mitad2 = (len(palabra2) + 1) // 2

    primera_mitad1 = palabra1[:mitad1]
    segunda_mitad1 = palabra1[mitad1:]
    primera_mitad2 = palabra2[:mitad2]
    segunda_mitad2 = palabra2[mitad2:]

    nueva_palabra1 = primera_mitad1 + segunda_mitad2
    nueva_palabra2 = segunda_mitad1 + primera_mitad2

    print(nueva_palabra1)
    print(nueva_palabra2)
    
if __name__=='__main__':
    main()
