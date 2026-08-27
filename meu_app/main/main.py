from funcoes import *
import subprocess
import os

def menu():
    # Tela inicial
    print("====="*10)
    print("--------------  Otimizador AOXY  -----------------")
    print("====="*10)

    # FUNÇÕES
    opcoes = ['[1] ➤  Desativar recursos','[2] ➤  Desintalar apps','[3] ➤  Atualizar Drivers','[4] ➤  Limpar Arquivos Desnecessarios','[5] ➤  Recursos De Energia','[6] ➤  Configurações Visuais','[7] ➤  Limpar Prefetch','[8] ➤  Apps De Inicialização','[9] ➤  Monitorar Temperatura','[10] ➤  EXIT']
    for i in opcoes:
         print(i)
    print('')  


#Função principal para escolha de opções

def main():
     while True:
        menu()
        escolha = input('Escolha Uma Opção: ')
        if escolha == '1':
            print('1- DESATIVAR RECURSOS')
            desativar_recursos_func()
            
        elif escolha == '2':
           print('2- DESINSTALAR APPS')
           desinstalar_app_func()
           
        elif escolha == '3':
           print('3- ATUALIZAR DRIVERS')
           atualizar_drives_func()
           
        elif escolha == '4':   
           print('4- LIMPAR ARQUIVOS DESNECESSARIOS')
           limpar_arquivos_desnecessarios_func()
           
        elif escolha == '5':   
           print('5- RECURSOS DE ENERGIA')
           recursos_energia_func()
           
           
        elif escolha == '6':
           print('7- CONFIGURAÇÕES VISUAIS')
           configuracoes_visuais_func()
           
        elif escolha == '7':
           print('8- LIMPAR PREFETCH')
           limpar_prefetch_temp_func()
           
        elif escolha == '8':
           print('9- APPS DE INICIALIZAÇÃO')
           apps_inicializacao_func()

        elif escolha == '9': 
          print('MONITORAR TEMPERATURA')
          monitorar_temperatura_func()
          
        else:
          print('10- EXIT')

if __name__ == '__main__':
   main()  
        

