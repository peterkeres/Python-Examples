"""
Peter keres
12/9/17

To help someone with moving cost
"""

import math


def greeting():
    print("Hello and welcome to moving to Columbus, Ga trip calculator!")
    print("Please answer the following series of questions.")


def userQuestions():
    """ Getting staring questions so i know somtihg about the user"""
    print("")
    overSeas = input("Are you moving from outside of the United Stated? Y for yes N for no: \n")
    while overSeas.lower() != "y" and overSeas.lower() != "n":
        overSeas = input("Sorry thats not what i asked for, please a Y for yes and a N for no: \n")
    # now questoins for only if they come from outside USA
    # put these answer into another list
    if overSeas.lower() == "y":
        overCostTicket = input("What is the cost of your plane ticket: \n")
        while not overCostTicket.isdigit():
            overCostTicket = input("Please enter in only the number amout for the cost of the ticket: \n")

        overCostStuff = input("Enter the cost to ship your belongings over: \n")
        while not overCostStuff.isdigit():
            overCostStuff = input("Please enter in only the number amout for the cost to ship your belongings: \n")

        overHours = input("Enter in the amount of hours your flight is: \n")
        while not overHours.isdigit():
            overHours = input("Please enter in only the numbers for the amount of hours for your flight: \n")

    elif overSeas.lower() == "n":
        overCostTicket = 0
        overCostStuff = 0
        overHours = 0

    famSize = input("Are you moving with a family or are you single? Y for a family N for single: \n")
    while famSize.lower() != "y" and famSize.lower() != "n":
        FamSize = input("Sorry thats not what i asked for, please a Y for family and a N for single: \n")
    # questions for if they do have a fam
    # put these answers into another list
    if famSize.lower() == "y":
        famSizeNum = input("Not including your self, How many people are in your family: \n")
        while not famSizeNum.isdigit() or int(famSizeNum) < 1:
            famSizeNum = input("Please enter in only the number for the amount of people in your family: \n")

        spouceYearPay = input("Enter your spouce's yearly income: \n")
        while not spouceYearPay.isdigit() or float(spouceYearPay) <= 0:
            spouceYearPay = input("Please enter in only numbers for your spouce's yearly income: \n")

    elif famSize.lower() == "n":
        famSizeNum = 0
        spouceYearPay = 0

    moveTruck = input("Will you be renting a moving truck? Y for yes N for no: \n")
    while moveTruck.lower() != "y" and moveTruck.lower() != "n":
        moveTruck = input("Sorry thats not what i asked for, please a Y for yes or a N for no: \n")

    if moveTruck.lower() == "y":
        insurance = input("Will you be getting insurance on the moving truck? Y for yes or a  N for no: \n")
        while insurance.lower() != "y" and insurance.lower() != "n":
            insurance = input("Sorry thats not what i asked for, please enter a Y for yes or a N for no: \n")
        if insurance.lower() == "y":
            insuranceCost = 300
        else:
            insuranceCost = 0
    else:
        insuranceCost = 0
        insurance = 0

    movePeople = input("Will you be hiring a moving company? Y for yes N for no: \n")
    while movePeople.lower() != "y" and movePeople.lower() != "n":
        movePeople = input("Sorry thats not what i asked for, please a Y for yes and a N for no: \n")

    yearPay = input("What is your yearly pay: \n")
    while not yearPay.isdigit() or float(yearPay) <= 0:
        yearPay = input("Please enter in only numbers for your yearly pay: \n")

    if overSeas.lower() == "y":
        milesToo = input(
            "Enter in the amount of miles you will go from where you enter the country to Columbus, GA: \n")
        while not milesToo.isdigit():
            milesToo = input("Please enter in only the number amout of the miles: \n")

        flyToColumbus = input("Will you be flying to Columbus, GA once you enter the country. Y for yes N for no: \n")
        while flyToColumbus.lower() != "y" and flyToColumbus.lower() != "n":
            flyToColumbus = input("Sorry thats not what i asked for, please a Y for yes and a N for no: \n")

        if flyToColumbus.lower() == "y":
            flyToColumbusCost = input("How much is the plane ticket: \n")
            while not flyToColumbusCost.isdigit() or float(flyToColumbusCost) <= 0:
                flyToColumbusCost = input("Please enter in only numbers for the cost of the plane ticket: \n")

            flyToColumbusHours = input("How many Hours is the plane flight: \n")
            while not flyToColumbusHours.isdigit() or float(flyToColumbusHours) <= 0:
                flyToColumbusCost = input("Please enter in only numbers for the length of the flight: \n")

        elif flyToColumbus.lower() == "n":
            flyToColumbusCost = 0
            flyToColumbusHours = 0


    elif overSeas.lower() == "n":
        milesToo = input("Enter in the amount of miles you will travle to Columbus, GA: \n")
        while not milesToo.isdigit():
            milesToo = input("Please enter in only the number amout of the miles: \n")

        flyToColumbus = input("Will you be flying to Columbus, GA. Y for yes N for no: \n")
        while flyToColumbus.lower() != "y" and flyToColumbus.lower() != "n":
            flyToColumbus = input("Sorry thats not what i asked for, please a Y for yes and a N for no: \n")

        if flyToColumbus.lower() == "y":
            flyToColumbusCost = input("How much is the plane ticket: \n")
            while not flyToColumbusCost.isdigit() or float(flyToColumbusCost) <= 0:
                flyToColumbusCost = input("Please enter in only numbers for the cost of the plane ticket: \n")

            flyToColumbusHours = input("How many Hours is the plane flight: \n")
            while not flyToColumbusHours.isdigit() or float(flyToColumbusHours) <= 0:
                flyToColumbusCost = input("Please enter in only numbers for the length of the flight: \n")

        elif flyToColumbus.lower() == "n":
            flyToColumbusCost = 0
            flyToColumbusHours = 0

    # list for basic information
    listBasic = [overSeas, famSize, moveTruck, insurance, insuranceCost, movePeople, yearPay, milesToo, flyToColumbus]

    # list for overSeas
    listOverSeas = [overCostTicket, overCostStuff, overHours]

    # list for famSize
    listFamSize = [famSizeNum, spouceYearPay]

    # list for flying to columbus
    listFlyToColumbus = [flyToColumbusCost, flyToColumbusHours]

    allDataList = [listBasic, listOverSeas, listFamSize, listFlyToColumbus]

    return allDataList


