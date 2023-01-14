def fib(num: int):
    if num <= 1: 
        return num
    else:
        return fib(num - 2) + fib(num - 1)


if __name__ == "__main__":
    val = fib(4)
    print(val)