import datetime
import matplotlib.pyplot as plt 

day = datetime.datetime(2022, 4, 1)

init=['10000', '7000', '4000']
data=[]

for i in init:
    grass = int(i)
    day = datetime.datetime(2022, 4, 1)
    while day!=datetime.datetime(2022,4,1)+datetime.timedelta(days=100):
        grass -= 15 * 30
        grass+=600
        grass -= (3*grass)//100
        day+=datetime.timedelta(days=1)
    data.append(grass)

print(data)
plt.bar(list(init), list(data), width=0.4, color='maroon')
plt.title('Wartosci zgromadzonej trawy po 100 dniach (w metrach szesciennych)')
plt.show()