def timeSpent(overHours, flyToColumbusHours, milesToo):
    """ to see total time spent during the move, return in a Hr format... also add 1 day default to unpack"""

    planeHours = float(overHours) + float(flyToColumbusHours)

    # going to say the avg person can drive 65 miles in a 1 hour period when moving
    timeDrive = float(milesToo) / 65

    totalTimeSpent = timeDrive + planeHours + 24  # 24 is for hours spend uppacking "1day"

    return totalTimeSpent


def workRevLost(yearPay, spouceYearPay, timeSpent):
    """find total amout lost during the move by not being able to work. returns a list of total money lost"""
    # round up becuase your going to spend a day moving even if its only a few hours
    totalDays = round((timeSpent / 24))
    if int(totalDays) == 0:
        totalDays == 1

    payLost = (float(yearPay) / 365) * totalDays

    # if there is a spouce or not
    if float(spouceYearPay) > 0:
        payLostSpouce = (float(spouceYearPay) / 365) * totalDays
    else:
        payLostSpouce = 0

    total = payLost + payLostSpouce

    return total


def planeCost(overCostTicket, flyToColumbusCost):
    """getting total plane cost, returning a total"""
    total = int(overCostTicket) + int(flyToColumbusCost)

    return total


def foodCost(timeSpent, famSizeNum):
    """getting total food cost, assume each person eats 3 meals aday at 10$ each, returns  a total cost"""

    dayOfFood = 3 * 10

    totalFoodCost = (dayOfFood * (round(timeSpent / 24))) * (
                int(famSizeNum) + 1)  # the one is for the person using the program

    return totalFoodCost


