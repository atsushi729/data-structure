class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert the binary strings to integers
        a_int = int(a, 2)
        b_int = int(b, 2)

        # Perform the binary addition
        sum_dec = a_int + b_int

        # Convert the result back to a binary string
        result = bin(sum_dec)[2:]

        return result

