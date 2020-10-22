import time
import datetime as dt
import winsound
def myAlarm():
    try:
        print("Enter time in hr min sec format:")
        t=[int(i) for i in input().split()]
        if (len(t)==3):
            ts=(t[0]*60*60)+(t[1]*60)+t[2]
            x = (str(dt.datetime.now())).split(" ")[1]
            ct = (int(x[:2]) * 60 * 60) + (int(x[3:5]) * 60) + (float(x[6:]))
            total_time=ts-ct
            time.sleep(total_time)
            freq=2500
            dur=2000
            winsound.Beep(freq,dur)
        else:
            print("You entered time in incorrect format")
            myAlarm()
    except Exception as e:
        print("Exception :",e,"Enter correct details")
        myAlarm()
myAlarm()
