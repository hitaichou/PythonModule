#Criptografia de textos com hashlib

"""
Hashlib é uma biblioteca nativa do Python que implementa algoritmos 
de hash seguros e rápidos. Ela fornece uma maneira simples de criar 
resumos criptográficos de dados, o que é útil para garantir a integridade 
dos dados, autenticação e armazenamento seguro de senhas entre outras aplicações.
É importante ressaltar que há bibliotecas mais robustas e seguras para
criptografia, como a cryptography, mas o hashlib é uma boa opção nativa
para tarefas básicas de hash.
"""


import hashlib

# 1 - Verificar os algoritmos disponíveis

"""
*****Para que serve os algorítmos disponíveis?*****
Eles servem para você escolher qual o melhor algoritmo para a sua aplicação
Alguns algoritmos são mais rápidos, outros mais seguros, 
mais indicados para senhas ou ingração de dados, outros 
para grandes ou pequenos volumes
"""
print(hashlib.algorithms_available)

#2 - Verificar algoritmos de acordo com o sistema operacional
print(hashlib.algorithms_guaranteed)

# 3 - Criar um hash SHA256
algorithm = hashlib.sha256() #Escolhendo o algoritmo
print(algorithm.digest()) #Mostrando o hash vazio
message = "A melhor forma de prever o fururo é criá-lo.".encode() #Mensagem a ser criptografada
algorithm.update(message) #Atualizando o algoritmo com a mensagem
print(algorithm.hexdigest()) #Mostrando o hash da mensagem

# 4 - Utilizando o algoritmo MD5
md5 = hashlib.md5() #Escolhendo o algoritmo
md5.update(message) #Atualizando o algoritmo com a mensagem
print(md5.hexdigest()) #Mostrando o hash da mensagem

