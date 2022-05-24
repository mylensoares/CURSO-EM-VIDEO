numeros = []
maior = 0
menor = 0
for i in range(0, 2):
    num = int(input("Informe um número: "))
    numeros.append(num)
    for e in range(len(numeros)):
        if e == 0: 
            maior = menor = numeros[e]
        else:
            if numeros[e] >= maior:
                maior = numeros[e]
            if numeros[e] <= menor:
                menor = numeros[e]

print(f"O maior valor digitado foi {maior} e o menor {menor}")

    