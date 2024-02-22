import numpy as np

def LFSR(x):
    T = 8760
    return ((x[0] > T and x[1] > T) or (x[2] > T and x[3] > T)) and x[4] > T and x[5] > T and (
        x[6] > T or x[7] > T or x[8] > T) and (x[9] > T or x[10] > T)

def trace(L):
    N = 53526
    n = [4, 2, 3, 2]
    m = 4
    lambd = [40 * 10**(-6), 10 * 10**(-6), 80 * 10**(-6), 30 * 10**(-6)]
    d = 0

    for _ in range(N):
        x = []
        for i in range(m):
            t = []
            for j in range(n[i]):
                alpha = np.random.uniform(0, 1)
                t.append(-np.log(alpha) / lambd[i])

            for j in range(L[i]):
                l = np.argmin(t)
                t[l] -= np.log(np.random.uniform(0, 1)) / lambd[i]

            for j in range(n[i]):
                x.append(t[j])

        d += not LFSR(x)

    P = 1 - d / N
    return P

P0 = 0.995
L = [0, 0, 0, 0]

for i in range(1, 5):
    L[0] = i
    for j in range(1, 5):
        L[1] = j
        for k in range(1, 5):
            L[2] = k
            for z in range(1, 5):
                L[3] = z
                P = trace(L)
                if P > P0:
                    print(f'P={P}')
                    print(L)
                    print(sum(L))
