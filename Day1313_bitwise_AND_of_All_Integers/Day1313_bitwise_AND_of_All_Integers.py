class BitwiseAND():
    def __init__(self, M:int, N:int):
        self.M = int(M)
        self.N = int(N)
    def Bitwise_AND(self):
        result = {}
        for i in range(self.M, self.N):
            for j in range(self.M + 1, self.N + 1):
                result[str(i) + ' & ' + str(j)] = i & j
        return result