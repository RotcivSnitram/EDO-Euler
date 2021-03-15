'''
Documentação:
Programa que calcula EDO de primeira ordem pelo método de Euler 

Ao digitar o comando no terminal deve-se colocar:
python (ou python3) nomedoarquivo.py 'equação x(t)' t_inicial t_final x(0) número_de_pontos
'''

# Biblioteca
import numpy as np
import math
import sys
import matplotlib.pyplot as plt

# Funções
def funcaoderiv(x, t):
    # Documentação:
    """
    Digite em forma de string a sua função

    Parâmetros: x (array), t (array)
    Retorno: equação (array)
    """
    return eval(sys.argv[1])

def solucao(t):
    # Documentação:
    """
    Função tangente: x = tan(t)

    Parâmetros: t (array)
    Retorno: tan(t) (array)
    """
    return np.tan(t)

def Euler(f, xi, ti, tf, N):
    # Documentação:
    """
    Método de Euler para resolução numérica de EDO de primeira ordem

    Parâmetros: x (array zerado), t (array zerado), N (int), h (float)
    Retorno: x (array), t (array)
    """
    h = (t_f - t_i)/N

    for i in range(N-1):
        x[i+1] = x[i] + (funcaoderiv(x[i], t[i]))*h
        t[i+1] = t[i] + h

    return x, t

# Parâmetros
t_i = float(eval(sys.argv[2]))
t_f = float(eval(sys.argv[3]))
x_i = float(eval(sys.argv[4]))
N = int(eval(sys.argv[5]))
t = np.zeros(N)
x = np.zeros(N)

# Método de Euler
x, t = Euler(funcaoderiv, x_i, t_i, t_f, N)

# Resultado exato
xs = solucao(t)

# Gráfico da função
plt.scatter(t, x, label = 'numérico')
plt.scatter(t, xs, color = 'red', label = 'correto')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Gráfico da função tangente pelo método de Euler")
plt.legend()
plt.grid(True)
plt.show()
