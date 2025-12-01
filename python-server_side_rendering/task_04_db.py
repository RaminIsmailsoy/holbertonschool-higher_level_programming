#!/usr/bin/python3
''' Extending Dynamic Data Display to Include SQLite in Flask '''


from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# --- Database Setup Script (Run once before starting the server) ---

def create_database():
    """Creates the SQLite database and populates the Products table."""
    # Ensure the file is created in the same directory as the script
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert sample data (DELETE then INSERT to ensure fresh data if script is rerun)
    cursor.execute('DELETE FROM Products')
    cursor.executemany('''
        INSERT INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        # Add the data from Task 3's files for full testing coverage (optional, but good practice)
        (3, 'Notebook', 'Office Supplies', 5.50),
        (4, 'Webcam', 'Electronics', 49.00)
    ])

    conn.commit()
    conn.close()

# --- Helper Functions for Data Reading ---

def read_json_data(filename='products.json'):
    """Reads and parses data from a JSON file."""
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, 'r') as f:
            # Note: Assuming the JSON file is present from Task 3
            return json.load(f)
    except Exception:
        return None

def read_csv_data(filename='products.csv'):
    """Reads and parses data from a CSV file."""
    data = []
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception:
        return None
    return data

def read_sql_data(product_id=None):
    """
    Fetches data from the SQLite database.
    If product_id is provided, fetches only that product.
    """
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    products_list = []
    conn = None # Initialize connection to None
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # This allows accessing columns by name
        cursor = conn.cursor()

        if product_id is None:
            # Fetch all products
            cursor.execute("SELECT id, name, category, price FROM Products")
        else:
            # Fetch specific product by ID
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))

        # Convert sqlite3.Row objects to standard Python dictionaries
        for row in cursor.fetchall():
            products_list.append(dict(row))

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None # Return None on database error
    finally:
        if conn:
            conn.close()

    return products_list

# --- Main Route ---

@app.route('/products')
def products():
    """
    Handles data display based on 'source' (json, csv, or sql) and filters by optional 'id'.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    all_products = None

    # 1. Source Validation and Data Loading
    if source == 'json':
        all_products = read_json_data()
    elif source == 'csv':
        all_products = read_csv_data()
    elif source == 'sql':
        # The ID filtering will be handled below, so we fetch all data first (or handle filtering in read_sql_data)
        # For simplicity and consistency with other functions, we'll fetch all here and filter later.
        all_products = read_sql_data()
    else:
        # Edge Case: Invalid or missing 'source'
        return render_template('product_display.html', error="Wrong source. Must be 'json', 'csv', or 'sql'.")

    # Handle file/DB reading error
    if all_products is None:
        return render_template('product_display.html', error=f"Could not load data from {source} source (file not found or database error).")

    # Initialize the list of products to display
    display_products = all_products

    # 2. ID Filtering (if 'id' parameter is provided)
    if product_id_str:
        try:
            target_id = int(product_id_str)

            # Filter the list based on the ID
            filtered_list = [p for p in all_products if p.get('id') == target_id]

            if not filtered_list:
                # Edge Case: ID not found
                return render_template('product_display.html', error=f"Product not found. ID {target_id} does not exist in the {source} data.")

            display_products = filtered_list

        except ValueError:
            # Edge Case: Invalid ID format (not an integer)
            return render_template('product_display.html', error="Invalid ID format. ID must be an integer.")

    # 3. Successful Display
    return render_template('product_display.html', products=display_products, source=source)

# --- Server Execution ---

if __name__ == '__main__':
    # ⚠️ IMPORTANT: Run the database creation script before starting the server
    create_database()
    print("Database 'products.db' created and populated.")

    # Run the application on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)
