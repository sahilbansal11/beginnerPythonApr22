class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # DO NOT TAKE ANY INPUT, INPUTS ARE PROVIDED IN THE FUNCTION
        # A is an INPUT
        # IGNORE self FOR NOW, WE WILL TALK ABOUT IT IN THE OOP CLASS

        counter = 1
        final_result = 0
        while counter <= A:
            if counter % 2 == 0:
                # if it's even, update the final_result
                final_result += counter
            counter += 1

        # DO NOT PRINT ANY OUTPUT
        # return THE OUTPUT
        return final_result

