
x = range(5)

n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))
n4 = int(input("Digite o quarto numero:"))
n5 = int(input("Digite o quinto numero:"))

numero = n1,n2,n3,n4,n5

for _ in x:
    numero = int(input("Digite um número:"))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f"O maior número é o  {n1}")
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(f"O maior número é o {n2}")
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 >n5:
    print(f"O maior número é o {n3}")
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print(f"O maior número é o {n4}")
elif n5 > n1 and n5> n2 and n5> n3 and n5 > n4:
    print(f"O maior número é o {n5}")