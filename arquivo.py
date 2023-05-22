import math # Importando biblioteca para facilitar trabalho
import matplotlib.pyplot as plt # Importando para fazer o gráfico

# Função do item 1 para facilitar o código
def funcaoSegundoGrau(a, b, c):
    # Faz o delta 
    delta = (b**2)  - (4 * a * c)
    # X do vértice e Y do vértice (independente do resultado do delta)
    xv = -b/(2*a)
    print(f"O x do vértice é de {xv:.2f}")
    yv = -delta / (4*a)
    print(f"O y do vértice é de {yv:.2f}")

    #Quando delta é positivo
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        somaRaizes = x1 + x2
        produtoRaizes = x1 * x2
        print(f"O x1 vale {x1:.2f} e o x2 vale {x2:.2f}")
        print(f"A soma das raízes é de {somaRaizes:.2f}")
        print(f"O produto das raízes é de {produtoRaizes:.2f}")

    # Delta = 0
    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"As raízes são iguais valendo {x1}")

    # Delta menor que 0
    elif delta < 0:
        print(f"Não há raízes de números reais.")

def graficoFuncao(a, b, c):
    x = []
    y = []
    i = -10
    while i <= 10:
        x.append(i)
        f = a * i**2 + b * i + c
        y.append(f)
        i += 0.1

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico da Função de Segundo Grau')
    plt.grid(True)
    plt.show()

    print(x)
    print(y)


# Pedindo para o usuário digitar os valores de a, b e c
a = float(input("Informe o coeficiente angular da equação (a): "))
b = float(input("Informe o coeficiente linear da equação (b): "))
c = float(input("Informe o coeficiente livre da equação (c): "))

funcaoSegundoGrau(a, b, c)
graficoFuncao(a, b, c)