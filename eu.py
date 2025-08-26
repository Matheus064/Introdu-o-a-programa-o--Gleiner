num_jogadores=int(input("Escreva o número de jogadores "))
soma=0
for i in range(num_jogadores):
    altura_jogadores=float(input("Escreva o altura dos jogadores"))
    soma+=altura_jogadores
print("A média de altura dos jogadores é: ",soma/num_jogadores)



