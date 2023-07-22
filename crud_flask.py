import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

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
        return None

    def create_item(self, code, description, amount, price):
        existing_item = self.read_item(code)
        if existing_item:
            return jsonify({'message': 'Item already created with that code.'}), 400
        
        new_item = Item(code, description, amount, price)
        self.cursor.execute('INSERT INTO items VALUES(?, ?, ?, ?)', (code, description, amount, price))
        self.connection.commit()
        return jsonify({'message': 'Item added to inventory.'}), 200
    
    def update_item(self, code, new_description, new_amount, new_price):
        item = self.read_item(code)
        if item:
            item.update(new_description, new_amount, new_price)
            self.cursor.execute('UPDATE items SET description = ?, amount = ?, price = ? WHERE code = ?', (new_description, new_amount, new_price, code))
            self.connection.commit()
            return jsonify({'message': 'Inventory item updated'}), 200
        return jsonify({'message':'Item not found in inventory'}), 404
    
    def read_items(self):
        self.cursor.execute('SELECT * FROM items')
        rows = self.cursor.fetchall()
        items = []
        for row in rows:
            code, description, amount, price = row
            item = {'code': code, 'description': description, 'amount': amount, 'price': price}
            items.append(item)
        return jsonify(items), 200
    
    def delete_item(self, code):
        self.cursor.execute('DELETE FROM items WHERE code = ?', (code,))
        if self.cursor.rowcount > 0:
            self.connection.commit()
            return jsonify({'message': 'Item deleted from inventory'}), 200
        else:
            return jsonify({'message': 'Item not found in inventory'}), 404



class Cart:

    def __init__(self) -> None:
        self.connection = sqlite3.connect('inventory.db')
        self.cursor = self.connection.cursor()
        self.cart_items = []
    
    def add_2_cart(self, code, amount, inventory):
        item_2_add = inventory.read_item(code)
        
        if item_2_add is None:
            return jsonify({'message': 'Item not in cart'}), 404
        
        if item_2_add.amount < amount:
            return jsonify({'message': 'Not enough amount in cart'}), 400
        
        for item in self.cart_items:
            if item.code == code:
                item.amount += amount
                self.cursor.execute('UPDATE items SET amount = amount - ? WHERE code = ?', (amount, code))
                self.connection.commit()
                return jsonify({'message': 'Item added to cart'}), 200
            
        new_item = Item(code, item_2_add.description, amount, item_2_add.price)
        self.cart_items.append(new_item)
        self.cursor.execute('UPDATE items SET amount = amount - ? WHERE code = ?', (amount, code))
        self.connection.commit()
        return jsonify({'message': 'Item added to cart'}), 200

    def remove_item(self, code, amount, inventory):
        for item in self.cart_items:
            if item.code == code:
                if amount > item.amount:
                    return jsonify({'message': 'Not enough amount in cart'}), 400
                
                item.amount -= amount
                if item.amount == 0:
                    self.cart_items.remove(item)
                self.cursor.execute('UPDATE items SET amount = amount + ? WHERE code = ?', (amount, code))
                self.connection.commit()
                return jsonify({'message': 'Item removed from cart'}), 200
        return jsonify({'message': 'Item not in cart'}), 404
    
    def read_cart(self):
        cart_items = []
        for item in self.cart_items:
            item = {'code': item.code, 'description': item.description, 'amount': item.amount, 'price': item.price}
            cart_items.append(item)
        return jsonify(cart_items), 200



# ============ FLASK API CONFIG & ROUTE ============ #

web_app = Flask(__name__) # creates a new instance of this class, which becomes my web application
CORS(web_app)

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


@web_app.route('/')
def index():
    return "Inventory's API"


@web_app.route('/items', methods=['GET'])
def get_items():
    return inv.read_items()


@web_app.route('/items', methods=['POST'])
def post_item():
    code = request.json.get('code') # TODO may it was .get_json() Test this
    description = request.json.get('description')
    amount = request.json.get('amount')
    price = request.json.get('price')
    return inv.create_item(code, description, amount, price)


@web_app.route('/items/<int:code>', methods=['PUT'])
def put_item(code):
    new_description = request.json.get('description')
    new_amount = request.json.get('amount')
    new_price = request.json.get('price')
    return inv.update_item(code, new_description, new_amount, new_price)


@web_app.route('/items/<int:code>', methods=['DELETE'])
def delete_item(code):
    return inv.delete_item(code)

@web_app.route('/cart', methods=['POST'])
def post_2_cart():
    code = request.json.get('code')
    amount = request.json.get('amount')
    inventory = Inventory()
    return cart.add_2_cart(code, amount, inventory)

@web_app.route('/cart', methods=['DELETE'])
def delete_from_cart():
    code = request.json.get('code')
    amount = request.json.get('amount')
    inventory = Inventory()
    return cart.remove_item(code, amount, inventory)

@web_app.route('/cart', methods=['GET'])
def get_cart():
    return cart.read_cart()


# ============ RUN ============ #

if __name__ == '__main__':
    web_app.run()

