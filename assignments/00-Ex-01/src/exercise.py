# Crea un programa que pida al usuario dos cadenas de caracteres como entrada e imprima la cadena 
# con la longitud mayor en la consola. 
# Si las dos cadenas tienen la misma longitud, la función debe imprimir ambas cadenas una en cada renglón.

def main():
        #escribe tu código abajo de esta línea
        cadena1 = input()
        cadena2 = input()

        if len(cadena1) > len(cadena2):
            print(cadena1)
        elif len(cadena2) > len(cadena1):
            print(cadena2)
        else:
            print(cadena1)
            print(cadena2)

if __name__=='__main__':
    main()
