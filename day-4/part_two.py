import math

input_start = 168888
input_end = 699999


def has_same_digits_adjacent_only_twice(n):
    digit_count = 1
    prev = n % 10
    has_same_digits = False
    while n > 1:
        n = math.floor(n / 10)
        cur = n % 10
        if prev == cur:
            digit_count += 1
        else:
            if digit_count == 2:
                has_same_digits = True
            digit_count = 1
        prev = cur
    return has_same_digits


def is_never_decreasing(n):
    prev = n % 10
    while n > 1:
        n = math.floor(n / 10)
        cur = n % 10
        if prev < cur:
            return False
        prev = cur
    return True


def is_valid(n):
    digit_count = 1
    has_same_digits_only_twice = False
    prev = n % 10
    while n > 1:
        n = math.floor(n / 10)
        cur = n % 10
        if prev < cur:
            return False
        if prev == cur:
            digit_count += 1
        else:
            if digit_count == 2:
                has_same_digits_only_twice = True
            digit_count = 1
        prev = cur
    return has_same_digits_only_twice


def valid_combinations(start, end):
    count = 0
    for n in range(start, end+1):
        if is_valid(n):
            count += 1
    return count


def main():
    print('from {0} to {1}'.format(input_start,input_end))
    print(valid_combinations(input_start, input_end))


if __name__ == '__main__':
    main()
