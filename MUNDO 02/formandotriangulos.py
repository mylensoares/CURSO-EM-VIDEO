s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os Segmentos podem formar um triangulo")
    if s1 == s2 == s3:
        print("Todos os lados são iguais formando um triangulo Equilátero")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("O triângulo possui dois lados igual e um diferente formando um triangulo Isósceles")
    else:
        print("Todos os lados são diferentes, formando um triângulo Escaleno")
else:
    print("Os segmentos não podem formar um triângulo")
