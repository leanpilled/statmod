from geom import IRNGEO_1, IRNGEO_2, IRNGEO_3
from uniform import IRNUNI
from binom import IRNBIN, IRNBNL
from puasson import IRNPOI, IRNPSN


while True:
    print("1 - Geometric distribution")
    print("2 - Uniform distribution")
    print("3 - Binomial distribution")
    print("4 - Puasson distribution")
    
    dis = int(input("Enter the number of distribution type : "))
    
    if dis == 1:
        print("1 - IRNGEO_1")
        print("2 - IRNGEO_2")
        print("3 - IRNGEO_3")
        method = int(input("Select function : "))
        p = float(input("Enter value of p : "))
        if method == 1:
            print(IRNGEO_1(p))
        elif method == 2:
            print(IRNGEO_2(p))
        elif method == 3:
            print(IRNGEO_3(p))
    elif dis == 2:
        low, high = map(int, (input("Enter value of low and high : ").split()))
        print(IRNUNI(low, high))
    elif dis == 3:
        print("1 - IRNBIN")
        print("2 - IRNBNL")
        method = int(input("Select function : "))
        n, p = map(float, input("Enter values for N and p : ").split())
        if method == 1:
            print(IRNBIN(n, p))
        elif method == 2:
            print(IRNBNL(n, p))
    elif dis == 4:
        print("1 - IRNPOI")
        print("2 - IRNPSN")
        method = int(input("Select function : "))
        mu = float(input("Enter values for mu : "))
        if method == 1:
            print(IRNPOI(mu))
        elif method == 2:
            print(IRNPSN(mu))
    else:
        print(f"Invalid distribution type : {dis}")
        
        