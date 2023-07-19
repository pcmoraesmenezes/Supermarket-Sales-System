from enum import Enum # Modulo que permite definir um conjunto de constantes numeraveis
from datetime import datetime #Modulo que permite manipular datas e horas

class TipoCalculadora(Enum): #Definição da classe e atribuindo uma herança 'Enum'
    JUROS_SIMPLES = 1  #Constantes da enumeração, essas constantes são criadas automaticamente como atributos da classe, permitindo o acesso via TipoCalculadora.Juros_Simples
    JUROS_COMPOSTOS = 2

class DescricaoProduto: #Esse trecho de codigo está criando uma classe chama Descrição de código, essa classe recebe 3 parametros, id, preco e descrição
    #self é uma convenção para se referenciar a uma instancia
    def __init__(self, id, preco, descricao): #As funções __init__ em python são funções que são iniciadas automaticamente quando você cria um objeto do tipo da classe, então quando 
        #Criarmos um objeto do tipo DescricaoProduto, teremos que passar 3 parametros esses parametros são instanciados dentro dessa função
        self.id = id
        self.preco = preco
        self.descricao = descricao

class Endereco: #O mesmo se aplica para essa classe, temos um init e estamos inicializando as instancias
    def __init__(self, logradouro, complemento, numero, cidade, bairro, uf, cep):
        self.logradouro = logradouro
        self.complemento = complemento
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.uf = uf
        self.cep = cep

class ItemVenda:
    def __init__(self, descricao_produto, quantidade):
        self.descricao_produto = descricao_produto
        self.quantidade = quantidade

    def get_subtotal(self):
        return self.quantidade * self.descricao_produto.preco #Metodo que é responsavel por retornar a multiplicação entre a quantidade dos produtos pelo preço

    def __str__(self): # O metodo str é um metodo especial, ele retorna uma string formatada. 
        return f"{self.descricao_produto.descricao}\t\t{self.descricao_produto.preco}\t{self.quantidade}\t{self.get_subtotal()}\n" #self.descricao_produto.descricao -> Acessando o produto
    #descricao do objeto descricao_produto, retornando assim a descricao do produto. \t\tCaracter de tabulação. #self.descricao_produto.preco -> Basicamente está retornando o preco.
    #self.quantidade -> retorna a quantidade. self.get_subtotal() -> Aqui faz-se a chamada do metodo get_subtotal. 

class Pagamento:
    def __init__(self, quantia_fornecida):
        self.quantia_fornecida = quantia_fornecida

    def __str__(self):
        return f"Quantia Fornecida: R$ {self.quantia_fornecida}" #Retornando a quantia fornecida
 
class PagamentoCartao(Pagamento): #Essa classe recebe uma herança de pagamento
    def __init__(self, quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora):
        super().__init__(quantia_fornecida) #Chamando o metodo super(), basicamente esse metodo é utilizado em casos de herança, ele está assegurando que a instancia (quantia_fornecida)
        #Será inicializada corretamente
        self.operadora = operadora
        self.quantidade_parcelas = quantidade_parcelas
        self.tipo_calculadora = tipo_calculadora

    def simular_parcelas(self, quantia, quantidade_parcelas):
        juros = self.consultar_taxa_juros() #Chamada de um metodo
        montante_com_juros = self.tipo_calculadora.calcular_montante_com_juros(quantia, quantidade_parcelas, juros) 
        return montante_com_juros / quantidade_parcelas

    def consultar_taxa_juros(self): #metodo para calcular a taxa de juros
        taxa_juros = 0.0
        if self.quantidade_parcelas == 2:
            taxa_juros = 2.5
        elif self.quantidade_parcelas == 3:
            taxa_juros = 5.0
        return taxa_juros

    def __str__(self):
        parcelas = self.simular_parcelas(self.quantia_fornecida, self.quantidade_parcelas)
        return f"Tipo de pagamento...: Cartão de Crédito\n{super().__str__()}\nOperadora................: {self.operadora}\nQuantidade de parcelas....: {self.quantidade_parcelas}\nValor de cada parcela...: {parcelas}\nTipo de calculadora usada na transação................: {self.tipo_calculadora}\n"
    #Bom como dito anteriromente o metodo especial __str__ ele é responsavel por retornar uma string formatada, nesse caso ele tem o retorno de um metodo super() que como dito anteriormente
    #É um metodo especifico para casos de herança, ele está assegurando que o metodo str seja instanciado devidamente

class PagamentoCheque(Pagamento): #PagamentoCheque é uma herança de pagamento
    def __init__(self, quantia_fornecida, banco):
        super().__init__(quantia_fornecida) #Assegurando a inicialização devida da instancia quantia_fornecida
        self.banco = banco

    def __str__(self):
        return f"Tipo de pagamento...: Cheque\nQuantia fornecida....: R$ {self.quantia_fornecida}\nBanco................: {self.banco}"

