import os

# 1 Consultar funcionalidades do módulo OS (operations systems)

# 1 - Retornar a pasta tual
print(os.getcwd())

# 2 - Listar arquivos ou pastar
print(os.listdir())

# 3 - Versão do SO
os.system('ver')

# 4 - configurações da maquina
os.system('systeminfo')

# 5 - Limpar a tela do terminal
os.system('cls')

import os


# 1 - retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas 
print(os.listdir())

# 3 - Versão da SO
os.system('ver')

# 4 - Configurações da Maquinas
os.system('systeminfo')

# 5 - Limpar a tela do terminal 
os.system('cls')

# 6 - desligar o computador
# os.system('shutdown /s')

# desliga imediatamente
# os.system('shutdown /s /t 0') 

os.system('shutdown /a')

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdown():
    os.system('shutdown /a')


