print("Programa para calcular Tipo de Caudrilatero")

a= eval(input("Escribe el primer lado: "))
b= eval(input("Escribe el segundo lado: "))
c= eval(input("Escribre el tercer lado "))
d= eval(input("Escribre el cuarto lado: "))

if((a==b and c==d and a!=c) or (b==c and a==d and a!=c)):
    print("El cuadrilatero es un rectangulo")
elif(a==b and a==c and a==d):
    print("El cuadrilatero es un cuadrado")
else:
    print("El cuadrilatero es de otro tipo")