class PagamentoDinheiro(Pagamento): #Mesma coisa da classe PagamentoCheque
    def __init__(self, quantia):
        super().__init__(quantia)

    def __str__(self):
        return f"Tipo de pagamento...: Dinheiro\n{super().__str__()}"

class CalculadoraFinanceira:
    def calcular_montante_com_juros(self, montante_inicial, periodo_meses, juros_ao_mes): 
        pass #Em python quando temos uma classe , instrução de controle, laços de repetição, entre outros temos que colocar algo em baixo dele ou causará erro no código
    #podemos colocar ... ou pass para evitar esse erro
    
class CalculadoraJurosCompostos(CalculadoraFinanceira):
    def calcular_montante_com_juros(self, montante_inicial, periodo_meses, juros_ao_mes):
        novo_montante = montante_inicial * (1 + juros_ao_mes) ** periodo_meses
        return novo_montante

    def __str__(self):
        return "Calculadora de juros compostos"

class CalculadoraJurosSimples(CalculadoraFinanceira):
    def calcular_montante_com_juros(self, montante_inicial, periodo_meses, juros_ao_mes):
        total_juros = montante_inicial * periodo_meses * (juros_ao_mes * 0.01)
        novo_montante = montante_inicial + total_juros
        return novo_montante

    def __str__(self):
        return "Calculadora de juros simples"

class CatalogoProdutos: #Criação de uma classe que terá os produtos
    def __init__(self):
        self.descricoes_produtos = [] # lista que receberá as descrições dos produtos
        self.contador_descricoes_produtos = 0
 
        #Definição dos produtos
        d1 = DescricaoProduto("01", 3.75, "Chocolate Talento")
        d2 = DescricaoProduto("02", 1.50, "Chiclete Trident")
        d3 = DescricaoProduto("03", 2.50, "Lata de Coca-cola")
        d4 = DescricaoProduto("04", 2.00, "Agua Mineral Caxambu")
        d5 = DescricaoProduto("05", 5.99, "Cerveja Corona extra")
        d6 = DescricaoProduto("06", 2.50, "Biscoito cream cracker")
        d7 = DescricaoProduto("07", 4.50, "Leite condensado")
        d8 = DescricaoProduto("08", 18.00, "Cafe Prima Qualitat")
        d9 = DescricaoProduto("09", 2.00, "Danete")
        d10 = DescricaoProduto("10", 1.00, "Bombril")

        self.descricoes_produtos.extend([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]) #.extends é uma função responsavel por adicionar multiplos elementos a uma lista

    def get_descricao_produto(self, id):
        for desc in self.descricoes_produtos:
            if desc.id == id:
                return desc
        raise Exception("Descricao Inexistente para o produto ", id) # Bom esse raise em python tem uma função muito interessante, ele é utilizado para gerar erros no código, sim, é uma 
    #função que gera erros no código, ela também pode ser utilizada para tratar exceções se utilizada juntamente com o try/except, mas nesse caso é para caso tente acessar um produto
    #que não exista, ai ele irá levantar um erro

class Venda:
    def __init__(self, data):
        self.itens_venda = []
        self.esta_completa = False
        self.data = data
        self.pagamento = None

    def criar_item_venda(self, descricao_produto, quantidade):
        item_venda = ItemVenda(descricao_produto, quantidade)
        self.itens_venda.append(item_venda) #.append é para adicionar um elemento a uma lista

    def fazer_pagamento(self, quantia_fornecida):
        self.pagamento = PagamentoDinheiro(quantia_fornecida)
        return self.calcular_troco()

    def fazer_pagamento_cheque(self, quantia_fornecida, banco):
        self.pagamento = PagamentoCheque(quantia_fornecida, banco)

    def fazer_pagamento_cartao(self, quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora):
        self.pagamento = PagamentoCartao(quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora)

    def calcular_troco(self):
        return self.pagamento.quantia_fornecida - self.calcular_total_venda()

    def calcular_total_venda(self):
        total_venda = 0.0
        for item_venda in self.itens_venda:
            total_venda += item_venda.descricao_produto.preco * item_venda.quantidade
        return total_venda

    def __str__(self): #Mais uma vez utilizando o metodo especial __str__ dessa vez é para mostrar a hora de maneira formatada
        status = "completa" if self.esta_completa else "incompleta"
        data_temp = self.data.strftime("%d/%m/%Y")
        hora_temp = self.data.strftime("%H:%M:%S")
        cabecalho = f"Data: {data_temp} hora: {hora_temp}\n\t\t\t\tStatus da venda: {status}\n\n Descrição\t\tPreço Unitário(R$)\t\tQuantidade\t\tSubtotal(R$) \n"
        corpo = ""

        for item_venda in self.itens_venda:
            corpo += str(item_venda)

        rodape = f"Total à vista (R$)\t\t\t\t\t\t\t{self.calcular_total_venda()}\n\n{str(self.pagamento)}"
        return cabecalho + corpo + rodape

