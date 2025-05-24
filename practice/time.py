
import datetime

date = datetime.date(2025, 1, 4)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime =  datetime.datetime(2020, 1, 12, 3, 30, 5)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has pass")
else:
    print("Target date has not pass")