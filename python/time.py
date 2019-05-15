import time

relogio = time.localtime()
print(relogio.tm_year)
print(relogio.tm_mon)
print(relogio.tm_mday)

print(relogio.tm_hour)
print(relogio.tm_min)
print(relogio.tm_sec)