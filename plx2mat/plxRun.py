import os
import time

print('Este programa converte os arquivos salvos na pasta Input files salvando os arquivos convertidos na pasta Output files')
print('Entrando na pasta Matlab Offline Files SDK')
os.chdir('Matlab Offline Files SDK')
print('Carregando o Matlab e executando o script de conversão')
os.system('matlab -batch readall')
print('programa finalizado!!')
time.sleep(20)
