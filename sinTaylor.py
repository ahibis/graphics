from math import pi,e
def sin(x):
    ex=0.00000000001
    ans=0
    n=2
    while x>2*pi:
        x-=2*pi
    term=x    
    while abs(term)>ex:
        ans+=term
        term*=-x*x/(2*n-2)/(2*n-1)
        n+=1
    print(n)
    return ans

E=[(2**i,e**(2**i)) for i in range(-6,7)]
E.reverse()
def lnZ(x):
    n=0
    res=1
    for i,ei in E:
        if res*ei<x:
            res*=ei
            n+=i
    return([n,res])

def ln(x):
    x0,xs = lnZ(x)
    x/=xs
    x-=1
    
    ex=0.000000000001
    ans=0
    n=2
    term=x
    while abs(term)>ex:
        ans+=term
        term*=-x*(n-1)/n
        n+=1
    print(n)
    return ans+x0

print(ln(100))

