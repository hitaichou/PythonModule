import os

#Exemplos de uso do módulo os

# 1 - retornar a pasta atual
print(os.getcwd())

# 2 - listar arquivos e pastas
print(os.listdir())

#Esses comandos abaixo executam comandos do sistema operacional
#como se estivessemos no terminal (cmd)

# 3 - versão SO
os.system('ver')

# 4 - configurações da máquina
os.system('systeminfo')

# 5 - limpar a tla do terminal
os.system('cls')

# 6 - desligar o computador
#os.system('shutdown -s') #desligar em 60 segundos por padrão #descomente para testar
#os.system('shutdown -s -t 0') #descomente para testar
#os.system('shutdown -a') #abortar o desligamento

def turn_off_one_hour():
    os.system('shutdown -s -t 3600') #desligar em 1 hora

def turn_off_half_an_hour():
    os.system('shutdown -s -t 1800') #desligar em 30 minutos
    
def cancel_turn_off():
    os.system('shutdown -a') #abortar o desligamento

cancel_turn_off()

#turn_off_one_hour()

        