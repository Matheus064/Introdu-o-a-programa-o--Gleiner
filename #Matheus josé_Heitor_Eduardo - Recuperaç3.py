#Matheus josé_Heitor_Eduardo - Recuperação

numero=int(input("Digite um número decimal: "))

hexadecimal=""
hex_digitos="0123456789ABCDEF"

num=numero

if num==0:
    hexadecimal="0"
else:
    while num > 0:
        resto=num%16
        hexadecimal = hex_digitos[resto] + hexadecimal
        num=num//16

print("Hexadecimal:", hexadecimal)