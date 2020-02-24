##You are given the following information, but you may prefer
##to do some research for yourself.
##
##1 Jan 1900 was a Monday.
##Thirty days has September,
##April, June and November.
##All the rest have thirty-one,
##Saving February alone,
##Which has twenty-eight, rain or shine.
##And on leap years, twenty-nine.
##A leap year occurs on any year evenly divisible by 4,
##but not on a century unless it is divisible by 400.
##How many Sundays fell on the first of the month during
##the twentieth century (1 Jan 1901 to 31 Dec 2000)?

weekday = ['Tuesday','Wednesday','Thursday','Friday','Saturday',\
           'Sunday','Monday']
month = ['January','February','March','April','May','June','July',\
         'August','September','October','November','December']
day = []
for i in range(1,32):
    day.append(i)
year = []
for i in range(1901,2001):
    year.append(i)
date = []

a = 0
b = 0
c = 0
d = 0

first_sun = 0

while 2 > 1:
    date.append(weekday[a] + ' ' + month[b] + ' ' +\
                str(day[c]) + ' ' + str(year[d]))
    if day[c] == 1 and weekday[a] == 'Sunday':
        first_sun += 1
        print(date[-1])

    if a == 6:
        a = 0
    else:
        a +=1
        
    if b == 3 and c == 29 or b == 5 and c == 29 or b == 8 and c == 29\
       or b == 10 and c == 29:
        c = 0
    elif b == 1 and c == 28:
        c = 0
    elif b == 1 and c == 27 and year[d] % 4 != 0:
        c = 0
    elif c == 30:
        c = 0
    else:
        c += 1

    if c == 0 and b == 11:
        b = 0
        d += 1
    elif c == 0:
        b += 1
    
    if d == 100:
        break

print(first_sun)
    
