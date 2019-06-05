import time
import datetime


# time.asctime() = Wed Jun  5 23:18:04 2019
# datetime.datetime.now = 2019-06-05 23:19:25.613302

class Study_Assistant: 
    


    #start = time.time()
    #end = time.time()
    #print(end - start)
    
    def begin_reading(self):
        start_time = datetime.datetime.now()  
        
        study_interval = datetime.timedelta(minutes=25)
        break_interval = datetime.timedelta(minutes=5)


        end_time = start_time + study_interval


        print("Time is now", start_time)
        print("Following the Pomodro Technique, next break is at: ", start_time + study_interval)
        finished_reading = "false"
        while not finished_reading == "true":
            start_time = datetime.datetime.now()
            end_time = start_time + study_interval


            self.begin_study_interval(start_time, end_time)
            print("Congratulations, you have completed 25 minutes of studying!")
            finished_reading = (input("Have you finished reading? (true/false)"))
            if finished_reading == "true":
                break
            print("Time to take a five minute brake")

            start_time = datetime.datetime.now()
            end_time = start_time + break_interval

            self.begin_break_interval(start_time, end_time)
            print("="*25)
            print("Suit up! Its time to continue reading!")
            print("="*25)
  

    def begin_study_interval(self, start_time, end_time):
        minutes = 0
        while minutes < 25:
            print("Time left: ", end_time - datetime.datetime.now(), "Time elapsed: ", datetime.datetime.now() - start_time, minutes)
            time.sleep(60)
            minutes += 1

    def begin_break_interval(self, start_time, end_time):
        break_interval = datetime.timedelta(minutes=5)
        minutes = 0
        while minutes < 5:
            print("Time left: ", end_time - datetime.datetime.now(), "Time elapsed: ", datetime.datetime.now() - start_time, minutes)
            time.sleep(30)
            minutes += 1



    #def get_current_time(self):
    #    return time.time()

    #def get_given_time(self, time_value):
     #   return time.asctime()


    #def print_current_time(self):
     #   print(time.asctime())


print(datetime.datetime.now())
print("_"*25)

q = Study_Assistant()
q.begin_reading()

