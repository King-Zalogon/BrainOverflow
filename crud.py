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

# add_item(1, 'first item', 9, 1.5)
# add_item(2, 'second item', 17, 2.25)

# print(check_item(2))
# print(check_item(3))
# print(check_item(1))
# change_item(1, 'first item', 6, 1.75)

# list_items()

# delete_item(1)
# add_to_cart(2, 99)
# add_to_cart(1, 4)
# add_to_cart(2, 9)


# add_to_cart(4, 4)
# remove_from_cart(1, 7)
# remove_from_cart(3, 7)
# remove_from_cart(2, 3)

# show_cart()
# list_items()

class Item:

    def __init__(self, code=int, description=str, amount=int, price=float) -> None:
        self.code = code
        self.description = description
        self.amount = amount
        self.price = price
    
    def update(self, new_description=str, new_amount=int, new_price=float):
        self.description = new_description
        self.amount = new_amount
        self.price = new_price


print("\033[H\033[J") #Cleans console/terminal screen

# item_a = Item(1, 'First item', 20, 1.99)

# print(item_a.code)
# print(item_a.description)
# print(item_a.amount)
# print(item_a.price)

# item_a.change_item(1, 'First item A', 15, 2.25)

# print(item_a.code)
# print(item_a.description)
# print(item_a.amount)
# print(item_a.price)

class Inventory:

    def __init__(self) -> None:
        self.items = []
    
    def create_item(self, code=int, description=str, amount=int, price=float):
        new_item = Item(code, description, amount, price)
        self.items.append(new_item)

    def read_item(self, code= int):
        for item in self.items:
            if item.code == code:
                return item
        return False
    
    def update_item(self, code, new_description, new_amount, new_price):
        item = self.read_item(code)
        if item:
            item.update(new_description, new_amount, new_price)

    def read_inventory(self):
        print("-"*30)
        for item in self.items:
            print(f"Code: {item.code}")
            print(f"Name: {item.description}")
            print(f"Stock: {item.amount}")
            print(f"Price: {item.price}")
            print("-"*30)
    
    def delete_item(self, code=int):
        for item in self.items:
            if item.code == code:
                self.items.remove(item)
                print('Item deleted')
                break
        else:    
            print('Item not found')



my_inventory = Inventory()
my_inventory.create_item(1, 'First Item', 10, 2.5)
my_inventory.create_item(2, 'Second Item', 20, 0.5)
my_inventory.create_item(3, 'Third Item', 15, 1.99)
my_inventory.create_item(4, 'Fourth Item', 6, 1)

# my_inventory.read_inventory()
# item = my_inventory.read_item(3)
# if item:
#     print('Item found')
#     print(f'Code: {item.code}')
#     print(f'Name: {item.description}')
#     print(f'Stock: {item.amount}')
#     print(f'Price: ${item.price}')
# else:
#     print('Item not found')

# my_inventory.update_item(4,'May the Fourth be with you', 5, 4)
# my_inventory.delete_item(6)
# my_inventory.read_inventory()

class ShopCart:

    def __init__(self) -> None:
        self.cart = []

    def create_item(self, code, amount, inventory):
        item = my_inventory.read_item(code)

        if not item:
            print('Item not found in inventory')
            return False

        if item.amount < amount:
            print('Not enough stock')
            return False
        
        for item in self.cart:
            if item.code == code:
                item.amount += amount
                item = inventory.read_item(code)
                item.update(item.description, item.amount - amount, item.price)
                return True
            
        new_item = Item(code, item.description, amount, item.price)
        self.cart.append(new_item)

        item = my_inventory.read_item(code)
        item.update(item.description, item.amount - amount, item.price)
        return True
    

    def delete_item(self, code, amount, inventory):

        for item in self.cart:
            if item.code == code:
                if amount > item.amount:
                    print('Not enough items in cart')
                    return False
                item.amount -= amount

                if item.amount == 0:
                    self.cart.remove(item)
                
                stock_item = inventory.read_item(code)
                stock_item.update(stock_item.description, stock_item.amount + amount, stock_item.price)
                return True
            
        print('Item not in cart')
        return False
    
    def read_cart(self):
        print('-'*30)
        for item in self.cart:
            print(f"Code: {item.code}")
            print(f"Name: {item.description}")
            print(f"Amount: {item.amount}")
            print(f"Price: {item.price}")
            print("-"*30)


my_inventory.read_inventory()
my_cart = ShopCart()
my_cart.create_item(1, 2, my_inventory)
my_cart.create_item(2, 5, my_inventory)
my_cart.create_item(1, 2, my_inventory)
my_cart.create_item(4, 1, my_inventory)

my_cart.read_cart()
my_inventory.read_inventory()
