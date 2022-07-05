class Palindrome:

    def __init__(self, digit):

        self.digit = digit

    def symmetrical(self):

        digit_count = len(str(self.digit))

        while digit_count > 0:

            if self.digit % 10 != self.digit // (10 ** (digit_count - 1)):

                return print('The number is not a palindrome')

            self.digit = self.digit % (10 ** (digit_count - 1))
            self.digit = self.digit // 10
            digit_count = len(str(self.digit))

            if digit_count < 2:

                return print('The number is a palindrome')

        # return (print('The number is a palindrome'))
