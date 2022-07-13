def factors(x):
    f=[]
    for i in range(1, x + 1):
       if x % i == 0:
           f.append(i)
    return f