class Registradora:
    def __init__(self, id):
        self.id = id
        self.vendas = []
        self.catalogo = CatalogoProdutos()

    def criar_nova_venda(self):
        venda = Venda(datetime.now())
        self.vendas.append(venda)

    def entrar_item(self, id, quantidade):
        venda = self.get_venda_corrente()
        descricao_produto = self.catalogo.get_descricao_produto(id)
        venda.criar_item_venda(descricao_produto, quantidade)

    def finalizar_venda(self):
        self.get_venda_corrente().esta_completa = True

    def get_venda_corrente(self):
        if self.vendas:
            return self.vendas[-1]
        else:
            raise Exception("Não há vendas correntes.")

    def get_catalogo(self):
        return self.catalogo

    def __str__(self):
        return f"Registradora ID: {self.id}"

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.vendas = []
        self.registradoras = []
        self.endereco = endereco

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def adicionar_registradora(self, registradora):
        self.registradoras.append(registradora)

    def get_ultima_venda(self):
        if self.vendas:
            return self.vendas[-1]
        else:
            raise Exception("Não há vendas registradas.")

    def get_registradora(self, id):
        for registradora in self.registradoras:
            if registradora.id == id:
                return registradora
        return None

    def __str__(self):
        return f"Nome: {self.nome}\nEndereço: {self.endereco.logradouro}, {self.endereco.numero}, {self.endereco.complemento}, {self.endereco.bairro}, {self.endereco.cidade}, {self.endereco.uf}, {self.endereco.cep}"

class DescricaoProdutoInexistente(Exception):
    pass

def gerar_recibo(registradora, troco):
    venda = registradora.get_venda_corrente()
    data_temp = venda.data.strftime("%d/%m/%Y")
    hora_temp = venda.data.strftime("%H:%M:%S")
    print("")
    print("--------------------------- Supermercado Preço Bão ---------------------------")
    print(f"                             Registradora: {registradora.id}")
    print("\t\t\t\tCUPOM FISCAL")
    print(f"Data: {data_temp} hora: {hora_temp}")
    print(venda)
    print(f"Troco................: R$ {troco}")

def main():
    endereco = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
    loja = Loja("Supermercado Preço Bão", endereco)

    try: #Try em python serve para você 'tentar algo', caso dê errado, ou resulte em um erro, você lança uma exceção(except)
        registradora1 = Registradora("R01")
        loja.adicionar_registradora(registradora1)
        registradora1.criar_nova_venda()

        catalogo = registradora1.get_catalogo()

        registradora1.entrar_item("01", 3)
        registradora1.entrar_item("02", 2)
        registradora1.entrar_item("03", 1)

        registradora1.finalizar_venda()

        total_venda = registradora1.get_venda_corrente().calcular_total_venda()
        registradora1.get_venda_corrente().fazer_pagamento_cartao(total_venda, "American", 1, CalculadoraJurosSimples())

        gerar_recibo(registradora1, 0.0)

        registradora2 = Registradora("R02")
        loja.adicionar_registradora(registradora2)
        registradora2.criar_nova_venda()

        registradora2.entrar_item("08", 3)
        registradora2.entrar_item("01", 2)
        registradora2.entrar_item("09", 1)

        registradora2.finalizar_venda()

        registradora2.get_venda_corrente().fazer_pagamento(100.00)

        gerar_recibo(registradora2, 100 - registradora2.get_venda_corrente().calcular_total_venda())

        registradora3 = Registradora("R03")
        loja.adicionar_registradora(registradora3)

        registradora3.criar_nova_venda()
        registradora3.entrar_item("06", 3)
        registradora3.entrar_item("07", 2)
        registradora3.entrar_item("02", 1)
        registradora3.finalizar_venda()
        registradora3.get_venda_corrente().fazer_pagamento_cheque(registradora3.get_venda_corrente().calcular_total_venda(), "Banco do Brasil")

        gerar_recibo(registradora3, 0.0)

    except DescricaoProdutoInexistente as e:
        print(e)

if __name__ == "__main__": #Bom, esse if serve para verificar se o código será executado no arquivo de origem, caso você importe as classes desse modulo para um outro arquivo 
    #Ele não executará o main() que está logo em baixo.
    main()
