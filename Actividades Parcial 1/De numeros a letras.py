
from num2words import num2words

def convertir_numero_a_palabra(numero):
    try:
        if(numero<=0 or numero>1000000000000000000):
                print("Numero fuera del rango")
                return ""
        if isinstance(numero, int):
            palabra = num2words(numero, lang='es')
            return palabra
        elif isinstance(numero, float):  
            parte_entera,parte_decimal = ("{:.1f}").format(numero).split('.')
            parte_entera_palabra = num2words(int(parte_entera), lang='es')
            parte_decimal_palabra = num2words(int(parte_decimal), lang='es')
            return parte_entera_palabra + " punto " + parte_decimal_palabra
    except TypeError:
        print("Por favor, ingrese un tipo de dato correcto.")
        return ""
try:
    numero = eval(input("Ingrese un número entre 1 y 1,000,000,000,000,000,000: "))
    palabra = convertir_numero_a_palabra(numero)
    if(palabra):
        print("El número {} en palabras es: {}".format(numero, palabra))
except NameError:
    print("Por favor, ingrese un tipo de dato correcto.")

 