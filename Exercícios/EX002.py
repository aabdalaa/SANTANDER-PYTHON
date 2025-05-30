frutas = ["maçã", "banana", "laranja", "uva", "abacaxi", "kiwi", "morango", "pera", "cereja", "melancia", "mamão", "pêssego", "ameixa", "figo", "coco", "tangerina", "limão", "maracujá", "goiaba", "abacate"]
for fruta in frutas:
    if fruta == "banana":
        print("Encontrei a banana!")
    elif fruta == "maçã":
        print("==="*20)
        print("Seus dentes estão limpos, sua fruta é maça!")
    elif fruta == "laranja":
        print("A laranja é rica em vitamina C!")
    elif fruta == "abacaxi":
        print("Sem vergonha, hein? Escolheu o abacaxi!")
    elif fruta == "abacate":
        print("O abacate é uma fruta muito nutritiva!")
        print("==="*20)
        break
    else:
        print(f"A fruta {fruta} é deliciosa!")
    print("==="*20)
print("Fim do loop de frutas.")
print("==="*20)