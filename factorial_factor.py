def factors(x):
    f=[]

    if x==0 or x<0:
        return None
    for i in range(1, x + 1):
       if x % i == 0:
           f.append(i)
    return f


def factorial(x):

    if x == 1 or x==0 :
        return 1
    if x<0:
        return None
    else:
        return (x * factorial(x-1))