from numpy import *
import pandas as pd

arr=fromstring("\
    15 7 4 9 10 13 \
    15 7 15 9 7 7 \
    7 7 1 15 2 4 \
    2 3 6 4 17 14 \
    18 4 15 7 14 6\
    12 16 3 4 3 10",sep=" ").reshape(6,6)
N = arr.shape[0]    
strNames = [1,2,3,4,5,6,"min"];
colNames = [1,2,3,4,5,6,"min"];
zer = zeros((N,N))
size=0
path = []
def Print():
    a = arr.copy();
    
    minStr=a.min(axis=0)
    minCol=a.min(axis=1)
    w=sum(minStr)+sum(minCol)
    b=insert(a,N,minStr,axis=0)
    tab = insert(b,N,append(minCol,w),axis=1)
    print(pd.DataFrame(tab,index=strNames,columns=colNames))
def Print1():
    print(pd.DataFrame(arr,index=strNames[0:N],columns=colNames[0:N]))
def PrintZer():
    print(pd.DataFrame(zer,index=strNames[0:N],columns=colNames[0:N]))
while N>1:
    Print()
    minCol=arr.min(axis=1)
    for i, str in enumerate(arr):
        str -= minCol[i]
    minStr=arr.min(axis=0)
    size+=sum(minCol)+sum(minStr);
    print("Вычитаем наименьшие элементы по строкам")
    Print()
    for i, col in enumerate(arr.T):
        col -= minStr[i]
    print("Вычитаем наименьшие элементы по столбцам")
    Print1()
    zer=zeros((N,N))
    for i in range(N):
        for k in range(N):
            if arr[i,k] == 0:
                zer[i,k] = min(delete(arr[i],k)) + min(delete(arr.T[k],i))
            else:
                zer[i,k] = 0
    print("вычисляем веса нулей")
    PrintZer()
    maxI=argmax(zer)
    I = maxI // N
    K = maxI % N
    path.append((colNames[I],strNames[K]))
    Ii=colNames[I];
    Kk=strNames[K];
    print(f"удаляем строку и столбец {Ii},{Kk}")
    arr=delete(arr,I,axis=0)
    arr=delete(arr,K,axis=1)
    colNames = delete(colNames,K)
    strNames = delete(strNames,I)
    if((Kk.__str__() in strNames) and (Ii.__str__() in colNames)):
        k1=where(strNames == Kk.__str__())[0][0]
        i1=where(colNames == Ii.__str__())[0][0]
        arr[k1][i1]=inf;
    N-=1
path.append((strNames[0],colNames[0]))
Print1()
print(f"путь {path} занял {size}")