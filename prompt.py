#Uma lista de tarefas feita em python
#the to Do list made in python
import time

ARQUIVO = 'tarefas/lista1.txt'

#funçao listar tarefas/ function list task
def listarTarefas():
    try:
        with open(ARQUIVO, 'r') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma tarefa encontrada!!')
                time.sleep(2)
            else:
                for i, linha in enumerate(linhas):#le cada linha do arquivo/ read each line of file
                    print(f'{i+1} - {linha.strip()}')# imprime cada tarefa numerada/ print each task numbered
                
                time.sleep(5)

    except FileNotFoundError:
        print('Arquivo nao encontrado!!')
    except Exception as error:
        print(f'Ocorreu um erro: {error}')

#funçao que adiciona uma tarefa nova
#funtion that add a new task
def adicionarTarefa():
    tarefa = input('Digite a tarefa: ')
    try:
        with open(ARQUIVO, 'a') as add:
            add.write(f'[ ] {tarefa}\n')
            print('Tarefa adicionada com sucesso!!')
    except Exception as error:
        print(f'Ocorreu um erro: {error}')

#funçao que remove uma tarefa
#function that remove a task
def removerTarefa():
    try:
        listarTarefas()
        indice = int(input('Digite o numero da tarefa que deseja remover: ')) - 1
        with open(ARQUIVO, 'r') as delete:
            linhas = delete.readlines()
            if not linhas:
                print('Nenhuma tarefa encontrada!!')
                time.sleep(2)
            else:
                for i, linha in enumerate(linhas):
                    print(f'{i+1} - {linha.strip()}')

                time.sleep(5)







def home():
    #ele vai rodar enquanto o usuario nao encerrar ou escolher a 5° opçao
    #this code executed until the user exist or chooses a 5th option
    while True: 
        print('\n-----Bem-Vindo-----\n')
        print('1 - Listar Tarefas\n')
        print('2 - Adicionar tarefa\n')
        print('3 - Remover tarefa\n')
        print('4 - Marcar tarefa concluida\n')
        print('5 - Sair\n')

        opcao = input("Escolha uma opçao: ")

        try:
            if opcao == '1':
                listarTarefas()
            elif opcao == '2':
                adicionarTarefa()
            elif opcao == '3':
                removerTarefa()
            elif opcao == '4':
                marcarConcluida()
            elif opcao == '5':
                print('Saindo...')
                break
            else:
                print('Opçao invalida')
        except ValueError:
            print('Por favor, digite um numero para escolher a funçao desejada!!')
            time.sleep(2)

home()
