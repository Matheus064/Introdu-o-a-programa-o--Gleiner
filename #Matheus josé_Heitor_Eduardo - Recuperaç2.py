#Matheus josé_Heitor_Eduardo - Recuperação
numero = input("Digite um número: ")

contador_impares = 0
for digito in numero:
    if digito in "13579":
        contador_impares += 1

fatorial = 1
for i in range(1, contador_impares + 1):
    fatorial *= i

print("Quantidade de dígitos ímpares:", contador_impares)
print("Fatorial:", fatorial)