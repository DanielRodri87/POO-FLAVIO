'''

 USUÁRIO:
    - Nome
    - CPF
    
 LIVRO
    - Nome
    - ISSN
    - Quantidade
    
 BIBLIOTECA
    - livros
    - emprestimos
    - usuarios
    - Usuario: Livro
    


'''
class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
class Livro:
    def __init__(self, nome, issn, quantidade):
        self.nome = nome
        self.issn = issn
        self.quantidade = quantidade
        
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []
        self.usuarios = []
        self.usuario_livro = {}
        
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
                
    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def emprestar_livro(self, source_usuario, source_livro):
        for usuario in self.usuarios:
            if usuario.nome == source_usuario:
                for livro in self.livros:
                    if livro.nome == source_livro:
                        if livro.quantidade == 0:
                            print('Livro não disponível')
                            return
                        livro.quantidade -= 1
                        self.emprestimos.append(livro)
                        self.usuario_livro[usuario] = livro
                        break
            
    def devolver_livro(self, usuario):
        livro = self.usuario_livro[usuario]
        livro.quantidade += 1
        self.emprestimos.remove(livro)
        del self.usuario_livro[usuario]
        
    def exibir_emprestados(self):
        for usuario, livro in self.usuario_livro.items():
            print(f'{usuario.nome} - {livro.nome}')
            
    def exibir_livros_disponiveis(self):
        for livro in self.livros:
            print(f'{livro.nome} - Quantidade: {livro.quantidade}')
            
    

bib = Biblioteca()

bib.adicionar_livro(Livro('Dom Casmurro', '111', 1))
bib.adicionar_livro(Livro('Laranja', '222', 2))
bib.adicionar_usuario(Usuario("Rita", "072"))
bib.adicionar_usuario(Usuario("daniel", "073"))
bib.adicionar_usuario(Usuario("selma", "074"))
bib.adicionar_usuario(Usuario("flavio", "075"))
bib.adicionar_usuario(Usuario("naldo", "076"))
bib.adicionar_usuario(Usuario("iago", "077"))


bib.emprestar_livro("Rita", "Laranja")
bib.emprestar_livro("daniel", "Laranja")
bib.emprestar_livro("selma", "Laranja")
bib.emprestar_livro("flavio", "Laranja")
bib.emprestar_livro("naldo", "Laranja")

bib.emprestar_livro("iago", "Laranja")

bib.exibir_emprestados()
