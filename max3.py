from math import inf
#найти наибольшую сумму кратную 10
def MAX(a, k=1,ai=[]):#находит максимальный кратный k кроме значений индексами ai
    return max(enumerate(a),key= lambda e:e[1] if e[1]%k==0 and not e[0] in ai else -inf)

a=[3, 4, 5, 15, 10, 17, 6, 12, 3, 11]
d=12
ps=[(12,1,1),(6,2,1),(4,3,1),(3,2,2)]
ans=[]
maxv=-inf
for p in ps:
    ai=[-1]*3
    maxs=[0]*3
    for i,k in enumerate(p):
        ai[i],maxs[i] = MAX(a,k,ai)
    print(f"{maxs[0]}*{maxs[1]}*{maxs[2]}={maxs[0]*maxs[1]*maxs[2]}")
    if maxs[0]*maxs[1]*maxs[2]>maxv:
        ans=(maxs[0],maxs[1],maxs[2],maxs[0]*maxs[1]*maxs[2])
        maxv=maxs[0]*maxs[1]*maxs[2]
print(f"ответ:{ans[0]}*{ans[1]}*{ans[2]}={ans[0]*ans[1]*ans[2]}")
