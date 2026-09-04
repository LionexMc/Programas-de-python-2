print("NÚMERO INVERTIDO")

numero = int(input("Ingresa un número entero: "))

signo = 1

if numero < 0:
    signo = -1
    numero = abs(numero)

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

invertido = invertido * signo

print("El número invertido es:", invertido)
