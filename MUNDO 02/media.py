nota1 = float(input("Informe sua nota da av1: "))
nota2 = float(input("Informe sua nota da av2: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Aprovado!,  media {media:.2f}.")
elif media < 7 and media >= 5:
    print(f"Recuperação!, media {media:.2f}.")
else:
    print(f"Reprovado!, media {media:.2f}.")