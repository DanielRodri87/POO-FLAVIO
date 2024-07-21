import abc

class Emprestavel(abc.ABC):
    def obter_info(self):
        pass

    def verificar_disponibilidade(self):
        pass


class Midia(abc.ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class EBook(Midia):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    def obter_info(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nFormato: {self.formato}\n"
    
    def verificar_disponibilidade(self):
        return self.disponivel
    
class AudioBook(Midia):
    def __init__(self, titulo, autor, duracao):
        super().__init__(titulo, autor)
        self.duracao = duracao

    def obter_info(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nDuração: {self.duracao}\n"
    
    def verificar_disponibilidade(self):
        return self.disponivel
    
class RevistaDigital(Midia):
    def __init__(self, titulo, edicao, ano_publicacao):
        super().__init__(titulo, "")
        self.ano_publicacao = ano_publicacao
        self.edicao = edicao

    def obter_info(self):
        return f"Título: {self.titulo}\nEdição: {self.edicao}\nAno publicação: {self.ano_publicacao}\n"
    
    def verificar_disponibilidade(self):
        return self.disponivel
    
class Impostor(Midia):
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.disponivel = True

    def obter_info(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nEditora: {self.editora}\n"
    
    def verificar_disponibilidade(self):
        return self.disponivel
    
class Biblioteca():
    def __init__(self):
        self.itens_emprestados = []

    def emprestar_midia(self, midia):
        # Verificar se o usuario pode emprestar a midia
        if isinstance(midia, Emprestavel):
            if midia.verificar_disponibilidade():
                self.itens_emprestados.append(midia)
                midia.disponivel = False
                return True, "Emprestado com sucesso"
            return False, "Midia indisponível"
        return False, "Usuário não autorizado"
        
    def devolver_midia(self, midia):
        if isinstance(midia, Emprestavel):
            if not midia.verificar_disponibilidade():
                self.itens_emprestados.remove(midia)
                midia.disponivel = True
                return True, "Devolvido com sucesso"
            return False, "Midia não foi emprestada"
        return False, "Usuário não autorizado"
    
    def listar_itens_emprestados(self):
        for item in self.itens_emprestados:
            print(item.obter_info())


# MESMOS TESTES DO PROFESSOR, MAS FIZ ALGUNS MAIS PARA COMPROVAR QUE ESTÁ RODANDO (EU ESPERO)

Emprestavel.register(EBook)
Emprestavel.register(AudioBook)
Emprestavel.register(RevistaDigital)

biblioteca = Biblioteca()

ebook1 = EBook("Python for Beginners", "John Smith", "PDF")
audiobook1 = AudioBook("The Hobbit", "J.R.R Tolkien", 360)
revista1 = RevistaDigital("National Geographic", 150, 2020)
livro1 = Impostor("Recusa", "Recusa da silva", "Recusa")

retorno = biblioteca.emprestar_midia(ebook1)
print(retorno[1])
retorno = biblioteca.emprestar_midia(ebook1)
print(retorno[1])
retorno = biblioteca.emprestar_midia(audiobook1)
print(retorno[1])
retorno = biblioteca.emprestar_midia(revista1)
print(retorno[1])
retorno = biblioteca.emprestar_midia(livro1)
print(retorno[1])

print("\nItens emprestados TESTE 1:")
biblioteca.listar_itens_emprestados()

retorno = biblioteca.devolver_midia(ebook1)
print(retorno[1])
retorno = biblioteca.devolver_midia(ebook1)
print(retorno[1])

print("\nItens emprestados TESTE 2:")
biblioteca.listar_itens_emprestados()