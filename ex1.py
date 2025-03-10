##Você está desenvolvendo um sistema para uma empresa de logística que precisa gerenciar a entrega
##de pacotes. Cada pacote tem um código único, um destino (cidade) e um peso (em kg). Os pacotes
##são organizados em um dicionário onde:
##• A chave é o código do pacote (string).
##• O valor é uma tupla contendo (cidade_destino, peso).
##O programa deve fornecer as seguintes funcionalidades por meio de um menu de opções para o
##usuário da aplicação.
##a) Adicionar um novo pacote: O usuário informa o código do pacote, a cidade de destino e o peso.
##O código do pacote não pode se repetir.
##b) Remover um pacote: O usuário informa o código do pacote e ele deve ser removido da lista de
##entregas.
##c) Exibir os três pacotes mais pesados: Exibir uma lista dos três pacotes com maior peso.
##d) Calcular o peso médio dos pacotes enviados para uma cidade específica: O usuário informa a
##cidade, e o programa retorna a média do peso dos pacotes enviados para essa cidade.
##e) Listar as três cidades com maior número de pacotes enviados: Exibir as cidades que mais recebem
##pacotes ordenadas pela quantidade

def adicionapacote(pacotes):
    codigo = input("Qual o codigo do pacote? ")
    if codigo in pacotes:
        print("codigo ja existe")
        return
    cidade = input("Qual o destino? ")
    peso = float(input("qual o peso? "))
    pacotes[codigo] = (cidade, peso)
    print("Pacote adicionado")

def removepacote(pacotes):
    codigo = input("qual pacote deseja remover? ")
    if codigo in pacotes:
        novodic = {}
        for chave in pacotes:
            if chave != codigo:
                novodic[chave] = pacotes[chave]
        pacotes.clear()
        pacotes.update(novodic)
        print("Pacote removido")
    else:
        print("Codigo nao encontrado")

def tresmaispesados(pacotes):
    if len(pacotes) == 0:
        print("Nenhum pacote encontrado")
        return
    pacotesordenados = []
    for chave in pacotes:
        pacotesordenados.append((chave, pacotes[chave][0], pacotes[chave][1]))
    for i in range(len(pacotesordenados)):
        for j in range(i + 1, len(pacotesordenados)):
            if pacotesordenados[i][2] < pacotesordenados[j][2]:
                pacotesordenados[i], pacotesordenados[j] = pacotesordenados[j], pacotesordenados[i]
    print("os tres pacotes mais pesados são:")
    for i in range(min(3, len(pacotesordenados))):
        print("Codigo:", pacotesordenados[i][0], "Cidde:", pacotesordenados[i][1], "Peso:", pacotesordenados[i][2], "kg")

def pesomedio(pacotes):
    cidade = input("qual cidade pro peso medio? ")
    somapesos = 0
    quantidade = 0
    for chave in pacotes:
        if pacotes[chave][0] == cidade:
            somapesos += pacotes[chave][1]
            quantidade += 1
    if quantidade > 0:
        media = somapesos / quantidade
        print("Peso medio de pacote para", cidade, "é", round(media, 2), "kg")
    else:
        print("Nao tem pacotes para essa cidade")

def cidademaispacote(pacotes):
    contagem = {}
    for chave in pacotes:
        cidade = pacotes[chave][0]
        if cidade in contagem:
            contagem[cidade] += 1
        else:
            contagem[cidade] = 1
    cidadesordenadas = []
    for cidade in contagem:
        cidadesordenadas.append((cidade, contagem[cidade]))
    for i in range(len(cidadesordenadas)):
        for j in range(i + 1, len(cidadesordenadas)):
            if cidadesordenadas[i][1] < cidadesordenadas[j][1]:
                cidadesordenadas[i], cidadesordenadas[j] = cidadesordenadas[j], cidadesordenadas[i]
    print("essas sao as tres cidades com mais pacotes:")
    for i in range(min(3, len(cidadesordenadas))):
        print(cidadesordenadas[i][0], "-", cidadesordenadas[i][1], "pacotes")

def menu():
    pacotes = {}
    while True:
        print("Menu:")
        print("1 Adicionar pacote")
        print("2 Remover pacote")
        print("3 Exibir tres pacotes mais pesados")
        print("4 Calcular peso médio para uma cidade")
        print("5 Listar tres cidades com mais pacotes")
        print("6 Sair")
        opcao = input(" o que deseja fazer? ")
        if opcao == '1':
            adicionapacote(pacotes)
        elif opcao == '2':
            removepacote(pacotes)
        elif opcao == '3':
            tresmaispesados(pacotes)
        elif opcao == '4':
            pesomedio(pacotes)
        elif opcao == '5':
            cidademaispacote(pacotes)
        elif opcao == '6':
            print("Saindo")
            break
        else:
            print("opçao invalida")

if __name__ == "__main__":
    menu()