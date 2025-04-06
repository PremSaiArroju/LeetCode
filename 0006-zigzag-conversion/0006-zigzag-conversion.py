class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only 1 row or string is shorter than numRows, return as is
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list to store strings for each row
        rows = [''] * numRows

        # Start at the first row and set the initial direction
        current_row = 0
        moving_down = False

        # Go through each character in the string
        for char in s:
            # Add character to the current row
            rows[current_row] += char

            # If we're at the top or bottom, change direction
            if current_row == 0 or current_row == numRows - 1:
                moving_down = not moving_down  # Flip direction

            # Move current_row up or down based on the direction
            if moving_down:
                current_row += 1
            else:
                current_row -= 1

        # Combine all rows to get the final result
        return ''.join(rows)