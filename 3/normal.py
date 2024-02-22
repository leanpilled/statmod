import numpy as np 
import math
from prettytable import PrettyTable 

N = 1000

def RNRM2(m, sigma):
    n = 0
    M = N
    S = 0
    while n <= M:
        a = np.random.uniform(0, 1)
        S = S + a
        n += 1
    return m + sigma * (S - 0.5 * n) * (6 / math.sqrt(3 * n))
    
gfg = []
for i in range(N):
    gfg.append(RNRM2(0, 1))
    
M1 = sum(gfg)/N
t = 0
for x in gfg:
    t += (x - M1)**2
    
D1 = t/N

def RNRM1():
    r = np.random.uniform(0, 1)
    f = np.random.uniform(0, 1)
    z0 = math.cos(2 * math.pi * f) * math.sqrt(-2 * math.log(r))
    z1 = math.sin(2 * math.pi * f) * math.sqrt(-2 * math.log(r))
    return [z0, z1]

gfg = []
for i in range(N):
    vals = RNRM1()
    for v in vals:
        gfg.append(v)
    
M2 = sum(gfg)/(N*2)
t = 0
for x in gfg:
    t += (x - M2)**2
    
D2 = t/(N*2)

myTable = PrettyTable(["Момент", "RNRM1", "RNRM2", "Теоретическое значение"])

myTable.add_row(["E(x)", M2, M1, 0.])
myTable.add_row(["V(x)", D2, D1, 1.0])

print(myTable)