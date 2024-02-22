import numpy as np
from prettytable import PrettyTable 
  
n = 100000

def IRNGEO_1(p):
    M = np.random.random()
    P = p
    M = M - P
    k = 1
    while M >= 0:
        P = P * (1 - p)
        k += 1
        M = M - P
    return k

gfg = []
for _ in range(n):
    gfg.append(IRNGEO_1(0.5))
    
M1 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M1)**2
    
D1 = t/n

def IRNGEO_2(p):
    u = np.random.uniform(0, 1)
    k = 1
    while u > p:
        u = np.random.uniform(0, 1)
        k += 1
    return k

gfg = []
for _ in range(n):
    gfg.append(IRNGEO_2(0.5))
    
M2 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M2)**2
    
D2 = t/n

def IRNGEO_3(p):
    u = np.random.random()
    return int(np.log(u) / np.log(1 - p)) + 1

gfg = []
for _ in range(n):
    gfg.append(IRNGEO_3(0.5))
    
M3 = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M3)**2
    
D3 = t/n

myTable = PrettyTable(["Оценка", "IRNGEO_1", "IRNGEO_2", "IRNGEO_3", "Теоретическое значение"])

myTable.add_row(["M", M1, M2, M3, 2.0])
myTable.add_row(["D", D1, D2, D3, 2.0])

print(myTable)
