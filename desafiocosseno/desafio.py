def angulo_radiano(angulo):
    radiano = angulo * 3.14159265359 / 180
    return radiano

def fatorial(numero):
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor

def cosseno(grau):
    valor = angulo_radiano(grau)
    z = 1 - (exponencial(valor, 2) / fatorial2) + (exponencial(valor, 4) / fatorial4) - (exponencial(valor, 6) / fatorial6) + (exponencial(valor, 8) / fatorial8) - (exponencial(valor, 10) / fatorial10)
    return z
    

def exponencial(numero, x):
    resultado1 = numero **  x

    return resultado1 

fatorial2 = fatorial(2)
fatorial4 = fatorial(4)
fatorial6 = fatorial(6)
fatorial8 = fatorial(8)
fatorial10 = fatorial(10)


cos = float(input("Informe um valor de angulo para calcular o Cosseno: "))
z = cosseno(cos)

print(f"O cosseno de {cos}° é: {z}")