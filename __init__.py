from time import sleep
from os import system
from platform import system as platform_system
from datetime import datetime

def identificar_sistema_operacional():
    sistema = platform_system()
    if sistema == "Windows":
        return "Windows"
    elif sistema == "Darwin":
        return "Mac"
    elif sistema == "Linux":
        return "Linux"
    else:
        return "Sistema não identificado"

def continuar():
    while True:
        continuar_s_or_n = str(input("Adicionar outro usuário?\n[1] SIM\n[2] NÃO\nResposta: ")).strip().upper()
        if continuar_s_or_n == '1' or continuar_s_or_n == 'SIM':
            sleep(0.5)
            break
        elif continuar_s_or_n == '2' or continuar_s_or_n == 'NAO' or continuar_s_or_n == 'NÃO':
            exit()
        else:
            sistema_operacional_if()
            print("Por favor, digite uma resposta válida (1/SIM ou 2/NÃO).")
            sleep(2)
            sistema_operacional_if()

def sistema_operacional_if():
    if sistema_operacional == 'Windows':
        return system('cls')
    elif sistema_operacional == 'Linux' or sistema_operacional == 'Mac':
        return system('clear')

def isalpha_para_lista(lista):
    for palavra in lista:
        if not palavra.isalpha():
            return False
    return True

sistema_operacional = identificar_sistema_operacional()
horario_atual = datetime.now()

while True: 
    sistema_operacional_if()
    print('Usuário')
    nome = str(input('Nome: ')).strip().capitalize().split()
    sobrenome = str(input('Sobrenome: ')).strip().capitalize().split()
    turma = str(input('Turma (Ex: 2D, 9E...): ')).strip().upper()
    usuario = nome[0] + sobrenome[0]
    x = isalpha_para_lista(nome)
    y = isalpha_para_lista(sobrenome)
    
    if x and y:
        pass
    else:
        print('ESTE VALOR NÃO É VÁLIDO!')
        sleep(2)
        continue 

    usuario = ' '.join(nome + sobrenome)
    with open('EBBA_BD.txt', 'r') as arquivo:
        participantes = arquivo.read()
        if usuario in participantes:
            sistema_operacional_if()
            print('Este usuário já participou da sessão.')
            sleep(2)
            sistema_operacional_if()
            break

        else:
            print('Seja bem vindo(a)!')
            with open('EBBA_BD.txt', 'a') as arquivo:
                arquivo.write(f'\n{usuario} {turma} {horario_atual}')
                sleep(2)
                sistema_operacional_if()

            separacao = list(turma)
            
            if separacao[0] == '9':
                with open('cont_9ano.txt', 'a') as arquivo2:
                    arquivo2.write(f'\n{usuario} {separacao [1]} {horario_atual}')

                if separacao[1] == 'A':
                    with open('cont_9anoA.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'B':
                    with open('cont_9anoB.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'C':
                    with open('cont_9anoC.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'D':
                    with open('cont_9anoD.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'E':
                    with open('cont_9anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'F':
                    with open('cont_9anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')

            elif separacao[0] == '1':
                with open('cont_1ano.txt', 'a') as arquivo3:
                    arquivo3.write(f'\n{usuario} {separacao [1]} {horario_atual}')
                
                if separacao[1] == 'A':
                    with open('cont_1anoA.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'B':
                    with open('cont_1anoB.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'C':
                    with open('cont_1anoC.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'D':
                    with open('cont_1anoD.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'E':
                    with open('cont_1anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'F':
                    with open('cont_1anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')

            elif separacao[0] == '2':
                with open('cont_2ano.txt', 'a') as arquivo4:
                    arquivo4.write(f'\n{usuario} {separacao [1]} {horario_atual}')

                if separacao[1] == 'A':
                    with open('cont_2anoA.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'B':
                    with open('cont_2anoB.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'C':
                    with open('cont_2anoC.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'D':
                    with open('cont_2anoD.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'E':
                    with open('cont_2anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'F':
                    with open('cont_2anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')

            elif separacao[0] == '3':
                with open('cont_3ano.txt', 'a') as arquivo5:
                    arquivo5.write(f'\n{usuario} {separacao [1]} {horario_atual}')

                if separacao[1] == 'A':
                    with open('cont_3anoA.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'B':
                    with open('cont_3anoB.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'C':
                    with open('cont_3anoC.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'D':
                    with open('cont_3anoD.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'E':
                    with open('cont_3anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
                elif separacao[1] == 'F':
                    with open('cont_3anoE.txt', 'a') as arquivo2:
                        arquivo2.write(f'\n{usuario} {horario_atual}')
    continuar()
