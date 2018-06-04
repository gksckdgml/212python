#-*-cording:utf-8-*-

import matplotlib.pyplot as plt
import random

# x1 = [1,2,3,4,5,6,7,8,9]
# y1 = [10,14,25,5,20,30,14,25,5]
# x2 = [1,2,3,4,5,6,7,8,9]
# y2 = [16,41,18,30,10,14,25,30,14]

x1 = [i for i in range(100)]
y1 = [random.randint(0,j) for j in range(100)]

plt.plot(x1,y1, label = "First")
# plt.plot(x2,y2, label = "Second")

plt.xlabel("Numbers")
# plt.ylabel("Counting")

plt.title("Practice Plot - 한글")

plt.legend()
plt.show()
