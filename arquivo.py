import math # Importando biblioteca para facilitar trabalho
import matplotlib.pyplot as plt # Importando para fazer o gráfico

# Função do item 1 para facilitar o código
def funcaoSegundoGrau(a, b, c):
    # Faz o delta 
    delta = (b**2)  - (4 * a * c)
    # X do vértice e Y do vértice (independente do resultado do delta)
    xv = -b/(2*a)
    print(f"O x do vértice é de {xv}")
    yv = -delta / (4*a)
    print(f"O y do vértice é de {yv}")

    #Quando delta é positivo
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        somaRaizes = x1 + x2
        produtoRaizes = x1 * x2
        print(f"O x1 vale {x1} e o x2 vale {x2}")
        print(f"A soma das raízes é de {somaRaizes}")
        print(f"O produto das raízes é de {produtoRaizes}")

    # Delta = 0
    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        print(f"As raízes são iguais valendo {x1}")

    # Delta menor que 0
    elif delta < 0:
        print(f"Não há raízes de números reais.")

# Pedindo para o usuário digitar os valores de a, b e c
a = float(input("Informe o coeficiente angular da equação (a): "))
b = float(input("Informe o coeficiente linear da equação (b): "))
c = float(input("Informe o coeficiente livre da equação (c): "))

funcaoSegundoGrau(a, b, c)