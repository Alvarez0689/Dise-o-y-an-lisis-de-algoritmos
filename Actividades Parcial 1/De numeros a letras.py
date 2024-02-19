
from num2words import num2words

def convertir_numero_a_palabra(numero):
    try:
        n = float(numero)
        print(n)
        if(n<=0 or n>1000000000000000000):
            print("Numero fuera del rango")
        else:
            palabra = num2words(n, lang='es')
            return palabra
    except ValueError:
        return "Por favor, ingrese un número válido."

numero = input("Ingrese un número entre 1 y 1,000,000,000,000,000,000,000: ")
palabra = convertir_numero_a_palabra(numero)
if(palabra):
    print("El número {} en palabras es: {}".format(numero, palabra))

    