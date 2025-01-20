class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """

        # Pre process matrix
        row, col = len(mat), len(mat[0])

        # Track painted counts for each row and column
        # 0 means not set.
        rows = [0] * row
        cols = [0] * col

        # Map each matrix value to its coordinates (row, column)
        map = {mat[r][c]: (r, c) for r in range(row) for c in range(col)}

        # Check if a row's value in the map is the length, same with columns.
        for i in range(len(arr)):
            r, c = map[arr[i]] # Get the row and column for the current value
            rows[r] += 1 # Increment the painted count for the corresponding row
            cols[c] += 1 # Increment the painted count for the corresponding column

            # Check if any row or column is fully painted
            if rows[r] == col or cols[c] == row:
                return i