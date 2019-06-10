import time
import datetime

class Personal_Assistant:

    def start(self):
        print("Good", self.timeOfDay() + ", sir!")
        print("Todays forcast is showing... ")

    def timeOfDay(self):
        time_now = datetime.datetime.now().time()
        hour_now = time_now.hour

        if 6 <= hour_now < 9 :
            return "morning"
        elif hour_now < 14:
            return "day"
        elif hour_now < 18:
            return "afternoon"
        elif hour_now < 21:
            return "evning"
        else:
            return "night"


a = Personal_Assistant()
a.start()
