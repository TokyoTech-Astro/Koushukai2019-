p=[]
t=2
while len(p)<100:
    for i in p:
        if t%i==0:
            break
    else:
        p.append(t)
    t+=1
print(p[99])