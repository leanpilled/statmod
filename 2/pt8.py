import numpy as np
from scipy.stats import pearsonr

p = 0.7
size = 50

sample = np.random.geometric(p, size)

expected_freq = [(1 - p) ** k * p for k in range(max(sample))]

unique, counts = np.unique(sample, return_counts=True)

d = dict(zip(unique, counts))

sample_freq = []
    
for i in range(1, max(sample) + 1):
    if i in d:
        sample_freq.append(d[i] / size)
    else:
        sample_freq.append(0)
    
res = pearsonr(sample_freq, expected_freq)

print("p-value:", res.pvalue)

alpha = 0.05
if res.pvalue < alpha:
    print("Отклоняем нулевую гипотезу: эмпирическое распределение не согласуется с теоретическим")
else:
    print("Не отклоняем нулевую гипотезу: эмпирическое распределение согласуется с теоретическим")
