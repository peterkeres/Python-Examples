"""
peter keres
jul 29
showing a student what i would have done for reading from a file and parsing lines
this was done WELL after the proejct was due, this is to just answers quesitons they had of how someone else would
solve this problem
"""

"""
Will open a text file and parse out the names into a list, and return that list'
parm: fileName- path too the file'
return: a list of names as a string'
"""


def emailParser(fileName):
    '#this opens the file and gives us a way to interact with the file'
    logFile = open(fileName, "r")

    '#gives us a empty list of names that we will fill'
    listOfNames = []

    '#getting each set of names from the file'
    '#start forloop'
    for line in logFile:
        trimPassOne = line.split("@")  # splits each line in file into 2 parts, at the @
        # example-   trimPassOne[0] = From stephen.smith
        #           trimPassOne[1] = bigred.cornell.edu Saturday Jan 5th 09:30:15 2019

        trimPassTwo = trimPassOne[0].split(" ")  # splits the trimed part into another 2 parts at the space
        # example-   trimPassTwo[0] = From
        #            trimPassTwo[1] = stephen.smith

        listOfNames.append(trimPassTwo[1])  # puts just the name part of the final split inot the list
        # example-    trimPassTwo[1] = stephen.smith
    '#end forloop'

    '#gives us back the list of names'
    return listOfNames


def main():
    print("hello, starting program")
    print("=========================")
    print("=========================")

    fileName = "logfile.txt"

    print(emailParser(fileName))

    print("=========================")
    print("=========================")
    print("end of program, bye bye")


main()
