"""
Reverse bits of a given 32 bits unsigned integer.
"""
def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.zfill(32)
        n = [int(n[i]) for i in range(len(n))]

        s = 0
        stepen_of_2 = 1
        for i in range(32):
            s += stepen_of_2 * n[i]
            stepen_of_2 *= 2
            
        return s    
