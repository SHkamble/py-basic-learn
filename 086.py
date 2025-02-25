class Password:
    def __init__(self, password):
        self.__password = password
        self.print_var = 10  # Assuming this is intended to exist for reference.

    def get_password(self, isAuth):
        if isAuth:
            return self.__password
        else:
            print("Error: Unauthorized access to password")
            return None  # Explicitly returning None for clarity.

    def set_password(self, password):
        if len(password) >= 10:
            self.__password = password
        else:
            print("Error: Weak password, must be at least 10 characters long")

    def print_len(self):
        if isinstance(self.__password, str):  # Safeguard in case __password isn't a string.
            print("Your password length is", len(self.__password))
        else:
            print("Error: Password is not set or invalid")


pwd = Password("Hacker12345678")

# Removed the problematic line `pwd.public_var`

pwd.print_len()
pssd = pwd.get_password(True)
print(pssd)

pwd.set_password("Hacker123456789")
pwd.print_len()
