class User:
    def __init__(self, user_id, username, password, full_name="", email="", profile_pic=None):
        """
        Initialize a User object.

        Parameters:
        - user_id (int): Unique identifier for the user.
        - username (str): The username chosen by the user.
        - password (str): The user's password.
        - full_name (str, optional): The full name of the user (default is an empty string).
        - email (str, optional): The email address of the user (default is an empty string).
        - profile_pic (str or None, optional): File path or URL to the user's profile picture
          (default is None).

        Note:
        - The `user_id` should be unique for each user.
        - The `profile_pic` parameter can be a file path or a URL, or None if the user
          has no profile picture.
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.profile_pic = profile_pic

    def __str__(self):
        """
        Return a string representation of the User object.
        """
        return f"User: {self.username} ({self.full_name}), Email: {self.email}, UserID: {self.user_id}"
