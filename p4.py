def reverse(num):
    rev = 0

    while(num != 0):
        r = int(num % 10)
        rev = rev * 10 + r
        num = int(num / 10)
    return rev

num = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        new_num = i * j
        if new_num == reverse(new_num) and new_num > num:
            num = new_num

print(num)
