# CheckNumberOfSquaresWhichAddUpToANumber
#Original Question:
#A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 32 + 12. Given X, how can we determine the number of ways in which it can be written as the sum of two squares? For example, 10 can only be written as 32 + 12 (we don't count 12 + 32 as being different). On the other hand, 25 can be written as 52 + 02 or as 42 + 32.

#SoroushHajizadeh September 25 2018
import math
import sys

def checkIfPerfectSquare(numberToCheck):  #sees if perfect square
    x = int(math.sqrt(numberToCheck)) #we know we're being given integers, so sqrt has to be int
    if ((x*x) == int(numberToCheck)): #if it is, return true, otherwise return false
        return True;
    return False

numberOflines = int(sys.stdin.readline()) #get number of lines from first line

for number in range (0, numberOflines):  #Go through file N number of times, given by first line
    numberToCheck = int(sys.stdin.readline()) #place number we're checking in memory
#    print("bob", numberToCheck)
    count = 0 #set the number of times this is true to 0 for each iteration

    for x in range (1, int(math.sqrt(numberToCheck))):  #Go from 0 to the square root, doesn't check square root as it can be a flaot
        if (((x*x) < (numberToCheck-x*x)) & (checkIfPerfectSquare(numberToCheck-(x*x)))):  #we check to see if each number squared, till the square root, is less than ours minus that number. Then we can check to see if our number, minus that number is a square root. If so, we have one solution!
                count = count+1 #we add one if true!!!

    if (checkIfPerfectSquare(numberToCheck) == True):  #check the square root itself, as this isn't covered by range or python.
        count = count+1



    print(count)
