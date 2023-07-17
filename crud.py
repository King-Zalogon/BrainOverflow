# Trying to create basic CRUD functions from which to work on future projects.

# Basic CRUD functions
items=[]
cart=[]

def add_item(code=int, descript=str, amount=int, price=float):
    new_item = {
        'code': code,
        'description':descript,
        'stock':amount,
        'price':price,
    }
    items.append(new_item)
    return True


def check_item(code=int):
    
    for item in items:
        if item['code'] == code:
            return item
    
    return False

    
def change_item(code=int, new_descript=str, new_amount=int, new_price=float):

    for item in items:
        if item['code'] == code:
            item['description'] = new_descript
            item['stock'] = new_amount
            item['price'] = new_price

            return True
    
    return False
    

def list_items():
    print("-"*30)
    for item in items:
        print(f'Code: {item["code"]}')
        print(f'Description: {item["description"]}')
        print(f'Stock: {item["amount"]}')
        print(f'Price: {item["price"]}')
        print("-"*30)

def delete_item(code=int):
    for item in items:
        if item['code'] == code:
            items.remove(item)
            return True

    return False


# Shopping Cart Functions

def add_to_cart(code=int, amount=int):
    return True

def remove_from_cart(code=int, amount=int):
    return True

def show_cart():
    return True

