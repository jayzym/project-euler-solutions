sum_square = 0
square_sum = 0

for num in range(1, 101):
    sum_square += num ** 2
    square_sum += num

square_sum = square_sum ** 2

difference = square_sum - sum_square

print(difference)
