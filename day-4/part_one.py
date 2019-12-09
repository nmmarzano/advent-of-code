import math

input_start = 168888
input_end = 699999


def is_valid(n):
    has_same_digits = False
    prev = n % 10
    while n > 1:
        n = math.floor(n / 10)
        cur = n % 10
        if prev < cur:
            return False
        if prev == cur:
            has_same_digits = True
        prev = cur
    return has_same_digits


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
