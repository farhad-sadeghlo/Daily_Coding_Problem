import numpy as np
import math

class MonteCarlo:

    """
    For reference please read:
    1. https://www.cs.cornell.edu/jwoller/samples/montecarlo/
    2. https://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/compute-pi.html
    """

    def __init__(self, rand_num):

        self.rand_num = int(rand_num)
        self.throwcounts = 0
        self.incirclecounts = 0

    def pi_num_by_montecarlo(self):

        for _ in range(self.rand_num):

            xthrows = np.abs(np.random.random())
            ythrows = np.abs(np.random.random())
            self.throwcounts += 1

            if math.pow(xthrows, 2) + math.pow(ythrows, 2) <= 1.0:

                self.incirclecounts += 1

        pi_num = 4 * (self.incirclecounts / self.throwcounts)

        return print(f'pi number is: {pi_num:.3f}')
