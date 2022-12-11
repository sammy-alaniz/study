import math

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        
        n = len(s)
        sections = math.ceil(n / (2 * num_rows - 2.0))
        num_cols = sections * (num_rows - 1)
        
        matrix = [[' '] * num_cols for _ in range(num_rows)]
        
        curr_row, curr_col = 0, 0
        curr_string_index = 0
        
        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while curr_string_index < n:
            # Move down.
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1
                
            curr_row -= 2
            curr_col += 1
            
            # Move up (with moving right also).
            while curr_row > 0 and curr_col < num_cols and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1
        
        answer = ""
        print(matrix)
        for row in matrix:
            answer += "".join(row)
            
        return answer.replace(" ", "")

    def convert_two(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        zigzag = ['' for i in range(numRows)]
        row=0
        switch=True
        for i in s:
            zigzag[row]+=i
            if switch:            
               row+=1
            else:
                row-=1
            if row==numRows-1:
                switch=False
            if row==0:
                switch=True
            print(zigzag)
        return ''.join(zigzag)


if __name__ == "__main__": # this is how you set up a main function in python
    row = 3
    sol = Solution()
    output = sol.convert('Sammy', row)
    print(output)

    output_two = sol.convert_two('Sammy', row)
    print(output_two)
