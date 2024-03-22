class Account():
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    
    def __str__(self):
        return f"{self.username:<10} {self.password:<10} {self.role:<10}"