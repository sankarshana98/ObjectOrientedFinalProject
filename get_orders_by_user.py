import json

def get_orders_by_user_id(user_id):
    file_path = "orders.json"

    orders = []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content:
                all_orders = json.loads(content)
                if isinstance(all_orders, list):
                    orders = [order for order in all_orders if order.get("user_id") == user_id]
                else:
                    print("Invalid content in orders.json. Expected a JSON array.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")

    return orders