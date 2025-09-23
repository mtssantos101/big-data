import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  

def gerar_grafico_livros(biblioteca):
    if not biblioteca.livros:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return
    
    titulos = [livro.titulo for livro in biblioteca.livros.values()]
    emprestimos = [livro.quantidadeDeEmprestimos for livro in biblioteca.livros.values()]

    if all(qtd == 0 for qtd in emprestimos):
        print("Nenhum livro foi emprestado ainda.")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(titulos, emprestimos, color="green", edgecolor="black")
    plt.xlabel("Livros")
    plt.ylabel("Quantidade de Empréstimos")
    plt.title("Livros Mais Emprestados")
    plt.xticks(rotation=45, ha="right")

    
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.tight_layout()
    plt.savefig('grafico.png')
    plt.show()
