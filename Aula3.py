#  velocidade = int(input("Qual sua velocidade?"))
# if velocidade >= 80:
#     print("Você ultrapassou o limite de velocidade")
#     velocidade = velocidade - 80
#     print(f"valor da multa é {velocidade*5:.2f}")
# if velocidade <= 80:
#     print("voce está no limite de velocidade")


# a = int(input("Insira o primeiro valor"))
# b = int(input("Insira o segundo valor"))
# c = int(input("Insira o terceiro valor"))
# if a >= b and a >=c:
#     print("a é o valor maior")
# elif b >= a and b >= b:
#     print("b é o valor maior")
# elif c>= a and c >= b:
#     print("c é o maior valor")
#
#     if a <= b and a <= c:
#         print("a é o menor valor")
#     elif b <= a and b <= c:
#         print("b é o menor valor")
#     elif c <= a and c <= b:
#         print("c é o menor valor")

salario = float(input("qual o seu salario?"))
if salario > 1250:
    print(f"ganhou um aumento de {salario * 0.1:.2f}")
else:
    print(f"ganhou um aumento de {salario * 0.15:.2f}")
