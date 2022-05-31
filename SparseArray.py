class SparseArray(object):
    def __init__(self, items=0):
        self.L = [0] * items
    def __setitem__(self, j, e):
        self.L[j] = e
    def __getitem__(self, j):
        return self.L[j]
    def __str__(self):
        return str(self.L)

sa = SparseArray(6)
sa[0] = (12, "sheeesh")
sa[1] = (21, "deep")
sa[2] = (51, "meaning")
sa[3] = (76, "yan")
sa[4] = (108, "ang ")
sa[5] = (420, "means ")
print("Sparse Array Content: \n", sa)