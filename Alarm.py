import datetime
import playsound
import time
timer = input('Alarm tarihi girin(Gün Ay Yıl Saat Dakika şeklinde(02 08 2022 20 15)): ')
day, month, year, hour, minu = [i for i in timer.split()]

alarm = datetime.datetime(int(year), int(month), int(day), int(hour), int(minu))
now = datetime.datetime.today()

difference = alarm - now
difference_second = difference.seconds
time.sleep(difference_second - 50)

while True:
    now = datetime.datetime.today()
    if now.day == alarm.day and now.month == alarm.month and now.year == alarm.year and now.hour == alarm.hour and now.minute == alarm.minute:
        playsound('konum/ses_dosyası.mp3')
        time.sleep(50)
        break
    else:
        time.sleep(3)
