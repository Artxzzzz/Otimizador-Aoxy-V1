from funcoes import *
import subprocess
import os
import time


def menu():
    # Tela inicial
    print("====="*10)
    print("--------------  Otimizador AOXY  -----------------")
    print("====="*10)

    # LISTA DE FUNÇÕES
    opcoes = ['[1] ➤  Desativar recursos','[2] ➤  Desinstalar apps','[3] ➤  Atualizar Drivers',
              '[4] ➤  Limpar Arquivos Desnecessarios','[5] ➤  Recursos De Energia',
              '[6] ➤  Configurações Visuais','[7] ➤  Limpar Prefetch',
              '[8] ➤  Apps De Inicialização','[9] ➤  Monitorar Temperatura','[10] ➤  SAIR']
    for i in opcoes:
         print(i)
    print('')  

#Função principal para escolha de opções

def main():
     while True:
        os.system('cls' if os.name =='nt' else 'clear')
        
        menu()
        escolha = input('Escolha Uma Opção: ')
        if escolha == '1':
            print('1- DESATIVAR RECURSOS')
            time.sleep(2)
            desativar_recursos_func()
            
        elif escolha == '2':
           print('2- DESINSTALAR APPS')
           time.sleep(2)
           desinstalar_app_func()
           
        elif escolha == '3':
           print('3- ATUALIZAR DRIVERS')
           time.sleep(2)
           atualizar_drives_func()
           
        elif escolha == '4':   
           print('4- LIMPAR ARQUIVOS DESNECESSARIOS')
           time.sleep(5)
           limpar_arquivos_desnecessarios_func()
           
        elif escolha == '5':   
           print('5- RECURSOS DE ENERGIA')
           time.sleep(2)
           recursos_energia_func()
           
        elif escolha == '6':
           print('7- CONFIGURAÇÕES VISUAIS')
           time.sleep(2)
           configuracoes_visuais_func()
           
        elif escolha == '7':
           print('8- LIMPAR PREFETCH')
           time.sleep(2)
           limpar_prefetch_temp_func()
           
        elif escolha == '8':
           print('9- APPS DE INICIALIZAÇÃO')
           time.sleep(2)
           apps_inicializacao_func()

        elif escolha == '9': 
          print('MONITORAR TEMPERATURA')
          time.sleep(2)
          monitorar_temperatura_func()
          
        else:
          print('saindo.....')
          break

if __name__ == '__main__':
   main()  
        

