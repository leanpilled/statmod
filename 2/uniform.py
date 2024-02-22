import numpy as np 
from prettytable import PrettyTable 
  
n = 100000

def IRNUNI(low, high):
    u = np.random.sample()
    return (high - low + 1) * u + low
    
gfg = []
for i in range(n):
    gfg.append(IRNUNI(1, 100))
    
M = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M)**2
    
D = t/n
    
myTable = PrettyTable(["Оценка", "IRNUNI", "Погрешность", "Теоретическое значение"])

myTable.add_row(["M", M, abs(50.5 - M), 50.5])
myTable.add_row(["D", D, abs(833.25 - D), 833.25])

print(myTable)
