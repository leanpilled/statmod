import numpy as np
import math
from prettytable import PrettyTable 
  
n = 100000

def IRNPOI(mu):
    M = np.random.random()
    P = math.e ** -mu
    M = M - P
    k = 1
    while M >= 0:
        P = P * mu / k
        k += 1
        M = M - P
    return k - 1

gfg = []
for _ in range(n):
    gfg.append(IRNPOI(10))
    
M1 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M1)**2
    
D1 = t/n

def IRNPSN(mu):
    return np.random.normal(mu, mu)

gfg = []
for _ in range(n):
    gfg.append(IRNPSN(10))
    
M2 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M2)**2
    
D2 = t/n/10

myTable = PrettyTable(["Оценка", "IRNPOI", "IRNPSN", "Теоретическое значение"])

myTable.add_row(["M", M1, M2, 10.0])
myTable.add_row(["D", D1, D2, 10.0])

print(myTable)
