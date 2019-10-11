def main(n):
    listA  = [0] * (n + 1)
    return Fibonacci(n,listA)

def Fibonacci(n,listA):
    if listA[n] != 0:
        pass
    elif n <= 2:
        listA[n] = 1
    else:
        listA[n] = Fibonacci(n-1,listA) + Fibonacci(n-2,listA)
    
    return listA[n]

if __name__ == "__main__":
    print(main(500))
