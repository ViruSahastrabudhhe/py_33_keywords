from datetime import date
import time

class Clock:
    def getCurrentTime(self):
        yield date.today()
        yield time.localtime()
        pass

    # def setAlarm(self, hour, minute, second):
        