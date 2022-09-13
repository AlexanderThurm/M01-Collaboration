#There are 3600 seconds in 1 hour
seconds_per_hour = 60 * 60
print(seconds_per_hour)

seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)

x = seconds_per_day / seconds_per_hour
y = seconds_per_day // seconds_per_hour
print(x)
print(y)
#Yes, the / printed with a .0 and // printed without it.