class listRotator:

    def __init__(self, lst, num):

        self.lst = list(map(int, lst.rstrip().split()))
        self.num = int(num)
        print(self.lst)
        # for num in self.num:
        if self.num in self.lst:
            self.numloc = self.lst.index(self.num)

    def rotator(self):

        num_index = self.numloc
        count = len(self.lst)
        newlist = [self.lst[i] for i in range(num_index + 1, count)]
        newlist.extend(self.lst[i] for i in range(num_index + 1))

        return print(newlist)

