import time
from queue import PriorityQueue
from colorama import init, Fore, Style

init()

class Tarefa:
    def __init__(self, nome, prazo, duracao):
        # Inicializa uma nova tarefa com nome, prazo e duração
        self.nome = nome
        self.prazo_original = prazo
        self.prazo = prazo
        self.duracao = duracao
        self.restante = duracao

    def __lt__(self, other):
        # Define a comparação entre tarefas com base no prazo
        return self.prazo < other.prazo

    def __repr__(self):
        # Representação textual da tarefa
        return f"Tarefa(nome={self.nome}, prazo={self.prazo}, duracao={self.duracao})"

def mostrar_estado(tempo_atual, fila, tarefa_atual):
    # Mostra o estado atual do escalonador
    print("===========================================================")
    print(f"{Fore.CYAN}Tempo atual: {tempo_atual}{Style.RESET_ALL}")
    print("Tarefas na fila:")
    
    if fila.empty():
        # Mostra mensagem se a fila está vazia
        print("    Nenhuma tarefa na fila")
    else:
        # Lista todas as tarefas na fila
        for i, (_, tarefa) in enumerate(fila.queue, start=1):
            print(f"    {i}. {tarefa.nome} (Prazo: {tarefa.prazo}, Duração: {tarefa.duracao})")
    
    if tarefa_atual:
        # Mostra a tarefa atualmente em execução
        print(f"Tarefa em execução: {tarefa_atual.nome} (Prazo: {tarefa_atual.prazo}, Restante: {tarefa_atual.restante})")
    else:
        # Mensagem se nenhuma tarefa está em execução
        print("Nenhuma tarefa em execução")
    print("===========================================================")

def escalonador_edf():
    fila = PriorityQueue()  # Cria uma fila de prioridades
    tempo_atual = 0

    print("===========================================================")
    num_tarefas = int(input(f"{Fore.YELLOW}Digite o número de tarefas: {Style.RESET_ALL}"))
    print("===========================================================")
    
    for i in range(num_tarefas):
        # Coleta os detalhes de cada tarefa do usuário
        print("===========================================================")
        nome = input(f"{Fore.YELLOW}Digite o nome da Tarefa {i+1}: {Style.RESET_ALL}")
        prazo = int(input(f"{Fore.YELLOW}Digite o prazo da Tarefa {i+1}: {Style.RESET_ALL}"))
        duracao = int(input(f"{Fore.YELLOW}Digite a duração da Tarefa {i+1}: {Style.RESET_ALL}"))
        print("===========================================================")
        
        # Cria e adiciona a nova tarefa à fila
        tarefa = Tarefa(nome, prazo, duracao)
        fila.put((prazo, tarefa))
    
    tarefa_atual = None  # Nenhuma tarefa em execução no início

    while not fila.empty() or tarefa_atual:
        if not tarefa_atual and not fila.empty():
            # Se nenhuma tarefa está em execução, pega a próxima tarefa da fila
            _, tarefa_atual = fila.get()
        
        if tarefa_atual:
            # Executa a tarefa atual
            print(f"{Fore.GREEN}Tempo atual: {tempo_atual}")
            print(f"Executando => {tarefa_atual.nome} (Prazo: {tarefa_atual.prazo}, Restante: {tarefa_atual.restante}){Style.RESET_ALL}")
            tarefa_atual.restante -= 1
            time.sleep(0.5)  # Simula a execução da tarefa por um tempo
            
            if tarefa_atual.restante == 0:
                # Se a tarefa atual está concluída, remove-a
                print(f"{Fore.RED}Tarefa {tarefa_atual.nome} concluída{Style.RESET_ALL}")
                tarefa_atual = None

        # Mostra o estado atual do escalonador
        mostrar_estado(tempo_atual, fila, tarefa_atual)
        tempo_atual += 1  # Incrementa o tempo atual

# Executa o escalonador EDF
escalonador_edf()
