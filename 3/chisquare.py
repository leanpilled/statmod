import numpy as np 
from prettytable import PrettyTable 

N = 10000

def RNCHIS(n):
    res = 0
    for _ in range(n):
        u = np.random.normal(0, 1)
        res += u ** 2
    return res
    
gfg = []
for i in range(N):
    gfg.append(RNCHIS(10))
    
M = sum(gfg)/N
t = 0
for x in gfg:
    t += (x - M)**2
    
D = t/N

myTable = PrettyTable(["Момент", "RNCHIS", "Теоретическое значение"])

myTable.add_row(["E(x)", M, 10])
myTable.add_row(["V(x)", D, 20])

print(myTable)