shop: list['ProductInfo'] = []
class ProductInfo:
    def __init__(self, name, price, quantity, color, quality, shape):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color
        self.quality = quality
        self.shape = shape
    def return_price(self):
        text = f"""
        Name : {self.name}
        Price : {self.price}
        Quantity : {self.quantity}
        Color: {self.color}
        Quality: {self.quality}
        Shape: {self.shape}
        """
        print(text)

    def sign_up(self):
        shop.append(self)




# name = input("Name of product: ")
# price = input("Price of product: ")
# quantity = input("Quantity of product: ")
# color = input("Color of product: ")
# quality = input("Quality of product: ")
# shape = input("Shape of product: ")




product_1 = ProductInfo("apple", "10$")
product_1.sign_up()
print(shop[0].name)




