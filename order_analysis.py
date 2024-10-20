import json
import sys
from collections import defaultdict

def format_phone_number(phone_number):
    """Format phone number to xxx-xxx-xxxx."""
    return f"{phone_number[:3]}-{phone_number[4:7]}-{phone_number[8:]}"

def extract_customer_data(order):
    """Extract customer name and formatted phone number from the order."""
    phone_number = order.get('phone')
    customer_name = order.get('name')

    if phone_number and customer_name:
        return format_phone_number(phone_number), customer_name
    return None, None

def aggregate_items(orders):
    """Aggregate item data from orders."""
    items = defaultdict(lambda: {'price': 0.0, 'orders': 0})

    for order in orders:
        for item in order.get('items', []):
            item_name = item.get('name')
            item_price = item.get('price')

            if item_name and item_price is not None:
                items[item_name]['price'] = item_price  # Assuming price is constant for each item
                items[item_name]['orders'] += 1  # Increment order count
    return items

def load_orders_from_file(input_file):
    """Load orders from the specified JSON file."""
    try:
        with open(input_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' is not a valid JSON file.")
        sys.exit(1)

def save_to_file(data, filename):
    """Save data to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error: Failed to write to file '{filename}': {e}")
        sys.exit(1)

def main(input_file):
    """Main function to process orders and generate JSON output files."""
    customers = {}

    # Load orders from the input file
    orders = load_orders_from_file(input_file)

    # Process each order
    for order in orders:
        formatted_phone, customer_name = extract_customer_data(order)

        if formatted_phone and customer_name:
            customers[formatted_phone] = customer_name

    # Aggregate item data
    items = aggregate_items(orders)

    # Save customers to customers.json
    save_to_file(customers, 'customers.json')

    # Save items to items.json
    save_to_file(items, 'items.json')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python order_analysis.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
