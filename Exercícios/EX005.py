def dados():   
    print("==="*20)
    nome = str(input("Digite seu nome: "))
    while True:
        try:
            print("==="*20)
            idade = int(input("Digite a idade: "))
            print("==="*20)
            break  # se deu certo, sai do laço
        except ValueError:
            print("==="*20)
            print("Idade inválida. Digite um número inteiro.")
    peso = input("Digite seu peso: ")
    print("==="*20)
    altura = input("Digite sua altura: ")
    print("==="*20)
    sexo = str(input("Digite seu sexo: "))
    print("==="*20)
    while sexo not in ['M', 'F', 'm', 'f', 'Masculino', 'Feminino', 'masculino', 'feminino', 'MASCULINO', 'FEMININO']:
        print("Opção inválida. Digite 'M' para masculino ou 'F' para feminino.")
        print("==="*20)
        sexo = str(input("Digite seu sexo: "))
        print("==="*20)
    print(f"Prazer em te conhecer {nome}, você tem {idade} anos, pesa {peso} kg, mede {altura} metros e é do sexo {sexo}.")
    print("==="*20)

dados()