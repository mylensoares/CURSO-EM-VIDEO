preço = float(input("Informe o preço do produto: R$"))
print("Forma de pagamento:")
print("1. À vista em Dinheiro ou Cheque (10% de desconto)")
print("2. À vista no Cartão (5% de desconto)")
print("3. 2x no Cartão (preço integral)")
print("4. 3x ou mais no Cartão (20% de Juros)")
opcao = int(input("Escolha sua opção (1, 2, 3, 4 ou 5): "))
if opcao == 1:
    valor = preço - (preço * 10/100)
    print(f"O valor do produto será R${valor:.2f}")
elif opcao == 2:
    valor = preço - (preço * 5/100)
    print(f"O valor do produto será R${valor:.2f}")
elif opcao == 3:
    valor = preço / 2
    print(f"O valor do produto será R${preço:.2f} em 2 parcelas de R${valor} cada ")
elif opcao == 4:
    valor = preço + (preço * 20/100)
    quant_parcelas = int(input("Em quantas parcelas: "))
    total_parcelas = valor / quant_parcelas
    print(f"O valor total do produto será R${valor:.2f} em {quant_parcelas}x de R${total_parcelas:.2f}")
else:
    print("Valor inválido, utilize 1, 2, 3 ou 4 para selecionar a forma de pagamento")

    

