# Github Repo link
#https://github.com/ceewee12/03230030_BIA101_CAPIII
# Name:Choki wangmo
# BBI A
# 03230030

# reference
# https://youtu.be/55I-LENFJbI
# https://www.w3schools.com/python/python_regex.asp
#https://www.youtube.com/watch?v=5-7u-dUbin0
#https://www.youtube.com/watch?v=EzeeypMKx7os

#solution
#solution score : 480909

# Read the input.txt file
# importing re to find digit in inputfile
# importing regular expression
import re
class SumCalculator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_lines = self.fetch_input()
        self.total_sum = self.compute_sum()
     
#reading the file.txt
    def fetch_input(self):
        file = open(self.input_file, "r")
        input_lines = file.readlines()
        return input_lines
    

    def compute_sum(self):
        total_sum = 0
        for sent in self.input_lines:
            # Extract digits from the line
            digits = re.findall(r'\d', sent)

            # If the line contains at least two digits
            if len(digits) >= 2:
                # Extract the first and last digits
                f_digit = int(digits[0])
                l_digit = int(digits[-1])

                # Construct the two-digit number
                number = f_digit * 10 + l_digit

                # Add the number to the total sum
                total_sum += number

        return total_sum
    # solution
    def print_solution(self):
        print(f"The total sum from the given input file {self.input_file} is {self.total_sum}")
# Main function
def main():
    # Assuming input file
    input_file = "03230030_BIA101_CAPIII\\030.txt"
    calculator = SumCalculator(input_file)
    calculator.print_solution()

# Call the main function
main()
