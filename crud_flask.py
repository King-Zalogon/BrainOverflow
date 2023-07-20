import sqlite3
from flask import Flask, jsonify, request

DATABASE = 'inventory.db'

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

create_table()


