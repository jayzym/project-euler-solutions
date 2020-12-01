import math

def get_triplets():
    a = 0
    b = 1

    while True:
        product = 0
        a += 1
        b = a + 1

        while product <= 1000:
            c = math.sqrt((a**2) + (b**2))
            product = a + b + c
            if product == 1000:
                print(str(a*b*c))
                return

            else:
                b += 1

get_triplets()
