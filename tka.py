"""
условия
"""
ruls=[
    "1021R",
    "1120L",
    "2001S",
    "2111L"
]
P = "101q011"
s = "1" #начальное значение
f = "0" #конечное значение
K = 50 # максимальное кол-во операций
Nice = True # упрощеная запись
'''
программа
'''
si = P.find("q")
if(~si):    
    P = P[:si]+P[si+1:]
k=1
space="0"*K;
p=space+P+space;
lspace=len(space);
i=lspace+si;
iL=lspace;
iR=len(space+P)-1;
flags={
    'L':-1,
    'S':0,
    'R': 1
}
def setChar(str,i,char):
    s=[*str]
    s[i] = char
    return "".join(s);
def up(i):
    lets="⁰¹²³⁴⁵⁶⁷⁸⁹"
    s = str(i)
    return "".join(list(map(lambda a:lets[int(a)], s)))

def down(i):
    lets="₀₁₂₃₄₅₆₇₈₉"
    s = str(i)
    return "".join(list(map(lambda a:lets[int(a)], s)))
def nice(str):
    str+=" "
    res = ""
    t = ""
    i = 0
    for l in str:
        if l == t:
            i+=1
        else:
            res+=t  
            if i > 1:
                res+=up(i)
            i=1
            t=l
    return res

while True:
    ans=f"{p[iL:i]}q{down(s)}{p[i:iR+1]}"
    if Nice:
        ans=nice(ans)
    print(f"{k}) {ans}")
    if k == K:
        break;
    if s == f:
        break;
    F = False
    for rul in ruls:
        if s == rul[0] and p[i] == rul[1]:
            s = rul[2]
            p = setChar(p, i, rul[3])
            i += flags[rul[4]];
            if i<iL:
                iL = i 
            if i>iR:
                iR = i
            F=True
            break;
    k+=1
    if F == False:
        break;