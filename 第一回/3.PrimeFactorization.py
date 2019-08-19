n=int(input())
l=[]
while 1:
    for i in range(2,n//2+1):
        if n%i==0:
            l.append(i)
            n//=i
            break
    else:
        l.append(n)
        break
print(l[0],end=" ")
for i in range(1,len(l)):
    print("×",l[i],end=" ")