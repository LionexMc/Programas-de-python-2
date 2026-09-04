print("CONTADOR DE DÍGITOS")

numero = int(input("Ingresa un número entero: "))

numero = abs(numero)

if numero == 0:
    digitos = 1
else:
    digitos = 0

    while numero > 0:
        numero = numero // 10
        digitos += 1

print("El número tiene", digitos, "dígitos.")
