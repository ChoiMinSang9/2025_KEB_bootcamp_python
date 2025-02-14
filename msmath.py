def my_abs(n) -> int:
    """
    Retrun absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n < 0:
        return -n
    return n


def fibonacci_loop(n) -> int:
   """
   Calculate fibonacci number
   :param n:
   :return: result of value fibonacci
   """
   n_list = [0, 1]
   for i in range(n + 1):
       n_list.append(n_list[i] + n_list[i + 1])

   return n_list[n]


def fibonacci_recursion(n) -> int:
    """
    Calculate fibonacci number
    :param n:
    :return: result of value fibonacci
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)