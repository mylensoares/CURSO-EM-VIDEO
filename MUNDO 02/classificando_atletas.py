from datetime import date
def calculaidade():
    ano_atual = date.today().year
    ano_nascimento = int(input("Informe seu ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    return idade
print("Confederação Brasileira de Natação")
idade_atleta = calculaidade()
print(f"Sua idade é {idade_atleta}")
if idade_atleta <= 9:
    print("Sua categoria será Mirim")
elif idade_atleta <=14:
    print("Sua categoria será Infantil")
elif idade_atleta <= 19:
    print("Sua categoria será Júnior")
elif idade_atleta <= 25:
    print("Sua categoria será Sênior")
else:
    print("Sua categoria será Master")





