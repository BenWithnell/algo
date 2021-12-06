import sys

from SortingAlgo import bubble_sort, selection_sort



class Algos:
    def __init__(self):
        self.nums

        if "file" not in sys.argv[1].lower() or "csl" not in sys.argv[1].lower():
            print("You need to select either a file or csl as the list input")

        if sys.argv[1].lower() == "file":
            print('What is the text filename? make sure it is in the current directory and all the data is on seperate lines')
            filename = raw_input()
            if filename.endswith('.txt') == False:
                print("Error")
            nums = readFile(filename)
            print(nums)
            print(selection_sort(nums))


        if sys.argv[1].lower() == "csl":
            print("Write the values, seperating each vale with a space and comma")
            List = raw_input()
            nums = ConvertToArray(List)
            print(nums)
            print(bubble_sort(nums))
            print(selection_sort(nums))


def readFile(filename):
    nums = []
    with open(filename, 'r') as file:   
        for lines in file:
            if lines.strip() != "":
                nums.append(float(lines.strip()))

    return nums


def ConvertToArray(List):
    nums = List.split(",")
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    return nums









