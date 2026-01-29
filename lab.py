import math

def hypotenuse(a, b): #DONE
    A2 = a ** 2
    B2 = b ** 2
    C2 = A2 + B2
    H = math.sqrt(C2)
    return H

def num_digits(n): #DONE
    N2 = len(str(n))
    return N2

def tip_amount(total, percent): #DONE
    tip = total * (percent / 100)
    return round(tip, 2)
