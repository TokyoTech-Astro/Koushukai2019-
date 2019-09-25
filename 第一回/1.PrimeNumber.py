def nth_prime(n):
    prime_list = [2]
    start_number = 3

    while len(prime_list) < n:

        for p in prime_list:
           
            if start_number % p == 0:
                
                break

        else:
           
            prime_list.append(start_number)

        
        start_number += 2

    
    return prime_list[-1]

print(nth_prime(100))
