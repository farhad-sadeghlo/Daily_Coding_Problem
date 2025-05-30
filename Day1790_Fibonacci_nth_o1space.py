class FibonacciNthO1space:
    def __init__(self, n):
        self.n = n

    def fib(self):
        fib_lst = {}
        if self.n == 0:
            return 0
        elif self.n == 1:
            return 1
        else:
            fib_lst[self.n - 1] = FibonacciNthO1space(self.n - 2).fib() + FibonacciNthO1space(self.n - 1).fib()

        return fib_lst[self.n - 1]

#
if __name__ == "__main__":
    print(FibonacciNthO1space(int(input('Please type in the fibonacci number of interest: '))).fib())