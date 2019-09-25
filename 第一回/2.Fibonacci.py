fibo = [1,1]
fibo = fibo + [fibo.append(fibo[i-1]+fibo[i-2]) for i in range (2,50)]
print(fibo[49]) # fibo(n)はn+1番目としてカウントされる。
