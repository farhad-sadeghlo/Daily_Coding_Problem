class PushPopPull:
    def __init__(self):
        self.stack = []
    def push(self):
        while True:
            x = input('Please provide your num: ')
            if x != '':
                self.stack.append(int(x))
            else:
                break

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        if self.stack:
            return self.stack[len(self.stack) - 1]
        else:
            return -1

    def pull(self):
        if self.stack:
            return self.stack.pop(len(self.stack) - 1)
        else:
            return -1
