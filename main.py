import matplotlib.pyplot as plt
import numpy as np


x = np.array([10, 25, 30, 50, 60])
mylabels = ["Bananas", "Maçãs", "Morangos", "Uvas", "Melancias"]

myexplode = [0, 0.4, 0, 0, 0]

plt.title("GRÁFICO EM PIZZA!")


plt.pie(x, labels=mylabels, explode=myexplode)
plt.legend( title = "Frutas")
plt.show()