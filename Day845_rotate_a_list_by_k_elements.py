class listRotator:

    def __init__(self, lst, num):

        self.lst = lst.replace("[", '').replace("]", '').replace(" ", '').split(',')
        self.num = list(num)
        for num in self.num:
            if num in self.lst:
                self.numloc = self.lst.index(num)

    def rotator(self):

        num_index = self.numloc
        count = len(self.lst)
        newlist = [self.lst[i] for i in range(num_index + 1, count)]
        newlist.extend(self.lst[i] for i in range(num_index + 1))

        return print(newlist)

