#Parity
#The brute-force algorithm iteratively tests the value of each bit
#The time complexity isO(n), where n is the word size.
def parity (x):
    result = 0
    while x:
        result ^= x & 1         # MOD 2
        x >>= 1                 # X / 2    
    return result

#Parity X-1
#Let k be the number of bits set to 1 in a particular word. (For example, for 10001010,
#k = 3.) Then time complexity of the algorithm below is O(k).
def parity(x):
    result = 0
    while x:
        result ^= 1 
        x &= x-1    #Drops the lowest set bit of x.
    return result

print(parity(0b10010))

a = 0b1101
print(parity(a))