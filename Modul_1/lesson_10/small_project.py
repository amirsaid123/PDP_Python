products = []
while True:
    menu = """
        1) Search 🔍
        2) Product add
        3) Product list
        4) Product update
        0) exit
        >>>"""
    key = int(input(menu))

    match key:
        case 1:
            search_val = input(">>>").lower()
            for product in products:
                if product.get("name").lower().startswith(search_val):
                    print(product)
        case 2:
            name = input("New Product name : ")
            price = float(input("New Product price : "))
            count = int(input("New Product count : "))
            d = {
                "name" : name,
                "price" : price,
                "count" : count
            }
            products.append(d)
        case 3:
            for i in products:
                print(i)
        case 4:
            i = 1
            for product in products:
                print(f"{i}) {product.get('name')}")
                i += 1
            index = int(input(">>>"))-1
            fields = """
                1) name
                2) price
                3) count
            >>>"""
            field_key = input(fields)
            new_val= input("New Value : ")
            if field_key == "1":
                products[index]["name"] = new_val
            elif field_key == "2":
                products[index]["price"] = float(new_val)
            elif field_key == "3":
                products[index]["count"] = int(new_val)


        case 0:
            break
