import math


def cagr_berechnung(AK, EK, t):
    print( ((EK/AK)**(1/t))-1 )
    
    AK = 100
    EK = 700
    t = 30
    
    
    return cagr_berechnung(AK, EK, t)
    return cagr_berechnung()
    return (abs(cagr_berechnung(AK, EK, t)))

def cagr_berechnung(AK, EK, t):
    AK = abs(AK)
    EK = abs(EK)
    t = abs(t)
    cagr = (EK/AK)**(1/t)-1
    return cagr

x= cagr_berechnung(100, 700, 30)

print(x)


AK = 120
t = 30

EK_2 = AK * (1+x)**t

print(EK_2)


