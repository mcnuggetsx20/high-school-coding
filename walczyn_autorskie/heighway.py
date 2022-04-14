import matplotlib.pyplot as plt
import random

x = [1]
y = [1]

avg=[0,0]

mx=[0,0]
mn=[10**9, 10**9]

for i in range(5000):
    a = random.randint(0,1)
    x_new = -0.4*x[-1] -1 + (1.16 * x[-1] +1 -0.4*y[-1]) * a
    y_new = -0.4*y[-1] + 0.1 + (-0.1 + 0.4 * x[-1] + 1.16 * y[-1]) * a
    x.append(x_new)
    y.append(y_new)
    avg[0] += x_new * i>99
    avg[1] += y_new * i>99
    mx[0] = max(mx[0], x_new* int(i>99))
    mx[1] = max(mx[1], y_new* int(i>99))
    mn[0] = min(mn[0], x_new + 10**9 * int(i<=99))
    mn[1] = min(mn[1], y_new + 10**9 * int(i<=99))

avg[0] /= 4900
avg[1] /= 4900

print('{0:.1f}'.format(avg[0]), '{0:.1f}'.format(avg[1]))
print('{0:.1f}'.format(mn[0]), '{0:.1f}'.format(mn[1]))
print('{0:.1f}'.format(mx[0]), '{0:.1f}'.format(mx[1]))

plt.plot(x[99:], y[99:], 'o')
plt.show()
