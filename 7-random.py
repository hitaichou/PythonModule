"""
Esta biblioteca gera números ou caracteres aleatórios.
"""
import random

# 1 - Seleciona valor aleatório de uma lista
list1 = [1, 2, 3, 4, 5, 7, 8, 9]
print(random.choice(list1)) # Seleciona um valor aleatório da lista

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5,15)# Gera um número inteiro aleatório entre 5 e 15 (inclusive)
print(r1)

# 3 - Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name) # Seleciona um caractere aleatório da string
print(r2)

# 4 - Seleciona mais de um valor aleatório de uma lista
# random.sample(sequencia, tamanho)
print(random.sample(list1, 2)) # Seleciona 2 valores aleatórios da lista
print(random.sample(list1, 3)) # Seleciona 3 valores aleatórios da lista
s = "Olá mundo"
print(random.sample(s, 2)) # Seleciona 3 caracteres aleatórios da string

# 5 - Programa sorteio
done = False
while not done:
    print("O que você deseja fazer?")
    print("1 - Adivinhar um número")
    print("2 - Sair")
    
    choice = input(">: ")
    if choice == "1":
        print("=================Adivinhar o número entre 1 e 10:=================\n")
        number = int(input("Digite um número entre 1 e 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns! Você acertou!")
        else:
            print(f"Tente novamente! O número correto era {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida. Tente novamente com a opção 1 ou 2.")
    

