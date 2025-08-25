import math

#cuidado em manter o nome do arquivo e do import iguais
#isso pode dar erro de importação circular
#ex: se o arquivo se chamar math.py, o import math
#obs.: neste exemplo, o arquivo se chama 2-math.py, então não há problema


# 1 - acessar o numero pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o número de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondar para cima e para baixo
num = 10.4
print(math.ceil(num))  # arredonda para cima
print(math.floor(num)) # arredonda para baixo

# 4 - Fatorial de um número
num2 = int(input("Digite um número para calcular o fatorial: "))
print(math.factorial(num2))

# 5 - Potência
print(math.pow(5, 5)) # 5 elevado a 5

# 6 - Raiz quadrada
print(math.sqrt(25)) # raiz quadrada de 25

# 7 MDC - máximo divisor comum
mdc = math.gcd(20, 100) # máximo divisor comum entre 20 e 100 
print(mdc)

# 8 Logaritmo
print(math.log(10))