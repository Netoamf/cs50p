X = "X"
O = "O"
VAZIO = " "

tabuleiro = [X, O, X,
            O, X, O,
            O, VAZIO, X]

range(0,9)

#for casa in tabuleiro:
#    print(casa)

for i in range(len(tabuleiro)):
    print(tabuleiro[i])