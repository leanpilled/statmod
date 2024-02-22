import numpy as np
from prettytable import PrettyTable 
  
n = 100000

def IRNBIN(N, p):
    M = np.random.random()
    P = (1 - p) ** N
    M = M - P
    k = 0
    while M >= 0:
        P = P * (((N - k) / (k + 1)) * (p / (1 - p)))
        k += 1
        M = M - P
    return k

gfg = []
for _ in range(n):
    gfg.append(IRNBIN(10, 0.5))
    
M1 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M1)**2
    
D1 = t/n

def IRNBNL(n, p):
    return np.random.normal(n * p, np.sqrt(n * p * (1.0 - p)))

gfg = []
for _ in range(n):
    gfg.append(IRNBNL(10, 0.5))
    
M2 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M2)**2
    
D2 = t/n

myTable = PrettyTable(["Оценка", "IRNBIN", "IRNBNL", "Теоретическое значение"])

myTable.add_row(["M", M1, M2, 5.0])
myTable.add_row(["D", D1, D2, 2.5])

print(myTable)
