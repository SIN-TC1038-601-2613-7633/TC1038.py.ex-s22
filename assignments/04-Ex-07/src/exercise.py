# Escribe un programa que lea un string y cuente el número de vocales y consonantes que contiene, 
# ignorando espacios y caracteres especiales.

def main():
    
    texto = input()
    texto = texto.replace(" ", "").lower()

    num_vocales = 0
    num_consonantes = 0

    for c in texto:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            num_vocales += 1
        elif c.isalpha():
            num_consonantes += 1
    
    print(num_vocales)
    print(num_consonantes)

if __name__=='__main__':
    main()
