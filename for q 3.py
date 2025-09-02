N = int(float(input("Digite um número: ")))
soma = 0
for i in range(1, N + 1 ):
    soma += i
print("A soma dos números inteiros de 1 a", N, "é:", soma)