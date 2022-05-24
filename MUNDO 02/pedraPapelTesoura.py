import random
import time
itens = ("PEDRA", "PAPEL", "TESOURA")
print("=*30")
pc_escolhe = random.randint(0, 2)
time.sleep(1)
print("JÔ",end=" ")
time.sleep(1)
print("KEN", end=" ")
time.sleep(1)
print("PÔ!!!")
usuario_escolhe = input("Pedra, Papel ou tesoura? ").upper().strip()
if itens[pc_escolhe] == usuario_escolhe:
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("EMPATE!")
elif itens[pc_escolhe] == "PEDRA" and usuario_escolhe == "PAPEL":
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("Usuário Venceu!")
elif itens[pc_escolhe] == "PEDRA" and usuario_escolhe == "TESOURA":
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("Computador Venceu!")
elif itens[pc_escolhe] == "PAPEL" and usuario_escolhe == "PEDRA":
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("Computador Venceu!")
elif itens[pc_escolhe] == "PAPEL" and usuario_escolhe == "TESOURA":
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("Usuário Venceu!")
elif itens[pc_escolhe] == "TESOURA" and usuario_escolhe == "PEDRA":
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("Usuário Venceu!")
elif itens[pc_escolhe] == "TESOURA" and usuario_escolhe == "PAPEL":
    print("O computador escolheu:", itens[pc_escolhe])
    print("O Usuário escolheu:", usuario_escolhe)
    print("Computador Venceu!")

