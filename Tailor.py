K=10
def round(x,dx=0.0001):
    x/=dx
    if x%1>=0.5:
        x//=1
        x+=1
    else:
        x//=1
    x*=dx
    return x
def getDer(f,x,k=5,dx=0.0001):#f-функция x-точка в которой нужно найти производную k-колличество производных dx-шаг
    F=[]
    answer=[]
    for i in range(k+1):
        F.append(f(x+i*dx))
    answer.append(F[0]);
    for i in range(k):
        for j in range(k-i):
            F[j]=(F[j+1]-F[j])/dx
        answer.append(F[0]);
    return answer
FACT=[0]*1000;

def fact(x):#нахождение факториала x
    if FACT[x]!=0:
           return FACT[x]
    if x==0:
        FACT[x]=1
        return FACT[x]
    FACT[x]=fact(x-1)*x
    return FACT[x]

def Taylor(f,x,k=5,dx=0.0001):#нахождение коэффициэнтов Тейлора
    dev=getDer(f,x,k,dx)
    for i in range(k+1):
        dev[i]/=fact(i)
        dev[i]=round(dev[i],dx)
    return dev


def printTaylor(f,x,k=5,dx=0.0001):
    taylor=Taylor(f,x,k,dx)
    answer='';
    for i in range(k+1):
        if taylor[i]==0:
            continue;
        if i==0:
            answer+=f"+{taylor[i]}"
            continue;
        if x==0:
            if i==1:
                answer+=f"+{taylor[i]}x"
                continue;
            answer+=f"+{taylor[i]}x^{i}"
            continue;
        if i==1:
            answer+=f"+{taylor[i]}(x-{x})"
            continue;
        answer+=f"+{taylor[i]}(x-{x})^{i}"
    print(answer[1::])
f=lambda x:x**3;
print("функцию x^3 можно разложить как")
printTaylor(f,1,5,0.00001)
print('\n'.join("1,2,3".split(",")))