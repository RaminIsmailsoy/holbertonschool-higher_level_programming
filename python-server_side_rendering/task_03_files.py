#!/usr/bin/python3
''' Displaying Data from JSON or CSV Files in Flask '''


from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# --- Helper Functions for Data Reading ---

def read_json_data(filename='products.json'):
    """Reads and parses data from a JSON file."""
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}")
        return []

def read_csv_data(filename='products.csv'):
    """Reads and parses data from a CSV file."""
    data = []
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, mode='r', newline='') as f:
            # csv.DictReader maps the rows to dictionaries using the header row as keys
            reader = csv.DictReader(f)
            for row in reader:
                # Convert 'id' and 'price' to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    return data

# --- Main Route ---

@app.route('/products')
def products():
    """
    Handles data display based on 'source' and filters by optional 'id'.
    """
    # Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    # 1. Source Validation
    if source == 'json':
        all_products = read_json_data()
    elif source == 'csv':
        all_products = read_csv_data()
    else:
        # Edge Case: Invalid or missing 'source'
        return render_template('product_display.html', error="Wrong source. Must be 'json' or 'csv'.")

    # Handle file reading error
    if all_products is None:
        return render_template('product_display.html', error=f"Could not load data from {source} file.")

    # Initialize the list of products to display
    display_products = all_products

    # 2. ID Filtering (if 'id' parameter is provided)
    if product_id_str:
        try:
            target_id = int(product_id_str)
            # Filter the list to find the matching product
            filtered_list = [p for p in all_products if p.get('id') == target_id]

            if not filtered_list:
                # Edge Case: ID not found
                return render_template('product_display.html', error=f"Product not found. ID {target_id} does not exist in the {source} data.")

            display_products = filtered_list

        except ValueError:
            # Edge Case: Invalid ID format (not an integer)
            return render_template('product_display.html', error="Invalid ID format. ID must be an integer.")

    # 3. Successful Display
    # Pass the filtered (or full) list of products and the source to the template
    return render_template('product_display.html', products=display_products, source=source)

# --- Server Execution ---

if __name__ == '__main__':
    # Run the application on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)
