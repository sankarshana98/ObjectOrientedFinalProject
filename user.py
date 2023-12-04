# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def __str__(self):
#         return f"User: {self.username}"

# user.py

class User:
    def __init__(self, user_id, username, password, full_name="", email="", profile_pic=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.profile_pic = profile_pic

    def __str__(self):
        return f"User: {self.username} ({self.full_name}), Email: {self.email}, UserID: {self.user_id}"

