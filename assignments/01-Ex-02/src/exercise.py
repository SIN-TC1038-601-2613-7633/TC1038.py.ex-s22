# Programa que lea un string y muestre fragmentos de este.
# En la primera línea imprimir la longitud del string recibido.
# En la segunda línea imprimir solo el primer carácter del string recibido.
# En la tercera línea imprimir solo el último carácter del string recibido.
# En la cuarta línea imprimir solo los caracteres con índice impar dentro del string.

def main():
    cadena = input()
    print(len(cadena))
    print(cadena[0])
    print(cadena[-1])
    print(cadena[1::2])

if __name__=='__main__':
    main()
