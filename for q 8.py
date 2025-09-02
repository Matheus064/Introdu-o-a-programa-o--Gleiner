N = int(float(input("Digite um número: ")))
fator = 1
for i in range(1, N+1):
    fator *= i
print(f"O fatorial de {N} é {fator}")