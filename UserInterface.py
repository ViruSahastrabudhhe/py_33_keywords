from Authentication import Authentication as auth
from Calculator import Calculator as calc
from Clock import Clock as clock
from Camera import Camera as cam

class UserInterface:
    def __init__(self):
        self.shutDown = "q Q"
        self.auth = auth()
        self.calc = calc()
        self.clock = clock()
        self.cam = cam()

    def start(self):
        print("luke demerin shitty samsung phone simulator")

        while True:
            if self.auth.attempts == 0:
                self.auth.lockout()

            pinInput = input("\nPIN: ")
            if self.auth.login(pinInput)==True:
                print("Welcome!")
                self.auth.attempts = 3
                self.navigation()
                break
            else:
                print("Incorrect PIN!")
                self.auth.attempts -= 1
                continue

    def navigation(self):
        while True:
            print("\nHome screen:")
            print("1 - Clock")
            print("2 - Camera")
            print("3 - Calculator")
            print("X - Close screen")
            print("Q - Shut down")

            navigationChoice = input("\nNavigation: ")
            if navigationChoice.lower() not in self.shutDown:
                if navigationChoice=="1":
                    self.clockChoices()
                    continue
                elif navigationChoice=="2":
                    self.cameraChoices()
                    continue
                elif navigationChoice=="3":
                    self.calculatorChoices()
                    continue
                elif navigationChoice.lower()=="x":
                    self.closeScreen()
                    continue
                else:
                    print("Unknown input!")
                    continue

            raise Exception("Phone shut down!")

    def clockChoices(self):
        while True:
            print("\nChange time with the clock!")
            print("A - Get current time")
            print("B - Date calculator")
            print("X - Return to main menu")

            clockChoice = input("\nClock navigation: ")
            if clockChoice.lower()=="x":
                break

            self.clockFunctions(clockChoice)

    def clockFunctions(self, clockChoice: str):
        if clockChoice.lower()=="a":
            self.clock.getCurrentTime()
            return
        if clockChoice.lower()=="b":
            while True:
                days = input("The date after how many days (empty input will return to clock): ")

                if days==" ":
                    break
                
                try:
                    daysParseInt = int(days)
                except ValueError:
                    return None
                
                print(self.clock.getDate(daysParseInt))
        return
        
    def cameraChoices(self):
        while True:
            print("\nTake photos with the camera!")
            print("A - Selfie")
            print("X - Return to main menu")

            camChoice = input("\nCamera navigation: ")
            if camChoice.lower()=="x":
                break

            self.cameraFunctions(camChoice)

    def cameraFunctions(self, camChoice: str):
        if camChoice.lower()=="a":
            self.cam.selfie()

        return

    def calculatorChoices(self):
        while True:
            print("\nDo math with two variables!")
            print("A - Addition")
            print("B - Subtraction")
            print("C - Multiplication")
            print("D - Division")
            print("E - History")
            print("X - Return to main menu")

            calculatorNav = input("\nCalculator operation: ")
            if calculatorNav.lower()=="x":
                break
            
            self.calculatorFunctions(calculatorNav)

    def calculatorFunctions(self, calculatorNav: str):
        if calculatorNav.lower()=="a":
            while True:
                a = input("Num 1 (leave empty to return to main menu): ")
                b = input("Num 2 (leave empty to return to main menu): ")
                if (a==" " and b==" ") or a==" " or b==" ":
                    break

                try:
                    aParseInt = int(a)
                    bParseInt = int(b)
                except ValueError:
                    return None

                sum = self.calc.addition(aParseInt, bParseInt)
                print(f"Sum of {aParseInt} + {bParseInt} = {sum}")
                self.calc.history.append(self.calc.addition(aParseInt, bParseInt))

        if calculatorNav.lower()=="b":
            while True:
                a = input("Num 1 (leave empty to return to main menu): ")
                b = input("Num 2 (leave empty to return to main menu): ")
                if (a==" " and b==" ") or a==" " or b==" ":
                    break

                try:
                    aParseInt = int(a)
                    bParseInt = int(b)
                except ValueError:
                    return None

                difference = self.calc.subtraction(aParseInt, bParseInt)
                print(f"Difference of {aParseInt} - {bParseInt} = {difference}")
                self.calc.history.append(difference)

        if calculatorNav.lower()=="c":
            while True:
                a = input("Num 1 (leave empty to return to main menu): ")
                b = input("Num 2 (leave empty to return to main menu): ")
                if (a==" " and b==" ") or a==" " or b==" ":
                    break
                
                try:
                    aParseInt = int(a)
                    bParseInt = int(b)
                except ValueError:
                    return None

                product = self.calc.multiplication(aParseInt, bParseInt)
                print(f"Product of {aParseInt} * {bParseInt} = {product}")
                self.calc.history.append(product)

        if calculatorNav.lower()=="d":
            while True:
                a = input("Num 1 (leave empty to return to main menu): ")
                b = input("Num 2 (leave empty to return to main menu): ")
                if (a==" " and b==" ") or a==" " or b==" ":
                    break

                try:
                    aParseInt = int(a)
                    bParseInt = int(b)
                except ValueError:
                    return None
                    
                quotient = self.calc.division(aParseInt, bParseInt)
                print(f"Quotient of {aParseInt} / {bParseInt} = {quotient}")
                self.calc.history.append(quotient)

        if calculatorNav.lower()=="e":
            self.calculatorHistory()

        return

    def calculatorHistory(self):
        while True:
            print("\nCalculator history: ")
            print("A - View history")
            print("B - Delete history")
            print("X - Return to calculator")

            calcHistoryNav = input("\nInput: ")
            if calcHistoryNav.lower()=="x":
                break
            
            if calcHistoryNav.lower()=="a":
                self.calc.printHistory()
            elif calcHistoryNav.lower()=="b":
                del self.calc.history
                print("Successfully deleted calculator history!")
                self.calc.history = []
            else:
                print("Invalid input!")

    def closeScreen(self):
        print("\nPhone screen turned off!")
        openScreen = input()
        print("\nPhone screen turned on!")
        self.start()