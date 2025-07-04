def fib(self, n: int) -> int:
    def fibonacci_dynamic(n):
        if n == 0:
            return 0
        fib_list = [0, 1]
        for i in range(2, n + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[n]

    return fibonacci_dynamic(n)