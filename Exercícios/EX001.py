idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade <=25 and idade >= 18:
    print("Você é jovem maior de idade, mas ainda é jovem.")
else:
    print("Você é um adulto.")