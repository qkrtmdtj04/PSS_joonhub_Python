N = int(input())

fibo = [0, 1]
p = 1000000//10*15

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= 1000000

print(fibo[N%p])