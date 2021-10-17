from playsound import playsound
from datetime import datetime


alarm_time = input("When should the alarm should be set (in HH:MM:SS:(pm or am)) : ")

alarm_hr = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_mrng_or_eve =  alarm_time[9:11].upper()

print(alarm_time, type(alarm_time))

while True:
    now = datetime.now()
    current_hr = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_mrng_or_eve = now.strftime("%p")

    if current_mrng_or_eve == alarm_mrng_or_eve:
        if current_hr == alarm_hr:
            if current_min == alarm_min:
                if current_sec == alarm_sec:
                    print("ALARM RINGING...")
                    playsound('G:\My Drive\Python Projects\HanumanChalisa.mp3')
                    break