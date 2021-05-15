import os
import time

print('_______________________________________________________plx2mat_______________________________________________________')
print('Este programa converte os arquivos salvos na pasta Input files salvando os arquivos convertidos na pasta Output files.','\n')
print('Escolha a rotina desejada: ','\n',
      '1 - converter todos os dados do arquivo.','\n',
      '2 - converter somente os dados de LFP.','\n')
print('Entrando na pasta Matlab Offline Files SDK...','\n')
os.chdir("Matlab Offline Files SDK")
rotina = int(input("Digite o número da rotina escolhida: "))
print('Carregando o Matlab e executando o script de conversão...','\n')
if rotina == 1:
    os.system('matlab -batch readall')
    print('\n')
    print('Conversão realizada com sucesso!','\n')
elif rotina == 2:
    os.system('matlab -batch extract_lfp')
    print('\n')
    print('Conversão realizada com sucesso!','\n')
else:
    print('A rotina selecionada não existe, reinicie o programa.','\n')
print('\n')
print('Programa finalizado.','\n')
time.sleep(30)