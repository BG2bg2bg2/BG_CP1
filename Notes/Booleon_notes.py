# BG 1st Booleon notes

import time
import datetime as date



current_time = time.time()
readable_time = time.ctime(current_time)

new_curant_time = date.datetime.now()

hour = new_curant_time.strftime("%S")
#minute = %M
#weekday = %A, %a
#day of month = %D
# mounth = %B == fullname, abreve = %b
#year = %Y, %y
#second = %S
over = True





print(f"curent time in seconds since January 1, 1970(epoch): {current_time}")
print(f"curent time in seconds since January 1, 1970(epoch): {new_curant_time}")
print(f"today is {readable_time}")
print(f"the hour is {hour}")

print(f"The hour is saved as an integer: {isinstance(hour, int)}")
print(f"The hour is saved as an float: {isinstance(hour, float)}")
print(f"The hour is saved as an string: {isinstance(hour, str)}")


print(f"Hour has avalue: {bool()}")