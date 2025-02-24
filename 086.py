class Password:
    def __init__(self, password):
        self.__password = password

    def print_len(self):
        print("Your password Len is", len(self.__password))
pwd = Password("Hacker123")
pwd.print_len()