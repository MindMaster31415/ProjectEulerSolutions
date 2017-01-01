#"This is my solution for Problem 19 of Project Euler." - Sumedh Garimella
print("Now calculating the number of Sundays at the start of a month between 1901 and 2000...")
jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = 2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0
#months and the day-modulos(Sunday = 0, 7, etc.) for each month in 1901
y = 1901 #starting year
s = 0 #counter of Sundays in given period
while y <= 2000: #until 2000
    if jan % 7 == 0:  #if the modulo is 0 (Sunday), add to s
        s += 1
    if feb % 7 == 0:
        s += 1
    if mar % 7 == 0:
        s += 1
    if apr % 7 == 0:
        s += 1
    if may % 7 == 0:
        s += 1
    if jun % 7 == 0:
        s += 1
    if jul % 7 == 0:
        s += 1
    if aug % 7 == 0:
        s += 1
    if sep % 7 == 0:
        s += 1
    if oct % 7 == 0:
        s += 1
    if nov % 7 == 0:
        s += 1
    if dec % 7 == 0:
        s += 1
    y += 1
    jan += 1 #changes by 1 day every year (leap exceptions below...)
    feb += 1
    mar += 1
    apr += 1
    may += 1
    jun += 1
    jul += 1
    aug += 1
    sep += 1
    oct += 1
    nov += 1
    dec += 1
    if y % 4 == 0: #change occurs in a leap year for march - december since they are after leap day
        mar += 1
        apr += 1
        may += 1
        jun += 1
        jul += 1
        aug += 1
        sep += 1
        oct += 1
        nov += 1
        dec += 1
    if y % 4 == 1: #january and february add another day in the next year
        jan += 1
        feb += 1
print("The number of Sundays falling on the first of a month between 1901 and 2000 was:", s) #result
