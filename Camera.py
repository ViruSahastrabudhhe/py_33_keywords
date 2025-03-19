class Camera:
    def __init__(self):
        self.viewfinder = "pogi"

    def selfie(self):
        pogi = self.viewfinder
        if pogi is self.viewfinder:
            print("POGI SELFIE")

        def writeToFile():
            nonlocal pogi
            with open("cameraStuff.txt", "w") as file:
                file.write("pogi.jpg")
        
        writeToFile()