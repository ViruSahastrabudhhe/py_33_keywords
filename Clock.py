from datetime import date, timedelta, datetime
import time

class Clock:
    def currentTime(self):
        yield datetime.now()
        pass

    def getCurrentTime(self):
        global x
        x=self.currentTime()
        for z in x:
            print(z)

    def getDate(self, daysParseInt):
        dateAfterXDays = (datetime.now() + timedelta(days=daysParseInt) ).strftime('%d-%m-%Y')
        return dateAfterXDays