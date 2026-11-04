# Desarrolla un programa que contenga una función que identifique si una palabra es un palíndromo o no.
# El programa debe funcionar aún cuando la frase incluya espacios entre palabras y
# si tiene diferencias entre mayúsculas o minúsculas.

def es_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

def main():
    #escribe tu código abajo de esta línea
    frase = input()
    if es_palindromo(frase):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__=='__main__':
    main()
