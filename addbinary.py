class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Problem focuses on bit manipulation.
        # Collect result in an array in reverse.
        # Then put it back to normal.

        # Initialize variables
        out = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Conditionals deal with cases like 1010 + 101
            oper1 = a[i] if i >= 0 else '0'
            oper2 = b[j] if j >= 0 else '0'
            # Note four possible totals: 0, 1, 2, 3
            total = (oper1 == '1') + (oper2 == '1') + carry
            # If sum is greater than 1, carry gets the result of total // 2.
            carry = total // 2 
            # the value on the space is 1, if the total is 1 or 3.
            out.append('1' if total % 2 == 1 else '0') 
            i -= 1
            j -= 1
        return ''.join(reversed(out))