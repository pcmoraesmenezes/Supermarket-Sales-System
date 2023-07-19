from tkinter import *  #Importando todas as classes, funções e objetos do modulo tkinter
from tkinter import simpledialog, messagebox #Importa especificadamente as classes simpledialog e messagebox
from tkinter import ttk #Importa o modulo ttk do tkinter
from enum import Enum
from datetime import datetime

class TipoCalculadora(Enum):
    JUROS_SIMPLES = 1
    JUROS_COMPOSTOS = 2

class DescricaoProduto:
    def __init__(self, id, preco, descricao):
        self.id = id
        self.preco = preco
        self.descricao = descricao

class Endereco:
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
        return self.quantidade * self.descricao_produto.preco

    def __str__(self):
        return f"{self.descricao_produto.descricao}\t\t{self.descricao_produto.preco}\t{self.quantidade}\t{self.get_subtotal()}\n"

class Pagamento:
    def __init__(self, quantia_fornecida):
        self.quantia_fornecida = quantia_fornecida

    def __str__(self):
        return f"Quantia Fornecida: R$ {self.quantia_fornecida}"

class PagamentoCartao(Pagamento):
    def __init__(self, quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora):
        super().__init__(quantia_fornecida)
        self.operadora = operadora
        self.quantidade_parcelas = quantidade_parcelas
        self.tipo_calculadora = tipo_calculadora

    def simular_parcelas(self, quantia, quantidade_parcelas):
        juros = self.consultar_taxa_juros()
        montante_com_juros = self.tipo_calculadora.calcular_montante_com_juros(quantia, quantidade_parcelas, juros)
        return montante_com_juros / quantidade_parcelas

    def consultar_taxa_juros(self):
        taxa_juros = 0.0
        if self.quantidade_parcelas == 2:
            taxa_juros = 2.5
        elif self.quantidade_parcelas == 3:
            taxa_juros = 5.0
        return taxa_juros

    def __str__(self):
        parcelas = self.simular_parcelas(self.quantia_fornecida, self.quantidade_parcelas)
        return f"Tipo de pagamento...: Cartão de Crédito\n{super().__str__()}\nOperadora................: {self.operadora}\nQuantidade de parcelas....: {self.quantidade_parcelas}\nValor de cada parcela...: {parcelas}\nTipo de calculadora usada na transação................: {self.tipo_calculadora}\n"

class PagamentoCheque(Pagamento):
    def __init__(self, quantia_fornecida, banco):
        super().__init__(quantia_fornecida)
        self.banco = banco

    def __str__(self):
        return f"Tipo de pagamento...: Cheque\nQuantia fornecida....: R$ {self.quantia_fornecida}\nBanco................: {self.banco}"

class PagamentoDinheiro(Pagamento):
    def __init__(self, quantia):
        super().__init__(quantia)

    def __str__(self):
        return f"Tipo de pagamento...: Dinheiro\n{super().__str__()}"

class CalculadoraFinanceira:
    def calcular_montante_com_juros(self, montante_inicial, periodo_meses, juros_ao_mes):
        pass

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

class CatalogoProdutos:
    def __init__(self):
        self.descricoes_produtos = []
        self.contador_descricoes_produtos = 0

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

        self.descricoes_produtos.extend([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10])

    def get_descricao_produto(self, id):
        for desc in self.descricoes_produtos:
            if desc.id == id:
                return desc
        raise Exception("Descricao Inexistente para o produto ", id)

class Venda:
    def __init__(self, data):
        self.itens_venda = []
        self.esta_completa = False
        self.data = data
        self.pagamento = None

    def criar_item_venda(self, descricao_produto, quantidade):
        item_venda = ItemVenda(descricao_produto, quantidade)
        self.itens_venda.append(item_venda)

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

    def __str__(self):
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

