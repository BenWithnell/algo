import sys
# Import the different algorithms
from SortingAlgo import bubble_sort, selection_sort

def readFile(filename):
    nums = []
    # Open the file from the users input
    with open(filename, 'r') as file:
        # Go through the file line by line
        for lines in file:
            # If the line is empty ignore it
            if lines.strip() != "":
                # Check to see if the lines content contains a float(integer) or a string
                isfloat = True
                try:
                    float(lines.strip())
                except ValueError:
                   isfloat = False
                # Append the lines content to an array
                if isfloat == False:
                    nums.append(lines.strip())
                else:
                    nums.append(float(lines.strip()))
    # Close the file
    file.close()
    # Return the Array
    return nums


def ConvertToArray(List):
    # Seperate the String of input by the ',' and add it to an array
    nums = List.split(",")
    # Sort through the array, converting any numbers to floats
    for i in range(len(nums)):    
        isfloat = True
        try:
            float(nums[i])
        except ValueError:
           isfloat = False 
        if isfloat == False:
            nums[i] = nums[i]
        else:
            nums[i] = float(nums[i])
    # Return the Array
    return nums

def askWhichAlgorithm():
    List = raw_input()



# When the terminal prompt is run, if it doesn't include one of the inputs (file or csl) stop the program
try:
    if "file" not in sys.argv[1].lower() or "csl" not in sys.argv[1].lower():
        print("You need to select either a file or csl as the list input, try again")
        #quit()
except:
    print("You need to select either a file or csl as the list input, try again")
    quit()

# Input is file
if sys.argv[1].lower() == "file":
    # Ask for the filename
    print('What is the text filename?')
    print('make sure it is in the current directory and all the data is on seperate lines')
    print('*To exit press the keys: ctrl + z*')
    correctinput = False
    # Check to see if the file name is valid
    # If it is not, as the user again
    while correctinput == False:
        try:
            filename = raw_input()
            correctinput = True
            f = open(filename)
            f.close()
        except:
            correctinput = False
            print("incorrect input try again:")
            print('To exit press the keys: ctrl + z')
    # Run the function to convert the data from the file into an array
    nums = readFile(filename)
    print(nums)
    
    # Run and print the different sorting algorithms
    print(bubble_sort(nums))
    print(selection_sort(nums))

# Input is csl (comma seperated list)
if sys.argv[1].lower() == "csl":
    # Ask for a list of values/data seperated by a comma
    print("Write the values, seperating each vale with a comma")
    # Get the raw_input from the terminal
    List = raw_input()
    # Run the function to convert the data from a string into an array
    nums = ConvertToArray(List)
    print(nums)
    
    # Run and print the different sorting algorithms
    print(bubble_sort(nums))
    print(selection_sort(nums))












