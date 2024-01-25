from tkinter import Tk, Label, Button, simpledialog, messagebox, ttk
from enum import Enum
from datetime import datetime


class CalculatorType(Enum):
    SIMPLE_INTEREST = 1
    COMPOUND_INTEREST = 2


class ProductDescription:
    def __init__(self, id, price, description):
        self.id = id
        self.price = price
        self.description = description


class Address:
    def __init__(self, street, complement, number, city, district, state, zip_code):
        self.street = street
        self.complement = complement
        self.number = number
        self.city = city
        self.district = district
        self.state = state
        self.zip_code = zip_code


class SalesItem:
    def __init__(self, product_description, quantity):
        self.product_description = product_description
        self.quantity = quantity

    def get_subtotal(self):
        return self.quantity * self.product_description.price

    def __str__(self):
        return (
            f"{self.product_description.description}\t\t"
            f"{self.product_description.price}\t"
            f"{self.quantity}\t{self.get_subtotal()}\n"
        )


class Payment:
    def __init__(self, provided_amount):
        self.provided_amount = provided_amount

    def __str__(self):
        return f"Provided Amount: $ {self.provided_amount}"


class CardPayment(Payment):
    def __init__(self, provided_amount, operator, installment_quantity, calculator_type):
        super().__init__(provided_amount)
        self.operator = operator
        self.installment_quantity = installment_quantity
        self.calculator_type = calculator_type

    def simulate_installments(self, amount, installment_quantity):
        interest_rate = self.get_interest_rate()
        amount_with_interest = self.calculator_type.calculate_amount_with_interest(
            amount, installment_quantity, interest_rate)
        return amount_with_interest / installment_quantity

    def get_interest_rate(self):
        interest_rate = 0.0
        if self.installment_quantity == 2:
            interest_rate = 2.5
        elif self.installment_quantity == 3:
            interest_rate = 5.0
        return interest_rate

    def __str__(self):
        installments_value = self.simulate_installments(
            self.provided_amount, self.installment_quantity)

        return (
            f"Payment Type............: Credit Card\n"
            f"{super().__str__()}\nOperator................: {self.operator}\n"
            f"Installment Quantity......: {self.installment_quantity}\n"
            f"Value of Each Installment.: {installments_value}\n"
            f"Calculator Type Used in Transaction..............: {self.calculator_type}\n"
        )


class CheckPayment(Payment):
    def __init__(self, provided_amount, bank):
        super().__init__(provided_amount)
        self.bank = bank

    def __str__(self):
        return (f"Payment Type............: Check\n"
                f"Provided Amount.........: $ {self.provided_amount}\n"
                f"Bank.....................: {self.bank}")


class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def __str__(self):
        return f"Payment Type............: Cash\n{super().__str__()}"


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
        self.product_counter = 0

        d1 = ProductDescription("01", 3.75, "Chocolate Talento")
        d2 = ProductDescription("02", 1.50, "Chiclete Trident")
        d3 = ProductDescription("03", 2.50, "Lata de Coca-cola")
        d4 = ProductDescription("04", 2.00, "Agua Mineral Caxambu")
        d5 = ProductDescription("05", 5.99, "Cerveja Corona extra")
        d6 = ProductDescription("06", 2.50, "Biscoito cream cracker")
        d7 = ProductDescription("07", 4.50, "Leite condensado")
        d8 = ProductDescription("08", 18.00, "Cafe Prima Qualitat")
        d9 = ProductDescription("09", 2.00, "Danete")
        d10 = ProductDescription("10", 1.00, "Bombril")

        self.product_descriptions.extend([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10])

    def get_product_description(self, id):
        for desc in self.product_descriptions:
            if desc.id == id:
                return desc
        raise Exception("Description does not exist for product ", id)


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
        header = f"Date: {date_temp} time: {time_temp}\n\t\t\t\tSale status: {status}\n\n Description\t\tUnit Price(R$)\t\tQuantity\t\tSubtotal(R$) \n"
        body = ""

        for sale_item in self.sale_items:
            body += str(sale_item)

        footer = f"Total cash (R$)\t\t\t\t\t\t\t{self.calculate_total_sale()}\n\n{str(self.payment)}"
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
        description_product = self.catalog.get_product_description(id)
        sale.create_sale_item(description_product, quantity)

    def finish_sale(self):
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
        return (f"Name: {self.name}\nAddress: {self.address.street}, {self.address.number}, {self.address.complement}, "
                f"{self.address.district}, {self.address.city}, {self.address.state}, {self.address.zip_code}")


class NonexistentProductDescription(Exception):
    pass


