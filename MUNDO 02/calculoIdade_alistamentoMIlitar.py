from datetime import date
ano_atual = date.today().year
sexo = str(input("Informe o seu sexo (M ou F) : ")).upper().strip()
if sexo == 'M':
    data = int(input("Informe o ano do seu Nascimento: "))
    idade = ano_atual - data
    if idade == 18:
        print(f"Você tem {idade} anos e está no tempo de realizar o seu Alistamento militar")
    elif idade > 18:
        atraso = idade - 18
        print(f"Você tem {idade} anos e já se passaram {atraso} anos do período do seu Alistamento Militar")
        periodo_alist = ano_atual - atraso
        print(f"O ano do seu alistamento foi em {periodo_alist}")
    else:
        restam = 18 - idade
        print(f"Você tem {idade} anos e faltam {restam} anos para o seu Alistamento Militar")
        periodo_alist = ano_atual + restam
        print(f"O seu alistamento será em {periodo_alist}")
elif sexo == "F":
    print("Mulheres não estão obrigadas ao alistamento militar")
else:
    print("Inválido")