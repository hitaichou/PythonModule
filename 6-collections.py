""""
*****Para que serve as collections?*****
As collections são estruturas de dados especializadas que fornecem alternativas
eficientes e convenientes para armazenar e manipular dados em Python. 
Elas incluem tipos como namedtuple, deque, Counter, OrderedDict, 
defaultdict, entre outros. Cada uma dessas estruturas tem características 
específicas que as tornam úteis para diferentes cenários de programação.
Elas extendem as funcionalidades das listas, tuplas e dicionários padrão do Python,
oferecendo métodos adicionais e otimizações para operações comuns.
"""

from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Lista de Frutas (contagem)
fruits = ["Maçã", "Banana", "Laranja","Banana", "Maçã", "Pêra",
          "Tangerina", "Maçã", "Banana", "Laranja", "Uva", "Abacaxi",
          "Pêra","Uva"]
print(fruits)
print(Counter(fruits))  # Conta a ocorrência de cada fruta na lista

# 2 - Utilizando tupla nomeada (namedtuple)
game = namedtuple("Game", ["name", "price", "note"])
g1 = game("The Last of Us", 150, 9.5)
g2 = game("God of War", 120, 9.7)
print(g1)
print(g2)

# 3 - Ordenando dicionarios
students = {"Pedro": 23, "Ana": 22, "Ronaldo": 26, "Janaína": 25}
a = sorted(students.items(), key=itemgetter(0))  # Ordena por nome (chave)
print(a)

# 4 - Utilizando uma fila em ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)  # Adiciona 10 no início
print(deq)
deq.append(90)  # Adiciona 90 no final
print(deq)
deq.popleft()  # Remove o primeiro elemento
print(deq)
deq.pop()  # Remove o último elemento
print(deq)