def generate_receipt(cash_register, change):
    sale = cash_register.get_current_sale()
    date_temp = sale.date.strftime("%d/%m/%Y")
    time_temp = sale.date.strftime("%H:%M:%S")
    print("")
    print("--------------------------- Good Price Supermarket ---------------------------")
    print(f"                             Cash Register: {cash_register.id}")
    print("\t\t\t\tSALES RECEIPT")
    print(f"Date: {date_temp} time: {time_temp}")
    print(sale)
    print(f"Change................: R$ {change}")


class App(Tk):  # Creation of a class responsible for creating the graphical interface of the code
    def __init__(self):
        super().__init__()
        self.title("Supermarket Good Price")  # Title
        self.geometry("600x400")  # Set the window size when the program starts

        self.registrar = CashRegister("R01") 
        self.sale_in_progress = False
        self.payment_methods = ["Cash", "Check", "Credit Card"]  # Payment methods
        self.create_widgets()  # Calling the method

    def create_widgets(self):
        self.label = Label(self, text="Supermarket Good Price", font=("Arial", 16))  # Create a label widget
        self.label.pack(pady=20)  # Positioning the label, pady defines vertical space

        self.new_sale_btn = Button(self, text="New Sale", command=self.start_new_sale)  # Create a button
        self.new_sale_btn.pack(pady=10)  # Add vertical distance of 10 pixels

        self.payment_method_combobox = ttk.Combobox(self, values=self.payment_methods)
        self.payment_method_combobox.pack(pady=10) 
        self.payment_method_combobox.set(self.payment_methods[0])

        self.enter_item_btn = Button(self, text="Enter Item", command=self.enter_item)
        self.enter_item_btn.pack(pady=10)  

        self.finish_sale_btn = Button(self, text="Finish Sale", command=self.finalize_sale)
        self.finish_sale_btn.pack(pady=10)  

        self.quit_btn = Button(self, text="Quit", command=self.quit)
        self.quit_btn.pack(pady=10)  

    def start_new_sale(self):
        if self.sale_in_progress:
            messagebox.showerror("Error", "A sale is already in progress.")
            return

        self.registrar.create_new_sale()
        self.sale_in_progress = True
        messagebox.showinfo("New Sale", "A new sale has been initiated.")

    def enter_item(self):
        if not self.sale_in_progress:
            messagebox.showerror("Error", "No sale in progress.")
            return

        try:
            item_id = simpledialog.askstring("Enter Item", "Enter the product ID:")
            quantity = simpledialog.askinteger("Enter Item", "Enter the quantity:")
            self.registrar.enter_item(item_id, quantity)
            messagebox.showinfo("Item Added", "Item added to the sale.")
        except ProductDescriptionDoesNotExist as e:
            messagebox.showerror("Error", str(e))

    def finalize_sale(self):
        if not self.sale_in_progress:
            messagebox.showerror("Error", "No sale in progress.")
            return

        total_sale = self.registrar.get_current_sale().calculate_total_sale()

        selected_method = self.payment_method_combobox.get()

        if selected_method == "Cash":
            try:
                provided_amount = simpledialog.askfloat("Cash Payment", f"Total sale: $ {total_sale}\nEnter the provided amount:")
                change = self.registrar.get_current_sale().make_payment(provided_amount)
                self.registrar.get_current_sale().is_complete = True
                self.sale_in_progress = False
                generate_receipt(self.registrar, change)
                messagebox.showinfo("Sale Completed", f"Sale completed. Change: $ {change}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        elif selected_method == "Check":
            try:
                provided_amount = simpledialog.askfloat("Check Payment", f"Total sale: $ {total_sale}\nEnter the provided amount:")
                bank = simpledialog.askstring("Check Payment", "Enter the bank name:")
                self.registrar.get_current_sale().make_check_payment(provided_amount, bank)
                self.registrar.get_current_sale().is_complete = True
                self.sale_in_progress = False
                generate_receipt(self.registrar, 0.0)
                messagebox.showinfo("Sale Completed", "Sale completed. Payment by check.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        elif selected_method == "Credit Card":
            try:
                provided_amount = simpledialog.askfloat("Credit Card Payment", f"Total sale: $ {total_sale}\nEnter the provided amount:")
                operator = simpledialog.askstring("Credit Card Payment", "Enter the operator's name:")
                installment_quantity = simpledialog.askinteger("Credit Card Payment", "Enter the number of installments:")
                calculator_type = SimpleInterestCalculator()
                self.registrar.get_current_sale().make_credit_card_payment(provided_amount, operator, installment_quantity, calculator_type)
                self.registrar.get_current_sale().is_complete = True
                self.sale_in_progress = False
                generate_receipt(self.registrar, 0.0)
                messagebox.showinfo("Sale Completed", "Sale completed. Payment by credit card.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "No payment method selected.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
