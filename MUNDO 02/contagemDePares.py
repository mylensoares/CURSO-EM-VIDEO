print("Defina o intervalo: ")
i = int(input("Início: "))
f = int(input("Fim: "))
print(f"Os números pares entre {i} e {f} são:")
for c in range(i, f+1):
        if c % 2 == 0:
            print(c)