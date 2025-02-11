# v1.0) for -> while
# v1.1) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.2) **대신 pow 함수

def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False
    if it is not a prime number

    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        # for i in range(2, int(num ** 0.5) + 1):
        while i <= int(num ** 0.5) + 1:
            if num % i == 0:
                return False

            i += 1
            # is_prime = False  # count = count + 1
            # break
            # print(i, end=' ')
    else:
        return False

    return True


def print_prime_between(a, b):
    if a > b:
        a, b = b, a
    num = a
    while num <= b:
        if is_prime(num):
            print(num, end=" ")
        num += 1


# main
begin = int(input("input begin int: "))
end = int(input("input end int: "))

print_prime_between(begin, end)
