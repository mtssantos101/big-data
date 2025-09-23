from grafico import gerar_grafico_livros

class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id = id_usuario
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}"


class Livro:
    def __init__(self, id_livro, titulo, autor):
        self.id = id_livro
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.quantidadeDeEmprestimos = 0

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Status: {status}"


class Biblioteca:
    def __init__(self):
        self.usuarios = {}
        self.livros = {}
        self.emprestimos = {}

    def gerar_id(self, entidade):
        return max(entidade.keys(), default=0) + 1

    def criar_usuario(self, nome, email):
        id_usuario = self.gerar_id(self.usuarios)
        self.usuarios[id_usuario] = Usuario(id_usuario, nome, email)
        print(f"Usuário '{nome}' criado com ID {id_usuario}.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for usuario in self.usuarios.values():
            print(usuario)

    def atualizar_usuario(self, id_usuario, novo_nome):
        if id_usuario in self.usuarios:
            self.usuarios[id_usuario].nome = novo_nome
            print("Usuário atualizado.")
        else:
            print("Usuário não encontrado.")

    def deletar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print("Usuário deletado.")
        else:
            print("Usuário não encontrado.")

    def criar_livro(self, titulo, autor):
        id_livro = self.gerar_id(self.livros)
        self.livros[id_livro] = Livro(id_livro, titulo, autor)
        print(f"Livro '{titulo}' criado com ID {id_livro}.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros.values():
            print(livro)

    def atualizar_livro(self, id_livro, novo_titulo):
        if id_livro in self.livros:
            self.livros[id_livro].titulo = novo_titulo
            print("Livro atualizado.")
        else:
            print("Livro não encontrado.")

    def deletar_livro(self, id_livro):
        if id_livro in self.livros:
            del self.livros[id_livro]
            print("Livro deletado.")
        else:
            print("Livro não encontrado.")

    def emprestar_livro(self, id_usuario, id_livro):
        if id_usuario not in self.usuarios:
            print("Usuário não existe.")
            return
        if id_livro not in self.livros:
            print("Livro não existe.")
            return
        livro = self.livros[id_livro]
        if not livro.disponivel:
            print("Livro já está emprestado.")
            return

        livro.disponivel = False
        livro.quantidadeDeEmprestimos += 1
        self.emprestimos[id_livro] = id_usuario
        print(f"Livro ID {id_livro} emprestado para usuário ID {id_usuario}.")

    def devolver_livro(self, id_livro):
        if id_livro in self.emprestimos:
            self.livros[id_livro].disponivel = True
            del self.emprestimos[id_livro]
            print(f"Livro ID {id_livro} devolvido.")
        else:
            print("Esse livro não está emprestado.")

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Nenhum livro emprestado.")
            return
        for id_livro, id_usuario in self.emprestimos.items():
            usuario = self.usuarios.get(id_usuario)
            livro = self.livros.get(id_livro)
            print(f"Livro: {livro.titulo} (ID {id_livro}) -> Usuário: {usuario.nome} (ID {id_usuario})")


def main():
    biblioteca = Biblioteca()

    biblioteca.criar_livro("Senhor dos Anéis", "J.R.R. Tolkien") 
    biblioteca.criar_livro("Dom Quixote", "Miguel de Cervantes") 
    biblioteca.criar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")  
    biblioteca.criar_livro("1984", "George Orwell")  
    biblioteca.criar_livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling") 

    biblioteca.criar_usuario("Maria", "maria@email.com")  
    biblioteca.criar_usuario("João", "joao@email.com")   
    biblioteca.criar_usuario("Ana", "ana@email.com")      

    biblioteca.emprestar_livro(1, 1)
    biblioteca.devolver_livro(1)
    biblioteca.emprestar_livro(2, 1) 
    biblioteca.devolver_livro(1)
    biblioteca.devolver_livro(1)
    biblioteca.emprestar_livro(1, 2) 
    biblioteca.devolver_livro(2)
    biblioteca.emprestar_livro(2, 3) 
    biblioteca.devolver_livro(3)
    biblioteca.emprestar_livro(3, 4) 
    biblioteca.devolver_livro(4)
    biblioteca.emprestar_livro(1, 1) 
    biblioteca.devolver_livro(1)
    biblioteca.emprestar_livro(2, 2)
    biblioteca.devolver_livro(2)
    biblioteca.emprestar_livro(3, 2)  
    biblioteca.devolver_livro(2)
    biblioteca.emprestar_livro(1, 3)
    biblioteca.devolver_livro(3)
    biblioteca.emprestar_livro(2, 4)  
    biblioteca.devolver_livro(4)
    biblioteca.emprestar_livro(3, 5) 
    biblioteca.devolver_livro(5)
    biblioteca.emprestar_livro(1, 5) 
    biblioteca.devolver_livro(5)
    biblioteca.emprestar_livro(2, 5)  
    biblioteca.devolver_livro(5)
    biblioteca.emprestar_livro(3, 5) 
    biblioteca.devolver_livro(5)

    while True:
        print("\n--- MENU ---")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Criar livro")
        print("6. Listar livros")
        print("7. Atualizar livro")
        print("8. Deletar livro")
        print("9. Emprestar livro")
        print("10. Devolver livro")
        print("11. Listar empréstimos")
        print("12. Gráfico de livros mais emprestados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            biblioteca.criar_usuario(nome, email)
        elif opcao == "2":
            biblioteca.listar_usuarios()
        elif opcao == "3":
            id_u = int(input("ID do usuário: "))
            novo_nome = input("Novo nome: ")
            biblioteca.atualizar_usuario(id_u, novo_nome)
        elif opcao == "4":
            id_u = int(input("ID do usuário: "))
            biblioteca.deletar_usuario(id_u)
        elif opcao == "5":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            biblioteca.criar_livro(titulo, autor)
        elif opcao == "6":
            biblioteca.listar_livros()
        elif opcao == "7":
            id_l = int(input("ID do livro: "))
            novo_titulo = input("Novo título: ")
            biblioteca.atualizar_livro(id_l, novo_titulo)
        elif opcao == "8":
            id_l = int(input("ID do livro: "))
            biblioteca.deletar_livro(id_l)
        elif opcao == "9":
            id_u = int(input("ID do usuário: "))
            id_l = int(input("ID do livro: "))
            biblioteca.emprestar_livro(id_u, id_l)
        elif opcao == "10":
            id_l = int(input("ID do livro: "))
            biblioteca.devolver_livro(id_l)
        elif opcao == "11":
            biblioteca.listar_emprestimos()
        elif opcao == '12':
            gerar_grafico_livros(biblioteca)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
