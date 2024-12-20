customers: list['CustomerInfo'] = []

class CustomerInfo:
    def __init__(self, name, company, email, password):
        self.name = name
        self.company = company
        self.email = email
        self.password = password

    def return_info(self):
        text = f"""
        Name : {self.name}
        Company : {self.company}
        Email : {self.email}
        Password : {self.password}
        """
        print(text)

    def sign_up(self):
        customers.append(self)



name = input("Enter your name: ")
company = input("Enter your company: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

customer = CustomerInfo(name, company, email, password)
customer.sign_up()
print(customers[0].password)


