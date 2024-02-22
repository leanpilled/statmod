from chisquare import RNCHIS
from exp import RNEXP
from normal import RNRM1, RNRM2
from student import RNSTUD


while True:
    print("1 - chisquare distribution")
    print("2 - exponential distribution")
    print("3 - normal distribution")
    print("4 - student distribution")
    
    dis = int(input("Enter the number of distribution type : "))
    
    if dis == 1:
        N = int(input("Enter value of N : "))
        print(RNCHIS(N))
    elif dis == 2:
        b = float(input("Enter value of b : "))
        print(RNEXP(b))
    elif dis == 3:
        print("1 - RNRM1")
        print("2 - RNRM2")
        method = int(input("Select function : "))
        if method == 1:
            print(RNRM1())
        elif method == 2:
            m, sigma = map(float, input("Enter values for m and sigma : ").split())
            print(RNRM2(m, sigma))
    elif dis == 4:
        N = float(input("Enter value of N : "))
        print(RNSTUD(N))
    else:
        print(f"Invalid distribution type : {dis}")
        
        