## Você foi contratado para desenvolver um sistema de atendimento de um hospital que prioriza
## pacientes de acordo com a gravidade do caso. O hospital mantém uma lista de pacientes em espera,
## onde cada paciente tem um nome e uma prioridade de atendimento. Os pacientes são classificados
## em três níveis de prioridade:
## • Emergência (E): Deve ser atendido primeiro.
## • Urgência (U): Atendido depois das emergências.
## • Normal (N): Atendido por último.
## 2
## Os pacientes são armazenados em uma lista de tuplas, onde cada tupla contém (nome_do_paciente,
## prioridade).
## O sistema deve realizar as seguintes operações por meio de um menu de opções:
## a) Adicionar um paciente na lista: O paciente é inserido no final da lista.
## b) Remover um paciente específico: O usuário informa o nome do paciente e ele é removido da lista.
## c) Chamar os 3 próximos pacientes para atendimento: O programa deve exibir os três primeiros
## pacientes da lista, priorizando primeiro Emergência (E), depois Urgência (U) e, por último, Normal
## (N). Use slices para extrair os três primeiros pacientes ordenados corretamente.
## d) Exibir os próximos N pacientes na fila: O usuário informa um número N, e o programa deve exibir
## os N primeiros pacientes na ordem de prioridade correta

def adicionapaciente(fila):
    nome = input("qual o nome do paciente? ")
    prioridade = input("qual a prioridade do paciente? (E/U/N)").upper()
    if prioridade not in ['E', 'U', 'N']:
        print("prioridade invalida")
        return
    fila.append((nome, prioridade))
    print("paciente adicionado")

def removepaciente(fila):
    nome = input("Qual paciente deseja remover? ")
    novafila = []
    encontrado = False
    for paciente in fila:
        if paciente[0] == nome:
            encontrado = True
        else:
            novafila.append(paciente)
    if encontrado:
        fila.clear()
        fila.extend(novafila)
        print("Paciente removido")
    else:
        print("Paciente inexistente")

def classificador(fila):
    emergencia = []
    urgencia = []
    normal = []
    for paciente in fila:
        if paciente[1] == 'E':
            emergencia.append(paciente)
        elif paciente[1] == 'U':
            urgencia.append(paciente)
        else:
            normal.append(paciente)
    return emergencia + urgencia + normal

def chamaprox(fila):
    if len(fila) == 0:
        print("nenhum paciente na fila")
        return
    filaorganizada = classificador(fila)
    print("Proximos pacientes esperando:")
    for i in range(min(3, len(filaorganizada))):
        print("Nome:", filaorganizada[i][0], "Prioridade:", filaorganizada[i][1])

def exiben(fila):
    if len(fila) == 0:
        print("Nenhum paciente na fila")
        return
    n = int(input("quantos pacientes? "))
    filaorganizada = classificador(fila)
    print("Proximos", n, "pacientes na fila:")
    for i in range(min(n, len(filaorganizada))):
        print("Nome:", filaorganizada[i][0], "Prioridade:", filaorganizada[i][1])

def menu():
    fila = []
    while True:
        print("Menu:")
        print("1 Adicionar um paciente")
        print("2 Remover um paciente")
        print("3 Chamar os 3 proximos pacientes")
        print("4 Exibir os proximos N pacientes")
        print("5 Sair")
        opcao = input("o que deseja fazer? ")
        if opcao == '1':
            adicionapaciente(fila)
        elif opcao == '2':
            removepaciente(fila)
        elif opcao == '3':
            chamaprox(fila)
        elif opcao == '4':
            exiben(fila)
        elif opcao == '5':
            print("Saindo")
            break
        else:
            print("Opçao invalida")

if __name__ == "__main__":
    menu()
