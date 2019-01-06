# First, you will want to create a text file containing 100 (or a smaller number, if you're less cruel than I am)
# exercises.  Each exercise will involve addition (+) and subtraction (-) of four randomly chosen positive and
# negative integers.  Let's say that the integers should range from -40 to 40, but it shouldn't be too hard to adjust
# that range as necessary.
#
# Here is what the first five lines of the file might look like:
#     [  1]   19 - (   1) - (   4) + (  28) = ______
#     [  2]  -18 + (   8) - (  16) - (   2) = ______
#     [  3]   -8 + (  17) - (  15) + ( -29) = ______
#     [  4]  -31 - ( -12) - (  -5) + ( -26) = ______
#     [  5]  -15 - (  12) - (  14) - (  31) = ______
#
# Notice that I've tried to keep everything aligned, and that I put parentheses around all numbers, since he's new to
# negative numbers and can get confused by the whole "- -" thing.
#
# Second, I want you to write a program that reads through the lines of this text file and calculates the solution for
# each of these lines.  The output from this program should look like:
#
#     [  1]   19 - (   1) - (   4) + (  28) = 42
#     [  2]  -18 + (   8) - (  16) - (   2) = -28
#     [  3]   -8 + (  17) - (  15) + ( -29) = -35
#     [  4]  -31 - ( -12) - (  -5) + ( -26) = -40
#     [  5]  -15 - (  12) - (  14) - (  31) = -72
#
# I'm enclosing a simple set of tests; I'm still feeling a bit under the weather, and didn't have a chance to explore
# tmp_path as much as I had wanted.  I have some ideas for further tests, but I'll see if I can create those during
# the week.
import random

MAX_NUM = 40
MIN_NUM = -40
NUM_PROBLEMS = 100

NUMS = list(range(MIN_NUM,MAX_NUM))
OPERANDS = ['-', '+'] * 3
FORMAT='[{:3}]  ({:3}) {} ({:3}) {} ({:3}) {} ({:3}) = _____'

def create_math_problems(outfile):
    for i in range(NUM_PROBLEMS):
        sn = random.sample(NUMS, 4)
        so = random.sample(OPERANDS, 3)
        print(FORMAT.format(i+1, sn[0], so[0], sn[1], so[1], sn[2], so[2], sn[3]), file=outfile)


def solve_math_problems(outfile):
    for line in outfile.readlines():
        print(line[:-6].strip(), eval(line[6:-8]))


if __name__ == '__main__':
    create_math_problems(open('test.txt','w'))
    solve_math_problems(open('test.txt','r'))
