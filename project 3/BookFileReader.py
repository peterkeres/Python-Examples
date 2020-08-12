"""
peter keres
11/25/2017

reading a file and printing a list of books
"""


def fileimport():
    # getting the file open
    fileobject = open("bookListFile.txt", "r")
    thefile = fileobject.readlines()

    datelist = []
    booklist = []

    # split into 2 list, for date and other stuff
    for i in range(0, len(thefile), 1):
        date = ""
        book = ""
        for j in range(0, 4, 1):
            date += thefile[i][j]
        datelist.append(date)
        for k in range(5, len(thefile[i]), 1):
            book += thefile[i][k]
        booklist.append(book)
    filesplit = [datelist, booklist]

    return filesplit


def daterange(listsplit):
    # finding the earlyest date and lastest
    datelist = listsplit[0]
    lowest = datelist[0]
    highest = 0

    # find the earlyest date
    for i in range(0, len(datelist), 1):
        if int(lowest) > int(datelist[i]):
            lowest = datelist[i]

    # find the latest date
    for j in range(0, len(datelist), 1):
        if int(highest) < int(datelist[j]):
            highest = datelist[j]

    daterange = [lowest, highest]
    return daterange


def valadate(daterange):
    date1 = input("Enter the beginning year:")
    while not date1.isdigit() or int(date1) < int(daterange[0]) or int(date1) > int(daterange[1]):
        date1 = input("The year must between " + daterange[0] + " - " + daterange[1] + ". Enter the beginning year:")

    date2 = input("Enter the ending year:")
    while not date2.isdigit() or int(date2) < int(date1) or int(date2) > int(daterange[1]):
        date2 = input("The year must between " + date1 + " - " + daterange[1] + ". Enter the ending year:")

    inputdate = [date1, date2]
    return inputdate


def wanteddate(inputdate, filesplit):
    # getting the data i want
    userdate1 = inputdate[0]
    userdate2 = inputdate[1]
    alldates = filesplit[0]
    allbooks = filesplit[1]
    wanteddates = []
    wantedbooks = []
    wanteddatesflip = []
    wantedbooksflip = []

    for i in range(0, len(filesplit[0]), 1):
        if userdate1 <= alldates[i] and alldates[i] <= userdate2:
            wanteddates.append(alldates[i])
            wantedbooks.append(allbooks[i])

    # flipping the list around
    for j in range(len(wanteddates) - 1, -1, -1):
        wanteddatesflip.append(wanteddates[j])
        wantedbooksflip.append(wantedbooks[j])

    dataneed = [wanteddatesflip, wantedbooksflip]
    return dataneed


def output(dataneed):
    dates = dataneed[0]
    books = dataneed[1]

    print("All Titles between " + dates[0] + " and " + dates[len(dates) - 1] + ":")
    for i in range(0, len(dates), 1):
        print(dates[i] + "    " + books[i])


def main():
    output(wanteddate(valadate(daterange(fileimport())), fileimport()))

    user = input("Do you want to look for another range of dates? y for yes and n for no:")
    while user.lower() != "y" and user.lower() != "n":
        user = input("Didnt get that, if you want to look for another range type y for yes and n for no:")

    while user.lower() == "y":
        output(wanteddate(valadate(daterange(fileimport())), fileimport()))
        user = input("Do you want to look for another range of dates? y for yes and n for no:")
        while user.lower() != "y" and user.lower() != "n":
            user = input("Didnt get that, if you want to look for another range type y for yes and n for no:")


main()
