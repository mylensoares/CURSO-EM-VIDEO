peso = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura(m): "))
imc = peso / (altura**2)
print(f"O seu imc corresponde a {imc:.1f}")
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
