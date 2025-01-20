class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Initial notes
        """
        Circular array + Sliding Window
        Window size is k
        
        Brute force: 3 situations to take in account:

        If k > 0, replace the ith number with the sum of the next k numbers.
        If k < 0, replace the ith number with the sum of the previous k numbers.
        If k == 0, replace the ith number with 0.
        
        """

        result = [0 for i in range(len(code))] 
        # Deal with the k == 0 case, initialise array to be the result of the k == 0 case.
        if k == 0:
            return result
        
        # Both of the other cases need to iterate through the size of the code array.
        for i in range(len(result)):

            # Deal with k > 0 case
            if k > 0:

                # start from the second index of the array (1), to the window size k, 
                # to add up the next k numbers
                for j in range(i + 1, i + k + 1):
                    # Modulo can help with iterating through ciruclar arrays.
                    # if k = 3, 4 % k is 1, going right back to 1, and 5 % k, goes to 2.
                    # With the range i + 1, i + k + 1 we can replace each index with the sums.
                    result[i] += code[j % len(code)]
            
            # Deal with k < 0 case
            if k < 0:

                # Go reverse in indices.
                for j in range(i - abs(k), i):
                    result[i] += code[(j + len(code)) % len(code)]

        return result
    
    # Solution 2 copied from Leetcode solutions

    """
    Create an array result of the same length as code to store the decrypted values.
    If k is 0, return result, since all values should be zero.
    Set initial start and end indices based on k.
        If k > 0:
            Set start = 1 and end = k.
        If k < 0:
            Set start to code.length - |k| and end to code.length - 1.
    Calculate the initial sum of elements from start to end.
    Loop through each index i in code:
        Store the current sum in result[i].
        Update sum by subtracting the element at start and adding the element at end + 1, using modulo to handle wrapping around the array.
        Increment start and end by 1 to slide the window right.
    Return the result array with the decrypted values.

    """
    def decrypt2(self, code, k):
        result = [0 for _ in range(len(code))]
        if k == 0:
            return result
        # Define the initial window and initial sum
        # This is the "sliding window"
        start, end, window_sum = 1, k, 0
        # If k < 0, the starting point will be end of the array.
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        for i in range(start, end + 1):
            window_sum += code[i]
        # Scan through the code array as i moving to the right, update the window sum.
        # The window is sliding in each iteration as the start and end values pointers are moving forward.
        # The % len(code) ensures that the indices wrap around (circular behavior).
        for i in range(len(code)):
            result[i] = window_sum
            # Subtract the value at the start index
            window_sum -= code[start % len(code)]
            # Add the value at the next index after end
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
        return result

