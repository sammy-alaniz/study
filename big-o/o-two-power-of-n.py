def fib(num: int):
    print('fib called num is ', num)
    if num <= 1: 
        return num
    else:
        return fib(num - 2) + fib(num - 1)


if __name__ == "__main__":
    print('\n the fib function finds the fibonanci number at a given index')
    sequence = '0, 1, 1, 2, 3, 5, 8, 13, 21, 34'
    print('finonanci sequence : ', sequence)
    val = fib(5)
    print(val)