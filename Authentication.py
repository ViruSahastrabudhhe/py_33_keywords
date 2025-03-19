class Authentication:
    def __init__(self):
        self.attempts = 3

    def login(self, pin):
        try:
            pinParseInt = int(pin)
        except ValueError:
            print("PIN only accepts numbers!")
        finally:
            print(f"You have {self.attempts} attempts left!\n")
        
        if pinParseInt==1234:
            return True
        else:
            return False
        
    def lockout(self):
        print("Device lockout!")
        assert self.attempts == 3