import numpy as np 
import math
from prettytable import PrettyTable 

N = 10000

def RNEXP(b):
    u = np.random.uniform(0, 1)
    return -b * math.log(u)
    
gfg = []
for i in range(N):
    gfg.append(RNEXP(1))
    
M = sum(gfg)/N
t = 0
for x in gfg:
    t += (x - M)**2
    
D = t/N

myTable = PrettyTable(["Момент", "RNEXP", "Теоретическое значение"])

myTable.add_row(["E(x)", M, 1])
myTable.add_row(["V(x)", D, 1])

print(myTable)