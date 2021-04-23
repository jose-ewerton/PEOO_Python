class num:
    def __init__(self, n=0):
        self.n = n

    def __len__(self):
        return self.n


s1 = num(322)
print(len(s1))