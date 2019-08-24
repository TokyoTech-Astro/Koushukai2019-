x = int(input("Prime Factorization : input number to test: "))
factorization_list = []
i = 2

while i<=x:
    while x%i == 0:
        
        factorization_list.append(i)
        i = i
        x = x/i
    else:
        
        i += 1

        continue
       
    


print(factorization_list)