def moverCost(timeSpent, mover):
    """will get total cost for having movers, they get paid 10$ an hour, return a total cost"""
    if mover.lower() == "y":
        total = 10 * round(timeSpent)
    else:
        total = 0

    return total


def lodgingCost(famSizeNum, timeSpent):
    """will get the total cost for staying at hotels, returns total cost"""

    totalNights = round(
        (timeSpent / 24)) - 1  # the -1 is if they only spend one day moving they dont need to stay at a inn

    if totalNights > 0:
        if (int(famSizeNum) + 1) <= 2:
            totalCost = totalNights * 65
        elif (int(famSizeNum) + 1) >= 3:
            totalCost = totalNights * 85  # cost more for if there is a fam of 3 or more
    else:
        totalCost = 0

    return totalCost


def movingTruckCost(timeSpent, famSizeNum, milesToo, overSeasMoving):
    """will get the total cost for the truck, will go to different bracket based on fam size, will return a total cost num"""
    # will get a differnt size truck based on the size of there fam
    if (int(famSizeNum) + 1) == 1 or (int(famSizeNum) + 1) == 2:
        truckCostDay = 20
        truckCentMile = .10
        truckMPG = 25
    elif (int(famSizeNum) + 1) == 3 or (int(famSizeNum) + 1) == 4:
        truckCostDay = 25
        truckCentMile = .15
        truckMPG = 20
    else:
        truckCostDay = 30
        truckCentMile = .20
        truckMPG = 15

    dayCost = (round(timeSpent / 24)) * truckCostDay

    costPerMile = float(milesToo) * truckCentMile

    costGas = (float(milesToo) / truckMPG) * 2.95  # just going to say gas is 2.95

    totalCost = dayCost + costPerMile + costGas + float(overSeasMoving)

    return totalCost


def printOutTotal(timeSpent, workRevLost, planeCost, foodCost, lodgingCost, truckCost, moverCost):
    """will print out a total sheet the user can see of all the cost totals, no returns here"""
    print("")
    print("Time spent ........... {:,.0f}".format(timeSpent // 24) + " Days {:,.0f}".format(timeSpent % 24) + " hours")
    print("Revenue lost ......... ${:,.2f}".format(workRevLost))
    if float(planeCost) > 0:
        print("Plane cost ........... ${:,.2f}".format(planeCost))
    print("Food cost ............ ${:,.2f}".format(foodCost))
    if float(lodgingCost) > 0:
        print("Lodging cost ......... ${:,.2f}".format(lodgingCost))
    if float(truckCost) > 0:
        print("Moving truck cost .... ${:,.2f}".format(truckCost))
    if float(moverCost) > 0:
        print("Movers cost .......... ${:,.2f}".format(moverCost))
    totalCost = planeCost + foodCost + lodgingCost + truckCost + moverCost + workRevLost
    print("--------------------------------------------")
    print("Grand total .......... ${:,.2f}".format(totalCost))


def main():
    greeting()
    user = "y"
    while user.lower() == "y":

        listAll = userQuestions()
        time = timeSpent(listAll[1][2], listAll[3][1], listAll[0][7])
        workLost = workRevLost(listAll[0][6], listAll[2][1], time)
        plane = planeCost(listAll[1][0], listAll[3][0])
        food = foodCost(time, listAll[2][0])
        lodging = lodgingCost(listAll[2][0], time)
        truck = movingTruckCost(time, listAll[2][0], listAll[0][7], listAll[1][2])
        mover = moverCost(time, listAll[0][5])

        printOutTotal(time, workLost, plane, food, lodging, truck, mover)

        print("")
        user = input("would you like to run this again? Enter a Y for yes or a N for no: \n")
        while not user.lower() == "y" and not user.lower() == "n":
            user = input("Please enter only a Y for yes or a N for no: \n")

    print("Have a great day !")


main()
