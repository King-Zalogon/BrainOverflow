import sqlite3
from flask import Flask, jsonify, request

# ============ CONSTANTS ============ #

DATABASE = 'inventory.db'


# ============ DB CONNECTION ============ #

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
    code INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    amount INTEGER NOT NULL,
    price REAL NOT NULL
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


def create_database():
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()


create_database()  # Creates table if not already exists


# ============ CLASSES ============ #

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


class Inventory:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def read_item(self, code):
        self.cursor.execute('SELECT * FROM items WHERE code = ?', (code,))
        row = self.cursor.fetchone()
        if row:
            code, description, amount, price = row
            return Item(code, description, amount, price)
        return False

    def create_item(self, code, description, amount, price):
        existing_item = self.read_item(code)
        if existing_item:
            print('Item already created with that code')
            return False
        
        new_item = Item(code, description, amount, price)
        self.cursor.execute('INSERT INTO items VALUES(?, ?, ?, ?)', (code, description, amount, price))
        self.connection.commit()
        return True
    
    def update_item(self, code, new_description, new_amount, new_price):
        item = self.read_item(code)
        if item:
            item.update(new_description, new_amount, new_price)
            self.cursor.execute('UPDATE items SET description = ?, amount = ?, price = ? WHERE code = ?', (new_description, new_amount, new_price, code))
            self.connection.commit()
    
    def read_items(self):
        print('-'*30)
        self.cursor.execute('SELECT * FROM items')
        rows = self.cursor.fetchall()
        for row in rows:
            code, description, amount, price = row
            print(f'Code: {code}')
            print(f'Name: {description}')
            print(f'Stock: {amount}')
            print(f'Price: {price}')
            print('-'*30)
    
    def delete_item(self, code):
        self.cursor.execute('DELETE FROM items WHERE code = ?', (code,))
        if self.cursor.rowcount > 0:
            print('Item deleted')
            self.connection.commit()
        else:
            print('Item not found')


class Cart:

    def __init__(self) -> None:
        self.connection = sqlite3.connect('inventory.db')
        self.cursor = self.connection.cursor()
        self.cart_items = []
    
    def add_2_cart(self, code, amount, inventory):
        add_item = inventory.read_item(code)
        
        if not add_item:
            print('Item not found')
            return False
        
        if add_item.amount < amount:
            print('Not enough stock')
            return False
        
        for item in self.cart_items:
            if item.code == code:
                item.amount += amount
                self.cursor.execute('UPDATE items SET amount = amount - ? WHERE code = ?', (amount, code))
                self.connection.commit()
                return True
            
        new_item = Item(code, add_item.description, amount, add_item.price)
        self.cart_items.append(new_item)
        self.cursor.execute('UPDATE items SET amount = amount - ? WHERE code = ?', (amount, code))
        self.connection.commit()
        return True

    def remove_item(self, code, amount):
        for item in self.cart_items:
            if item.code == code:
                if amount > item.amount:
                    print('Trying to remove more than currently on cart')
                    return False
                
                item.amount -= amount
                if item.amount == 0:
                    self.cart_items.remove(item)
                self.cursor.execute('UPDATE items SET amount = amount + ? WHERE code = ?', (amount, code))
                self.connection.commit()
                return True
        print('Item not in cart')
        return False
    
    def read_cart(self):
        print('-'*30)
        for item in self.cart_items:
            print(f'Code:{item.code}')
            print(f'Name:{item.description}')
            print(f'Amount:{item.amount}')
            print(f'Cost:{item.price}')
            print('-'*30)


# ============ FLASK API CONFIG & ROUTE ============ #

web_app = Flask(__name__) # creates a new instance of this class, which becomes my web application

cart = Cart()
inv = Inventory()

@web_app.route('/items/<int:code>', methods=['GET'])
def get_item(code):
    # inventory = Inventory()
    item = inv.read_item(code)
    if item:
        return jsonify({
            'code': item.code,
            'description': item.description,
            'amount': item.amount,
            'price': item.price
        }), 200
    return jsonify({'message': 'Item not found.'}), 404

