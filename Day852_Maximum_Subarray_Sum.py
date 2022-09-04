# Given a circular array, compute its maximum subarray sum in O(n) time. A subarray
# can be empty, and in this case the sum is 0.

# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8
# where the 8 is obtained from wrapping around.

# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

class max_subarray:
    def __init__(self, lst: list):
        self.lst = list(map(int, lst.rstrip().split()))
        self.the_sum = 0
        # print(self.lst)
    def calc_max_subarray(self):
        for subarray in self.lst:
            subarray = int(subarray)
            if subarray > 0:
                self.the_sum += subarray
        return print(self.the_sum)
