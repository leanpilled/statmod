import numpy as np 
import math
import matplotlib.pyplot as plt 
from prettytable import PrettyTable 
  
n = 1000
gfg = np.random.uniform(0, 1, n) 

M = sum(gfg)/n
t = 0
for x in gfg:
    t += (x - M)**2
    
D = t/n
S = math.sqrt(D)

def K(f):
    divisible = 0.0
    divider = 0.0
    
    for i in range(n - f):
        divisible += (gfg[i] - M) * (gfg[i + f] - M)
    
    for i in range(n):
        divider += (gfg[i] - M)**2
    
    return divisible / divider

correlogramm = []
for i in range(n):
    correlogramm.append(K(i))
    
plt.hist(range(n), bins=n, weights=correlogramm)
plt.show()

def empirical_density_function(data, x):
    count = np.sum(data <= x)
    return count / len(data)

def empirical_distribution_function(data, x):
    sorted_data = np.sort(data)
    count = np.searchsorted(sorted_data, x, side='right')
    return count / len(data)

x_values = np.linspace(min(gfg), max(gfg), 100)
edf_values = [empirical_density_function(gfg, x) for x in x_values]
edf_integral_values = [empirical_distribution_function(gfg, x) for x in x_values]

print(edf_values == edf_integral_values)

plt.subplot(1, 2, 1)
plt.plot(x_values, edf_values, label='ЭФП')
plt.scatter(gfg, np.zeros_like(gfg), color='red', marker='|', label='Данные')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, edf_integral_values, label='ЭИФ')
plt.scatter(gfg, np.zeros_like(gfg), color='red', marker='|', label='Данные')
plt.legend()

plt.tight_layout()
plt.show()


myTable = PrettyTable(["n", "Оценка распр.", "RAND(эксперимент)", "Теоретическое значение", "Отклонение"])

n = 10
while n <= 10000:
    
    gfg = np.random.uniform(0, 1, n) 
    
    M = sum(gfg)/n
    t = 0
    for x in gfg:
        t += (x - M)**2
        
    D = t/n
    
    myTable.add_row([n, "M", M, 0.5, abs(0.5 - M)])
    myTable.add_row(["", "D", D, 0.08333, abs(0.08333 - D)])
    
    n *= 10
    
print(myTable)