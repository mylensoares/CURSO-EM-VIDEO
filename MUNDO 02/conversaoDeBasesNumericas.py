num = int(input("Digite um número inteiro que vc deseja converter: "))
legenda = int(input("Informe para qual base numérica você deseja realizar a conversão:\n 1-Binário\n 2-Octal\n 3-Hexadecimal\n Sua opção:"))
if legenda == 1:
    conversao_bin = bin(num)[2:]
    print(f"O número {num} convertido para binário é {conversao_bin}")
elif legenda == 2:
    conversao_octal = oct(num)[2:]
    print(f"O número {num} convertido para Octal é {conversao_octal}")
elif legenda == 3:
    conversao_hexa_dec = hex(num)[2:]
    print(f"O número {num} convertido para Hexadecimal é {conversao_hexa_dec}")
else:
    print("Informe um valor várido (1, 2 ou 3)")

