# Trying to create basic CRUD functions from which to work on future projects.

# Basic CRUD functions
items=[]
cart=[]

def add_item(code=int, descript=str, amount=int, price=float):
    new_item = {
        'code': code,
        'description':descript,
        'amount':amount,
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
            item['amount'] = new_amount
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

    current_item = check_item(code)
    if current_item is False:
        print("No item found in items")
        return False
    
    if current_item['amount'] < amount:
        print('Not enough stock of that item')
        return False
    
    for item in items:
        if item['code'] == code:
            item['amount'] -= amount
    
    for added_item in cart:
        if added_item['code'] == code:
            added_item['amount'] += amount
            return
        
    new_item = {
        'code': code,
        'description': item['description'],
        'amount': amount,
        'price': item['price']
    }

    cart.append(new_item)
    return True


def remove_from_cart(code=int, amount=int):
    
    for item in cart:
        if item['code'] == code:
            if item['amount'] < amount:
                print('Trying to remove more items than currently on cart')
                return False
            
            item['amount'] -= amount

            current_item = check_item(code)
            change_item(code, current_item['description'], current_item['amount'] + amount, current_item['price'])

            if item['amount'] == 0:
                cart.remove(item)

            return True
    
    print('No such item in shopping cart')
    return False

def show_cart():
    print("-"*30)
    total = 0

    for item in cart:
        print(f'Code: {item["code"]} - {item["description"]}')
        print(f'Price: {item["price"]} - Ampount: {item["amount"]}')
        sub_total = item['price'] * item['amount']
        total += sub_total
        print(f'Estimated cost: {sub_total}')
        print("-"*30)
    print(f'Total purchase cost: {total}')
    print("-"*30)
    return True

# Tests

add_item(1, 'first item', 9, 1.5)
add_item(2, 'second item', 17, 2.25)

# print(check_item(2))
# print(check_item(3))
# print(check_item(1))
# change_item(1, 'first item', 6, 1.75)

list_items()

# delete_item(1)
# add_to_cart(2, 99)
add_to_cart(1, 4)
add_to_cart(2, 9)


# add_to_cart(4, 4)
# remove_from_cart(1, 7)
# remove_from_cart(3, 7)
# remove_from_cart(2, 3)

show_cart()
list_items()

class Item:

    def __init__(self, code=int, description=str, amount=int, price=float) -> None:
        self.code = code
        self.description = description
        self.amount = amount
        self.price = price
    
    def change_item(self, code=int, new_description=str, new_amount=int, new_price=float):
        self.description = new_description
        self.amount = new_amount
        self.price = new_price


print("\033[H\033[J") #Cleans console/terminal screen

item_a = Item(1, 'First item', 20, 1.99)

print(item_a.code)
print(item_a.description)
print(item_a.amount)
print(item_a.price)

item_a.change_item(1, 'First item A', 15, 2.25)

print(item_a.code)
print(item_a.description)
print(item_a.amount)
print(item_a.price)