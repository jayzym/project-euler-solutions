import math

num = 600851475143
prime = 0

while num % 2 == 0: 
        prime = 2
        num /= 2 

for i in range(3, int(math.sqrt(num)), 2):
    while num % i == 0:
        prime = i
        num = num / i

if num > 2:
     maxPrime = num

print(prime)
