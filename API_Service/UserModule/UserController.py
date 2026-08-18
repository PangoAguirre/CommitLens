class UserValidator:
    def __init__(self):
        pass
    
    def validate_user(self, username, password, userRepository):
        if not username or not password:
            return False, "Username and password cannot be empty."
        if len(username) < 3 or len(password) < 6:
            return False, "Username must be at least 3 characters and password at least 6 characters long."
        if userRepository.get_user_by_username(username):
            return False, "Username already exists."
        return True, "Validation successful."