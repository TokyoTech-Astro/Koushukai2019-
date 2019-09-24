n = int(input())
listA = []
i = 2
while n > 1:
    if n % i == 0:
        listA.append(i)
        n = n // i
    else:
        i += 1
print(listA)    
