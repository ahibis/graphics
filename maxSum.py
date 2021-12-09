def MAX(a, d=1, r=0,i=-1):#находит максимальный имеющий остаток r при делении на d кроме значений с индексом i
    return max(enumerate(a),key= lambda e:e[1] if e[1]%d==r and e[0]!=i else -100)

a=[1, 4, 5, 14, 10, 17, 6, 12, 3, 11]
d = 5
r = 3
sums=[0]*5
for i in range(d):
    k,max1 = MAX(a,d,i);
    k,max2 = MAX(a,d,(d+r-i)%5,k);
    sums[i] = (max1+max2,max1,max2)
print(sums)
print(f"максимальная сумма {max(sums)}")