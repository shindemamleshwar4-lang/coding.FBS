#convert the time entered in hh,min and sec into second
hours = int(input('enter hours:-'))
minutes = int(input('enter minutes:-'))
second = int(input('enter second:-'))

Total_second= (hours * 3600 + minutes * 60) +second

print('total second:-', Total_second)