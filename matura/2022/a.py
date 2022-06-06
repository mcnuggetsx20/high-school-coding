import datetime

a = datetime.datetime.strptime('14:00', '%H:%M')
b = datetime.datetime.strptime('16:00', '%H:%M')

c = datetime.timedelta(days=0)
print( abs(b-a).seconds / 3600)


