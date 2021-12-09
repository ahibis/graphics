a=[1, 4, 5, 14, 10, 17, 6, 12, 3, 11]
d=3
Max=[(0,0)]*3
for i,e in enumerate(a):
    if Max[0][0]<e:
        Max[2]=Max[1]
        Max[1]=Max[0]
        Max[0] = (e,i)
        continue
    if Max[1][0]<e:
        Max[2]=Max[1]
        Max[1]=(e,i)
        continue
    if Max[2][0]<e:
        Max[2]=(e,i)
        continue
print(Max)

