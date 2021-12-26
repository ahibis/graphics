for i in range(1,100000):
    a=i**10;
    s=0;
    digits=[]
    while a>0:
        digits.append(a%10)
        a//=10
    digits.reverse()
    if sum(digits) == i:
        print(f"5∜{i**10}={'+'.join(map(str,digits))}")
        