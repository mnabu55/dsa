def is_happy_number(num):
    seen = {}
    current = num

    while True:
        current = sum_of_digits(current)
        if current == 1:
            return True
        if current in seen:
            return False
        seen[current] = True
    

def sum_of_digits(num):
    sum_digits = 0
    while num != 0:
        num, digit = divmod(num, 10)
        sum_digits += digit ** 2
    return sum_digits


nums = [28, 4]
for num in nums:
    print(is_happy_number(num))
