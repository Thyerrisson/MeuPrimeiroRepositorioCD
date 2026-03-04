pontos = 0
tripulacao = ["Tripulante 1", "Tripulante 2", "Tripulante 3"]
passo_atual = 1

pontos_atual = pontos

print("Bem-vindos à missão de exploração do planeta Alphara-7!")

while passo_atual <= 9:

    if passo_atual == 1:
        passo_atual += 1
        print("Vocês chegaram no planeta Alphara-7. Tome cuidado com as suas decisões!")

    elif passo_atual == 2:
        decisao = input("Vocês começam a sua exploracão. Vocês encontram uma área rica em minerais e em sinais de vida? (Digite 'sim' ou 'nao'): ")
    
        if decisao == "sim":
            print("Parabéns! Vocês encontraram uma área rica em minerais e sinais de vida. Vocês ganham 10 pontos!")
            pontos += 10
            pontos_atual = pontos
            passo_atual = 3
            print(f"Você está no passo {passo_atual}")
            print(f"Você tem {pontos_atual} pontos!")

        elif decisao == "nao":
            print("Que pena! Continue sua exploração.")
            passo_atual = 3
            print(f"Você está no passo {passo_atual}")

    elif passo_atual == 3:
        decisao = input("Vocês encontram uma montanha? (Digite 'sim' ou 'nao'): ")

        if decisao == "sim":
            decisao = input("Vocês decidem escalar ou contornar a montanha? (Digite 'escalar' ou 'contornar')")

            if decisao == "escalar":

                passo_atual = 4
                print(f"Você está no passo {passo_atual}")
                print("Vocês conseguem escalar a montanha? (Digite 'sim' ou 'nao')")
                decisao = input("Digite sua resposta: ")
                if decisao == "sim":
                    print("Parabéns! Vocês ganham mais 5 pontos por escalarem a montanha com sucesso!")
                    pontos += 5
                    pontos_atual = pontos
                    passo_atual = 8
                    print(f"Você está no passo {passo_atual}")
                    print(f"Você tem {pontos} pontos!")

                elif decisao == "nao":
                    print("Que pena! Vocês não conseguem escalar a montanha e perdem 5 pontos.")
                    pontos -= 5
                    pontos_atual = pontos
                    passo_atual = 2
                    print(f"Você tem {pontos} pontos!")

                    print(f"Você está no passo {passo_atual}")

            elif decisao == "contornar":
                passo_atual = 8
                print(f"Você está no passo {passo_atual}")
                print("Vocês decidem tomaram a melhor decisão! Mais 10 pontos!")
                pontos += 10
                pontos_atual = pontos
                print(f"Você tem {pontos_atual} pontos!")

        elif decisao == "nao":
            print("Vocês continuam explorando o planeta.")
            passo_atual = 2
            print(f"Você está no passo {passo_atual}")

    elif passo_atual == 8:
        decisao = input("Depois de uma longa exploração, vocês decidem se querem voltar para a nave ou continuar explorando (digite 'voltar' ou 'continuar')")

        if decisao == "voltar":
            passo_atual = 9
            print(f"Você está no passo {passo_atual}")
            print("Vocês decidem voltar para a nave e terminar a exploração. Parabéns!")
            
        elif decisao == "continuar":
            passo_atual = 3

    elif passo_atual == 9:
        print(f"Fim do jogo! Vocês voltaram para a terra com um total de {pontos}!")
    