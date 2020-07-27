sum = 0
num = 1
previous_num = 1

while num < 4000000:
    new_num = num + previous_num
    if new_num % 2 == 0:
        sum += new_num
    previous_num = num
    num = new_num

print(sum)

