# O computador escolheu um numero secreto entre 1 e 20
# Peça para o usuario tentar adivinhar  o numero e de dicas
# Msg se for maior menor ou se acertar

print(" Vamos brincar do jogo do numero secreto ? ")
palpite = int(input(" Escolha um numero entre 1 e 20 : "))

while palpite != 15:
    if palpite < 15:
        print("Tente um numero maior")
        palpite = int(input(" Escolha um numero entre 1 e 20 : "))

    elif palpite > 15:
        print(" Tente um numero menor ")
        palpite = int(input(" Escolha um numero entre 1 e 20 : "))


print("Parabens!! Você acertouuuu")

