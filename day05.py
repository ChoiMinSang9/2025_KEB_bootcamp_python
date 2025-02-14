def fibo_recursion(n) -> int:
    """
    fibonacci version recursion
    :param n: integer
    :return: result of fibonacci
    """
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursion(n - 2) + fibo_recursion(n - 1)


def fibo_loop(n) -> int:
    """
        fibonacci version loop
        :param n: integer
        :return: result of fibonacci
        """
    n_list=[0,1]
    for i in range(n+1):
        n_list.append(n_list[i]+n_list[i+1])

    return n_list[n]

n=int(input())
print(fibo_loop(n))    #fast speed
print(fibo_recursion(n))    #low speed
