
def check_nums(num):
    for n in range(1,21):
        if num % n != 0:
            return False
    return True

num = 20

while True:
    if check_nums(num):
        print(num)
        break
    else:
        num += 20
