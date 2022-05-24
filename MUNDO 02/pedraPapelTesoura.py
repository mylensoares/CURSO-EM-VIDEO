import random
import time
itens = ("PEDRA", "PAPEL", "TESOURA")
print("=*30")
pc_escolhe = random.randint(0, 2)
time.sleep(1)
print("Insira -1 para finalizar o programa")
print("\033[1;31mJÔ\033[m",end=" ")
time.sleep(1)
print("\033[1;31mKEN\033[m", end=" ")
time.sleep(1)
print("\033[1;31mPÔ!!!\033[m")
while True:
    usuario_escolhe = input("Pedra, Papel ou tesoura? ").upper().strip()
    pc_escolhe = random.randint(0, 2)
    if itens[pc_escolhe] == usuario_escolhe:
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;93mEMPATE!\033[m")
    elif itens[pc_escolhe] == "PEDRA" and usuario_escolhe == "PAPEL":
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;32mUsuário Venceu!\033[m")
    elif itens[pc_escolhe] == "PEDRA" and usuario_escolhe == "TESOURA":
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;31mComputador Venceu!\033[m")
    elif itens[pc_escolhe] == "PAPEL" and usuario_escolhe == "PEDRA":
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;31mComputador Venceu!\033[m")
    elif itens[pc_escolhe] == "PAPEL" and usuario_escolhe == "TESOURA":
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;32mUsuário Venceu!\033[m")
    elif itens[pc_escolhe] == "TESOURA" and usuario_escolhe == "PEDRA":
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;32mUsuário Venceu!\033[m")
    elif itens[pc_escolhe] == "TESOURA" and usuario_escolhe == "PAPEL":
        print("O computador escolheu:", itens[pc_escolhe])
        print("O Usuário escolheu:", usuario_escolhe)
        print("\033[1;31mComputador Venceu!\033[m")
    elif usuario_escolhe == "-1":
        print("\033[1;36mSistema Finalizado!\033[m")
        break
    else:
        print("\033[1;35mInválido, tente novamente\033[m")
