class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_info(self):
        print("Nome: " + self.nome.title())
        print("Idade: " + str(self.idade))

class Carro:
    def __init__(self, marca, modelo, ano, proprietario):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.proprietario = proprietario

    def exibir_info(self):
        '''Exibe as informações do carro incluindo as informações do proprietário'''
        lista = [self.ano, self.marca, self.modelo]
        print("Dados do Carro:")
        for item in lista:
            print(item)
        print("Dados do proprietário: ")
        self.proprietario.exibir_info()

nome1 = Pessoa('joao', 29)
carro1 = Carro('honda','civic', 2020, nome1)

carro1.exibir_info()
print()



class Livro:
    def __init__(self, titulo:str, autor:str, editora:str):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def exibir_info(self):
        '''exibe as informações do livro'''
        print("Título: " + self.titulo.title())
        print("Autor: " + self.autor.title())
        print("Editora: " + self.editora.title())

class Biblioteca:
    def __init__(self, nome:str, livros:list):
        self.nome = nome
        self.livros = livros

    def exibir_info(self):
        '''Eibe as informações da biblioteca incluindo titulos e autores dos livros'''
        print("Nome da biblioteca: " + self.nome.title())
        print("Livros: ")
        for livro in self.livros:
            print(livro.exibir_info())

livro_1 = Livro('pai rico pai pobre', 'flavio augusto', 'everest')
livro_2 = Livro('babilonia', 'pedro machado', 'oeste')
livro_3 = Livro('o velho chico', 'jose mendes', 'brasil')

acervo = [livro_1, livro_2, livro_3]

bibli = Biblioteca('granLivro', acervo)

bibli.exibir_info()
print()



class Casa:
    def __init__(self, endereco:str, valor:float):
        self.endereco = endereco
        self.valor = valor

    def exibir_info(self):
        '''exibe as informações da casa'''
        print("Endereço: " + self.endereco.title())
        print("Valor: " + str(self.valor))

class Imobiliaria:
    def __init__(self, nome:str, casas:list):
        self.nome = nome
        self.casas = casas

    def exibir_info(self):
        '''exibe o nome da empresa e dos objetos criados na classe "Casa"'''
        print("Nome da empresa: " + self.nome.title())
        for casa in self.casas:
            print("Casa disponível ")
            print(casa.exibir_info())

casa10 = Casa('rua sebastiao vilas', 144.000)
casa20 = Casa('rua benetito pereira', 210.000)

lista = [casa10, casa20]

imob = Imobiliaria('aluga valle', lista)
imob.exibir_info()
print()




class Produto:
    def __init__(self, nome:str, preco:float, estoque:int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def verificar_estoque(self):
        '''verifica a quantidade de estoque'''
        print("Verificando...")
        print("Esstoque atual: " + str(self.estoque))

    def atualizar_estoque(self, valor:int):
        '''atualiza o estoque com base no valor informado'''
        self.estoque = valor
        print("Atualizando estoque...")
        print("Estoque atualizado!")


class CarrinhoCompra:
    def __init__(self, itens:list):
        self.itens = itens
        self.valor_total = 0
        self.carrinho = []

    def adicionar_produto(self, item):
        self.carrinho.append(item)
        print("Produto adicionado!")
        self.valor_total += item.preco

    def remover_produto(self, item:str):
        if item in self.carrinho:
            self.carrinho.remove(item)
        print("Item removido!")
        self.valor_total -= item.preco

    def exibir_total(self):
        print("O valor total do carrinho é: " + str(self.valor_total))

    def exibir_carrinho(self):
        print("\nItens do carrinho: ")
        for item in self.carrinho:
            print(item.nome.title())




tv = Produto('televisao', 1100, 130)
teclado = Produto('teclado', 230, 23)
mesa = Produto('mesa', 540, 75)
cadeira = Produto('cadeira', 80, 20)
geladeira =Produto('geladeira', 2000, 128)

produtos = [mesa]

carrinho = CarrinhoCompra(produtos)

carrinho.exibir_total()
carrinho.adicionar_produto(mesa)
carrinho.exibir_total()
carrinho.adicionar_produto(cadeira)
carrinho.exibir_total()
carrinho.adicionar_produto(teclado)
carrinho.exibir_total()
carrinho.remover_produto(mesa)
carrinho.exibir_total()
carrinho.exibir_carrinho()



