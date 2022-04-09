from numpy import *
v=random.randint(1,100,60).reshape(20,3) # list of subjects
M=10000 # max mass of backpack
Max=0;
ans=[]
mas=0
mass=set()
v=[*v]
v.sort(key=lambda el:el[1]/el[0],reverse=True);
def f(i,tm,s,a):
    global Max,ans,mas,mass
    a=a.copy()
    o=v[i]
    if i in a and a[i]+1>o[2]:
        return False
    if tm+o[0]>M:
        return False
    if tm+o[0] in mass:
        return False
    if s+(M-tm)*o[1]/o[0]<=Max and Max!=0:
        return False
    tm+=o[0]
    s+=o[1]
    if not i in a:
        a[i]=0
    a[i]+=1
    mass.add(tm)
    flag=False;
    for k,_ in enumerate(v):
        F=f(k,tm,s,a)
        flag = flag or F
    if flag == False:
        # print(a,i,tm,s); intermediate steps
        if s>Max:
            Max=s
            ans=a.copy()
            mas=tm
    return True
f(0,0,0,{})
print(ans,mas,Max)