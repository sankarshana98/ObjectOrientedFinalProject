import json

def get_user_id_by_username(username):
    with open('users.json', 'r') as file:
        users = json.load(file)

    for user in users:
        if user["username"] == username:
            return user["user_id"]

    return None  # Return None if the username is not found
