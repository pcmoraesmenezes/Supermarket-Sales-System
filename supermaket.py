from enum import Enum
from datetime import datetime


class CalculatorType(Enum):
    SIMPLE_INTEREST = 1
    COMPOUND_INTEREST = 2


class ProductDescription:
    def __init__(self, product_id, price, description):
        self.product_id = product_id
        self.price = price
        self.description = description


class Address:
    def __init__(self, street, complement, number, city, neighborhood, state, cep):
        self.street = street
        self.complement = complement
        self.number = number
        self.city = city
        self.neighborhood = neighborhood
        self.state = state
        self.cep = cep


class SalesItem:
    def __init__(self, product_description, quantity):
        self.product_description = product_description
        self.quantity = quantity

    def get_subtotal(self):
        return self.quantity * self.product_description.price

    def __str__(self):
        return f"{self.product_description.description}\t\t{self.product_description.price}\t{self.quantity}\t{self.get_subtotal()}\n"


class Payment:
    def __init__(self, provided_amount):
        self.provided_amount = provided_amount

    def __str__(self):
        return f"Provided Amount: R$ {self.provided_amount}"


class CardPayment(Payment):
    def __init__(self, provided_amount, operator, installment_quantity, calculator_type):
        super().__init__(provided_amount)
        self.operator = operator
        self.installment_quantity = installment_quantity
        self.calculator_type = calculator_type

    def simulate_installments(self, amount, installment_quantity):
        interest = self.get_interest_rate()
        amount_with_interest = self.calculator_type.calculate_amount_with_interest(amount, installment_quantity, interest)
        return amount_with_interest / installment_quantity

    def get_interest_rate(self):
        interest_rate = 0.0
        if self.installment_quantity == 2:
            interest_rate = 2.5
        elif self.installment_quantity == 3:
            interest_rate = 5.0
        return interest_rate

    def __str__(self):
        installments = self.simulate_installments(self.provided_amount, self.installment_quantity)
        return f"Payment Type: Credit Card\n{super().__str__()}\nOperator: {self.operator}\nInstallment Quantity: {self.installment_quantity}\nInstallment Value: {installments}\nCalculator Type: {self.calculator_type}\n"


class CheckPayment(Payment):
    def __init__(self, provided_amount, bank):
        super().__init__(provided_amount)
        self.bank = bank

    def __str__(self):
        return f"Payment Type: Check\nProvided Amount: R$ {self.provided_amount}\nBank: {self.bank}"


class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def __str__(self):
        return f"Payment Type: Cash\n{super().__str__()}"


class FinancialCalculator:
    def calculate_amount_with_interest(self, initial_amount, period_months, monthly_interest_rate):
        pass


class CompoundInterestCalculator(FinancialCalculator):
    def calculate_amount_with_interest(self, initial_amount, period_months, monthly_interest_rate):
        new_amount = initial_amount * (1 + monthly_interest_rate) ** period_months
        return new_amount

    def __str__(self):
        return "Compound Interest Calculator"


class SimpleInterestCalculator(FinancialCalculator):
    def calculate_amount_with_interest(self, initial_amount, period_months, monthly_interest_rate):
        total_interest = initial_amount * period_months * (monthly_interest_rate * 0.01)
        new_amount = initial_amount + total_interest
        return new_amount

    def __str__(self):
        return "Simple Interest Calculator"


class ProductCatalog:
    def __init__(self):
        self.product_descriptions = []
        self.product_descriptions_counter = 0

        # Product definitions
        d1 = ProductDescription("01", 3.75, "Chocolate Talento")
        d2 = ProductDescription("02", 1.50, "Chewing Gum Trident")
        d3 = ProductDescription("03", 2.50, "Can of Coca-Cola")
        d4 = ProductDescription("04", 2.00, "Caxambu Mineral Water")
        d5 = ProductDescription("05", 5.99, "Corona Extra Beer")
        d6 = ProductDescription("06", 2.50, "Cream Cracker Biscuit")
        d7 = ProductDescription("07", 4.50, "Condensed Milk")
        d8 = ProductDescription("08", 18.00, "Prima Qualitat Coffee")
        d9 = ProductDescription("09", 2.00, "Danette")
        d10 = ProductDescription("10", 1.00, "Bombril")

        self.product_descriptions.extend([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10])

    def get_product_description(self, id):
        for desc in self.product_descriptions:
            if desc.product_id == id:
                return desc
        raise Exception("Product description does not exist for product ", id)


