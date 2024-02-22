import numpy as np
from scipy.stats import binomtest

sample_X = np.random.triangular(0, 1, 2, size=50)

sample_Y = np.random.normal(1, 1, size=50)

differences = sample_X - sample_Y

positive_diff_count = np.sum(differences > 0)
negative_diff_count = np.sum(differences < 0)

res = binomtest(min(positive_diff_count, negative_diff_count), n=50)

print("Количество положительных разностей:", positive_diff_count)
print("Количество отрицательных разностей:", negative_diff_count)
print("p-значение критерия знаков:", res.pvalue)

alpha = 0.05
if res.pvalue < alpha:
    print("Отвергаем гипотезу H0 о совпадении распределений X и Y")
else:
    print("Принимаем гипотезу H0 о совпадении распределений X и Y")
