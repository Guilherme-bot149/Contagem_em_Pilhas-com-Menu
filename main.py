caixas = int(input("Quantas caixas vc quer empilhar: "))
pilha = list(range(1, caixas+1))

print(f"E - Empilhar caixas")
print(f"D - Desempilhar caixas")
print(f"S - Sair")

while True:
    operacao = input("Digite a operacao >>>> ")
    if operacao == "D":
        if len(pilha) > 0:
            retirado = pilha.pop(-1)
            print(f"Caixa número {retirado} foi retirado!")
            print(f"{pilha}")
        else:
            print(f"Pilha de caixas vazia!")
    elif operacao == "E":
        novo = len(pilha)+1
        pilha.append(novo)
        print(f"Caixa número {novo} foi empilhado!")
        print(f"{pilha}")
    elif operacao == "S":
        break
    else:
        print(f"Valor digitado [{operacao}] não e operação valida!")
pilha(f"Pilha final: {pilha}")
