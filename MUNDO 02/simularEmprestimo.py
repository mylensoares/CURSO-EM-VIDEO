def calculaPrestacao(valor, salario, tempo):
    prestacao = valor / (tempo*12)
    if prestacao <= 30/100 * salario:
        return f"O valor da prestação mensal é de R${prestacao:.2f} em {tempo*12} meses"
    else:
        return "Empréstimo Negado"

valorImóvel = float(input("Digite o valor do imovel: "))
valorSalario = float(input("Informe o valor do seu salário: "))
anosQuitar = int(input("Em quantos anos vc pretende quitar o imóvel: "))


print(calculaPrestacao(valorImóvel, valorSalario, anosQuitar))
