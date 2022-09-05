# Given a circular array, compute its maximum subarray sum in O(n) time. A subarray
# can be empty, and in this case the sum is 0.

# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8
# where the 8 is obtained from wrapping around.

# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

class max_subarray:
    def __init__(self, lst: list, subarray_length):
        self.lst = list(map(int, lst.rstrip().split()))
        self.the_sum = 0
        self.subarray_len = int(subarray_length)
        self.subarray = []
        self.subarray_and_indices = {}
    def calc_max_subarray(self):
        counter = 0

        self.lst_sorted = sorted(self.lst, reverse=True)

        for subarray in self.lst_sorted:

            if subarray > 0:

                self.the_sum += subarray

                self.subarray.append(subarray)

                counter += 1

                if counter == self.subarray_len:

                    break

        for i, num in enumerate(self.lst):

            if num in self.subarray:

                self.subarray_and_indices[i] = num

        return print(self.the_sum, self.subarray_and_indices)
