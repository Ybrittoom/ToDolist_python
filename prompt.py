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
        with open(ARQUIVO, 'r') as arquivo:
            tarefas = arquivo.readlines()

        if not tarefas:
            print("Nenhuma tarefa para remover.")
            return

        # Listar as tarefas com número
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa.strip()}")

        # Pedir o número da tarefa
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1

        # Verificar se o número é válido
        if indice < 0 or indice >= len(tarefas):
            print("Número inválido.")
            return

        # Remover a tarefa e salvar o arquivo novamente
        tarefa_removida = tarefas.pop(indice)

        with open(ARQUIVO, 'w') as arquivo:
            arquivo.writelines(tarefas)

        print(f"Tarefa removida: {tarefa_removida.strip()}")

    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
    except ValueError:
        print("Digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


#function mark as done
#funçao para marcar como feito
def marcarConcluida():
    try:
        with open(ARQUIVO, 'r') as arquivo:
            tarefas = arquivo.readlines()

        if not tarefas:
            print('Nenhuma tarefa para marcar como concluida')
            return
        
        for i, tarefa in enumerate(tarefas):
            print(f'{i+1} - {tarefa.strip()}')


        indice = int(input('Digite o numero da tarefa que deseja concluir: ')) -1

        if indice < 0 or indice >= len(tarefas):
            print('Numero invalido')
            return
        
        if "[x]" in tarefas[indice]:
            print('Tarefa ja esta marcada como concluida!')
            return
        
        tarefas[indice] = tarefas[indice].replace("[ ]", "[x]", 1)

        with open(ARQUIVO, 'w') as arquivo:
            arquivo.writelines(tarefas)

    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
    except ValueError:
        print("Digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        




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