class App(Tk):  #Criação de uma classe que será responsavel pela criação da interface gráfica do código
    def __init__(self):
        super().__init__()
        self.title("Supermercado Preço Bão") #Titulo
        self.geometry("600x400") #Definição do tamanho da janela ao iniciar o programa

        self.registradora = Registradora("R01") 
        self.venda_in_progress = False
        self.payment_methods = ["Dinheiro", "Cheque", "Cartão de Crédito"]  #Metodos de pagamento
        self.create_widgets() #Chamando metodo

    def create_widgets(self):
        self.label = Label(self, text="Supermercado Preço Bão", font=("Arial", 16)) #Criação de um widget do tipo label
        self.label.pack(pady=20) #Posicionando o label, o pady define um espaço vertical 

        self.new_sale_btn = Button(self, text="Nova Venda", command=self.start_new_sale) #Criando um botão
        self.new_sale_btn.pack(pady=10)  # Adicionando dsitancia vertical de 10 pixels

        self.payment_method_combobox = ttk.Combobox(self, values=self.payment_methods)
        self.payment_method_combobox.pack(pady=10) 
        self.payment_method_combobox.set(self.payment_methods[0])

        self.enter_item_btn = Button(self, text="Entrar Item", command=self.enter_item)
        self.enter_item_btn.pack(pady=10)  

        self.finish_sale_btn = Button(self, text="Finalizar Venda", command=self.finalize_sale)
        self.finish_sale_btn.pack(pady=10)  

        self.quit_btn = Button(self, text="Sair", command=self.quit)
        self.quit_btn.pack(pady=10)  
    def start_new_sale(self):
        if self.venda_in_progress:
            messagebox.showerror("Erro", "Uma venda já está em progresso.")
            return

        self.registradora.criar_nova_venda()
        self.venda_in_progress = True
        messagebox.showinfo("Nova Venda", "Uma nova venda foi iniciada.")

    def enter_item(self):
        if not self.venda_in_progress:
            messagebox.showerror("Erro", "Nenhuma venda em progresso.")
            return

        try:
            item_id = simpledialog.askstring("Entrar Item", "Digite o ID do produto:")
            quantity = simpledialog.askinteger("Entrar Item", "Digite a quantidade:")
            self.registradora.entrar_item(item_id, quantity)
            messagebox.showinfo("Item Adicionado", "Item adicionado à venda.")
        except DescricaoProdutoInexistente as e:
            messagebox.showerror("Erro", str(e))

    def finalize_sale(self):
        if not self.venda_in_progress:
            messagebox.showerror("Erro", "Nenhuma venda em progresso.")
            return

        total_venda = self.registradora.get_venda_corrente().calcular_total_venda()

        selected_method = self.payment_method_combobox.get()

        if selected_method == "Dinheiro":
            try:
                quantia_fornecida = simpledialog.askfloat("Pagamento em Dinheiro", f"Total da venda: R$ {total_venda}\nDigite a quantia fornecida:")
                troco = self.registradora.get_venda_corrente().fazer_pagamento(quantia_fornecida)
                self.registradora.get_venda_corrente().esta_completa = True
                self.venda_in_progress = False
                gerar_recibo(self.registradora, troco)
                messagebox.showinfo("Venda Finalizada", f"Venda finalizada. Troco: R$ {troco}")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        elif selected_method == "Cheque":
            try:
                quantia_fornecida = simpledialog.askfloat("Pagamento com Cheque", f"Total da venda: R$ {total_venda}\nDigite a quantia fornecida:")
                banco = simpledialog.askstring("Pagamento com Cheque", "Digite o nome do banco:")
                self.registradora.get_venda_corrente().fazer_pagamento_cheque(quantia_fornecida, banco)
                self.registradora.get_venda_corrente().esta_completa = True
                self.venda_in_progress = False
                gerar_recibo(self.registradora, 0.0)
                messagebox.showinfo("Venda Finalizada", "Venda finalizada. Pagamento com cheque.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        elif selected_method == "Cartão de Crédito":
            try:
                quantia_fornecida = simpledialog.askfloat("Pagamento com Cartão de Crédito", f"Total da venda: R$ {total_venda}\nDigite a quantia fornecida:")
                operadora = simpledialog.askstring("Pagamento com Cartão de Crédito", "Digite o nome da operadora:")
                quantidade_parcelas = simpledialog.askinteger("Pagamento com Cartão de Crédito", "Digite a quantidade de parcelas:")
                tipo_calculadora = CalculadoraJurosSimples()  # Use the appropriate calculator here based on user choice
                self.registradora.get_venda_corrente().fazer_pagamento_cartao(quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora)
                self.registradora.get_venda_corrente().esta_completa = True
                self.venda_in_progress = False
                gerar_recibo(self.registradora, 0.0)
                messagebox.showinfo("Venda Finalizada", "Venda finalizada. Pagamento com cartão de crédito.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showerror("Erro", "Nenhum método de pagamento selecionado.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
