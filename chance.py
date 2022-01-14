from numpy import *
def f():
    chances = random.randint(0,2,1000)
    rnd1 = random.randint(0,2,1000)
    guess = [0]*2
    scores = 0
    for i,e in enumerate(chances):
        #tk=min(enumerate(guess),key=lambda x: x[1])[0]
        #tk = rnd1[i]
        tk=0
        if tk == e:
            scores+=1
        else:
            scores-=1
        guess[e] +=1
    return scores
scores=0
victories=0
print("очки за каждый раунд")
for i in range(200):
    s=f()
    print(s,sep=" ",end=" ")
    if s>=0:
        victories+=1
    scores+=s
print(f"\n общее число очков {scores} побед {victories}/200")