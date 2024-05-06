# Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada
# pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu
# programa deve ter um menu com as seguintes funções:
# a. incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou
# mais telefones. Ela deve receber como argumentos o nome e os telefones.
# b. incluirTelefone – essa função acrescenta um telefone em um nome existente na
# agenda. Caso o nome não exista na agenda, você̂ deve perguntar se a pessoa
# deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o
# novo nome.
# c. excluirTelefone – essa função exclui um telefone de uma pessoa que já está na
# agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
# d. excluirNome – essa função exclui uma pessoa da agenda.
# e. consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.
# f. Quando o usuário digitar um número negativo o programa é encerrado


def incluirNovoNome(agenda, nome, telefones):
    agenda[nome] = telefones
    
def incluirTelefone(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        incluirNovoNome(agenda, nome, [telefone])
        
def excluirTelefone(agenda, nome, telefone):
    if nome in agenda:
        if len(agenda[nome]) > 1:
            agenda[nome].remove(telefone)
        else:
            del agenda[nome]
    else:
        print("Nome não encontrado.")
        
        
def excluirNome(agenda, nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print("Nome não encontrado.")
        
def consultarTelefone(agenda, nome):
    if nome in agenda:
        return agenda[nome]
    else:
        print("Nome não encontrado.")
        return []
    
    
    
agenda = {}

while True:
    print("1 - Incluir novo nome")
    print("2 - Incluir telefone")
    print("3 - Excluir telefone")
    print("4 - Excluir nome")
    print("5 - Consultar telefone")
    print("6 - Encerrar")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        nome = input("Digite o nome: ")
        telefones = input("Digite os telefones separados por espaço: ").split()
        incluirNovoNome(agenda, nome, telefones)
    elif opcao == 2:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        incluirTelefone(agenda, nome, telefone)
    elif opcao == 3:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        excluirTelefone(agenda, nome, telefone)
    elif opcao == 4:
        nome = input("Digite o nome: ")
        excluirNome(agenda, nome)
    elif opcao == 5:
        nome = input("Digite o nome: ")
        telefones = consultarTelefone(agenda, nome)
        print(telefones)
    elif opcao == 6:
        break
    else:
        print("Opção inválida.")