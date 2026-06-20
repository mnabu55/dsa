def is_happy_number(n):
    def sum_of_digits(num):
        sum_digits = 0
        while num > 0:
            num, digit = divmod(num, 10)
            sum_digits += digit ** 2
        return sum_digits

    if n == 1:
        return True

    slow = n
    fast = sum_of_digits(n)

    while not (fast == 1 or slow == fast):
        slow = sum_of_digits(slow)
        fast = sum_of_digits(sum_of_digits(fast))
        if fast == 1:
            return True
    
    return False


nums = [28, 4]
for num in nums:
    print(is_happy_number(num))