class Sale:
    def __init__(self, date):
        self.sale_items = []
        self.is_complete = False
        self.date = date
        self.payment = None

    def create_sale_item(self, product_description, quantity):
        sale_item = SalesItem(product_description, quantity)
        self.sale_items.append(sale_item)

    def make_payment(self, provided_amount):
        self.payment = CashPayment(provided_amount)
        return self.calculate_change()

    def make_check_payment(self, provided_amount, bank):
        self.payment = CheckPayment(provided_amount, bank)

    def make_card_payment(self, provided_amount, operator, installment_quantity, calculator_type):
        self.payment = CardPayment(provided_amount, operator, installment_quantity, calculator_type)

    def calculate_change(self):
        return self.payment.provided_amount - self.calculate_total_sale()

    def calculate_total_sale(self):
        total_sale = 0.0
        for sale_item in self.sale_items:
            total_sale += sale_item.product_description.price * sale_item.quantity
        return total_sale

    def __str__(self):
        status = "complete" if self.is_complete else "incomplete"
        date_temp = self.date.strftime("%d/%m/%Y")
        time_temp = self.date.strftime("%H:%M:%S")
        header = f"Date: {date_temp} Time: {time_temp}\n\t\t\t\tSale Status: {status}\n\n Description\t\tUnit Price(R$)\t\tQuantity\t\tSubtotal(R$) \n"
        body = ""

        for sale_item in self.sale_items:
            body += str(sale_item)

        footer = f"Total Cash Sale (R$)\t\t\t\t\t\t\t{self.calculate_total_sale()}\n\n{str(self.payment)}"
        return header + body + footer


class CashRegister:
    def __init__(self, id):
        self.id = id
        self.sales = []
        self.catalog = ProductCatalog()

    def create_new_sale(self):
        sale = Sale(datetime.now())
        self.sales.append(sale)

    def enter_item(self, id, quantity):
        sale = self.get_current_sale()
        product_description = self.catalog.get_product_description(id)
        sale.create_sale_item(product_description, quantity)

    def finalize_sale(self):
        self.get_current_sale().is_complete = True

    def get_current_sale(self):
        if self.sales:
            return self.sales[-1]
        else:
            raise Exception("No current sales.")

    def get_catalog(self):
        return self.catalog

    def __str__(self):
        return f"Cash Register ID: {self.id}"


class Store:
    def __init__(self, name, address):
        self.name = name
        self.sales = []
        self.cash_registers = []
        self.address = address

    def add_sale(self, sale):
        self.sales.append(sale)

    def add_cash_register(self, cash_register):
        self.cash_registers.append(cash_register)

    def get_last_sale(self):
        if self.sales:
            return self.sales[-1]
        else:
            raise Exception("No registered sales.")

    def get_cash_register(self, id):
        for cash_register in self.cash_registers:
            if cash_register.id == id:
                return cash_register
        return None

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address.street}, {self.address.number}, {self.address.complement}, {self.address.neighborhood}, {self.address.city}, {self.address.state}, {self.address.cep}"


class ProductDescriptionNonexistent(Exception):
    pass


def generate_receipt(cash_register, change):
    sale = cash_register.get_current_sale()
    date_temp = sale.date.strftime("%d/%m/%Y")
    time_temp = sale.date.strftime("%H:%M:%S")
    print("")
    print("--------------------------- Good Price Supermarket ---------------------------")
    print(f"                             Cash Register: {cash_register.id}")
    print("\t\t\t\tSALES RECEIPT")
    print(f"Date: {date_temp} Time: {time_temp}")
    print(sale)
    print(f"Change...............: R$ {change}")


def main():
    address = Address("Street X", "", 5, "Alfenas", "Airport", "MG", "37130-000")
    store = Store("Good Price Supermarket", address)

    try:
        cash_register1 = CashRegister("CR01")
        store.add_cash_register(cash_register1)
        cash_register1.create_new_sale()

        product_catalog = cash_register1.get_catalog()

        cash_register1.enter_item("01", 3)
        cash_register1.enter_item("02", 2)
        cash_register1.enter_item("03", 1)

        cash_register1.finalize_sale()

        total_sale = cash_register1.get_current_sale().calculate_total_sale()
        cash_register1.get_current_sale().make_card_payment(total_sale, "American", 1, SimpleInterestCalculator())

        generate_receipt(cash_register1, 0.0)

        cash_register2 = CashRegister("CR02")
        store.add_cash_register(cash_register2)
        cash_register2.create_new_sale()

        cash_register2.enter_item("08", 3)
        cash_register2.enter_item("01", 2)
        cash_register2.enter_item("09", 1)

        cash_register2.finalize_sale()

        cash_register2.get_current_sale().make_payment(100.00)

        generate_receipt(cash_register2, 100 - cash_register2.get_current_sale().calculate_total_sale())

        cash_register3 = CashRegister("CR03")
        store.add_cash_register(cash_register3)

        cash_register3.create_new_sale()
        cash_register3.enter_item("06", 3)
        cash_register3.enter_item("07", 2)
        cash_register3.enter_item("02", 1)
        cash_register3.finalize_sale()
        cash_register3.get_current_sale().make_check_payment(cash_register3.get_current_sale().calculate_total_sale(), "Banco do Brasil")

        generate_receipt(cash_register3, 0.0)

    except ProductDescriptionNonexistent as e:
        print(e)


if __name__ == "__main__":
    main()
