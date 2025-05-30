print("==="*20)
número = int(input("Digite um número: "))
print("==="*20)
while número != 36:
    if número < 36:
        print(f"O número é maior que {número}.")
        print("==="*20)
    elif número > 36:
        print(f"O número é menor que {número}.")
        print("==="*20)
    else:
        print(f"O número é igual a {número}.")
        print("==="*20)
    número = int(input("Digite um número: "))
    print("==="*20)
print("Você acertou, o número era 36!")