"""
author: Peter Keres
date: 9/11/2017

purpose: This program is a simple generic trip calculator
"""


def user_greet() -> None:
    """
    Greets the user
    @return:
    """

    print("Welcome to the generic trip calculator!")


def user_place() -> str:
    """
    Gets the place where user wants to travel too
    @return: User input of where to go
    """

    return input("Where do you want to go? \n")


def user_distance() -> float:
    """
    Gets the distance the user will travel
    @return: How far in miles the user is traveling
    """

    correct: bool = False
    dis: float = 0.0

    while not correct:
        try:
            dis = float(input("How far will you travel (in miles)? \n"))
            if dis > 0:
                correct = True
        except ValueError:
            print("That doesnt look like a distance in miles, want to try that again?")

    return dis


def user_time() -> float:
    """
    Gets the time the user wants to spend traveling
    @return: How long the user wants to travel for
    """

    correct: bool = False
    time: float = 0.0

    while not correct:
        try:
            time = float(input("How long would you like your trip to take (in hours)? \n"))
            if time > 0:
                correct = True
        except ValueError:
            print("That doesnt look like time, want to try that again?")

    return time


def user_mph() -> float:
    """
    Gets how fast the user wants to travel
    @return: How fast the user wants to travel
    """

    correct: bool = False
    mph: float = 0.0

    while not correct:
        try:
            mph = float(input("How fast would you like to travel (miles per hour)? \n"))
            if mph > 0:
                correct = True
        except ValueError:
            print("That doesnt look like mph, want to try that again?")

    return mph


def display_place(place: str) -> None:
    """
    Displays the place the user is traveling too
    @param place: Place user is traveling too
    @return:
    """

    print("Traveling to " + place + ":")


def display_total_time(dis: float, mph: float) -> None:
    """
    Display the total time to take the trip
    @param dis: Distance the user is traveling
    @param mph: How fast the user is going to travel
    @return:
    """

    time_tot: float = dis / mph

    print("If you traveled " + str(round(dis, 1)) + " miles going " + str(round(mph, 1))
          + " miles per hour, it would take you " + str(round(time_tot, 1)) + " hours.\n")


def display_total_mph(dis: float, time: float) -> None:
    """
    Display the total mph used to take the trip
    @param dis: Distance of how far the user is traveling
    @param time: How long the user wants the trip to take
    @return:
    """

    speed_tot: float = dis / time

    print("If you traveled " + str(round(dis, 1)) + " miles in " + str(round(time, 1))
          + " hours, you would be traveling " + str(round(speed_tot, 1)) + " miles per hour.\n")


def display_total_miles(time: float, mph: float) -> None:
    """
    Display the total miles traveled on the trip
    @param time: How long the user wants the trip to take
    @param mph: How fast the user wants the trip to take
    @return:
    """

    dis_tot: float = mph * time

    print("If you traveled " + str(round(time, 1)) + " hours going " + str(round(mph, 1))
          + " miles per hour, you would travel " + str(round(dis_tot, 1)) + " miles.\n")


def main() -> None:
    """
    Main run of the program
    @return:
    """

    user_greet()

    place: str = user_place()
    dis: float = user_distance()
    time: float = user_time()
    mph: float = user_mph()

    display_place(place)
    display_total_time(dis, mph)
    display_total_mph(dis, time)
    display_total_miles(time, mph)

    print("\nHave a nice trip!")


if __name__ == "__main__":
    main()
