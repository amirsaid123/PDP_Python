customers: list['CustomerInfo'] = []
class CustomerInfo:
    def __init__(self, name, company, email, password, balance):
        self.name = name
        self.company = company
        self.email = email
        self.password = password
        self.balance = balance

    def return_info(self):
        text = f"""
        Name : {self.name}
        Company : {self.company}
        Email : {self.email}
        Password : {self.password}
        Balance : {self.balance}
        """
        print(text)

    def sign_up(self):
        customers.append(self)



tarif_list: list['Tarif'] = []

class Tarif:
    def __init__(self, name, time, space, ram, domain, support, price):
        self.name = name
        self.time = time
        self.space = space
        self.ram = ram
        self.domain = domain
        self.support = support
        self.price = price

    def return_info(self):
        text = f"""
        Name : {self.name}
        Time : {self.time}
        Space : {self.space}
        RAM : {self.ram}
        Domain : {self.domain}
        Support : {self.support}
        Price : {self.price} 
        """
        print(text)

    def add_to_list(self):
        tarif_list.append(self)


c1 = CustomerInfo("Amirsaid", "PDP", "amirsaid@gmail.com", "1234", "1000$")
c1.sign_up()

t1 = Tarif("Starter", "monthly", "5GB", "1GB", "5 domains", "24/7 support", "10.99$")
t2 = Tarif("Basic", "monthly", "10GB", "4GB", "10 domains", "24/7 support", "19.99$")
t3 = Tarif("Business", "monthly", "20GB", "8GB", "15 domains", "24/7 support", "29.99$")
t4 = Tarif("Ultra", "monthly", "50GB", "16GB", "25 domains", "24/7 support", "69.99$")

t1.add_to_list()
t2.add_to_list()
t3.add_to_list()
t4.add_to_list()

c1.return_info()

t4.return_info()

