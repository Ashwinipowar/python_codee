# import time
# t = time.strftime('%H:%M:%S:')
# hour = int(time.strftime('%H'))
# hour = int(input("Enter hour:"))
# print(hour)


# if(hour>=0 and hour<12):
#   print("GOOD MORNING SIR !")
# elif(hour>=12 and hour<17):
#   print("GOOD AFTERNOON SIR!")
# elif(hour>=17 and hour<24):
#   print("good night sir !")
# else:
#   print("not eligible")



# program no. two

from datetime import datetime
import pytz

ist_timezone = pytz.timezone('Asia/kolkata')
ist_now = datetime.now(ist_timezone)

current_hour = ist_now.hour

if 5 <= current_hour < 12:
    print("Good Morning! 🌞")
elif 12 <= current_hour < 17:
    print("Good Afternoon! ☀️")
elif 17 <= current_hour < 21:
    print("Good Evening! 🌆")
else:
    print("Good Night! 🌙")


print("Current Indian Standard Time (IST):", ist_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))




