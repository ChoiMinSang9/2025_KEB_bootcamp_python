# v1.0) for -> while
# v1.1) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.2) **대신 pow 함수
# v1.3) **연산자, pow 함수를 사용하지 않고 커스텀 함수를 만들어 동작 my_pow

import math


# assume exp is positive integer
def my_pow(base, exp) -> float:
    """
    밑과 지수를 입력받아 거듭제곱 함수를 만듦
    :param base: base number
    :param exp: exponent
    :return: the power result in the form
    """
    result = 1
    for k in range(exp):
        result = result * base

    return result


def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False
    if it is not a prime number

    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i * i < num:
            if num % i == 0:
                return False

            i += 1

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
