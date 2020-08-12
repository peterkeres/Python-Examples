"""
Peter Keres
1/15/18

Simple recycling programing
"""


class RecycleBin:
    """
    Class represents a bin that holds items to be recycled
    """

    def __init__(self):
        self.items = []

    def addItem(self, item):
        """
        adds an item into the recycle bin
        @param self:
        @param item: String of the item to be added
        @return:
        """

        new_item = OtherRecycle(item)

        if item.lower() == "aluminumcan":
            new_item = AluminumCan()
        elif item.lower() == "plasticbottle":
            new_item = PlasticBottle()
        elif item.lower() == "glassbottle":
            new_item = GlassBottle()
        elif item.lower() == "cardboardbox":
            new_item = CardboardBox()

        self.items.append(new_item)

    def removeItem(self, item):
        """
        Removes an item from the recycle bin
        @param item: String of the item to be removed
        @return:
        """

        for currentItem in self.items:
            if currentItem.name == item:
                self.items.remove(currentItem)
                return currentItem

    def holding(self):
        """
        What is inside the bin
        @return: a list of strings for each item in the bin
        """
        items = []

        for item in self.items:
            items.append(item.name)

        return items


class RecycleItem:
    """
    Base class for each item that can be recycled
    """

    def __init__(self, name):
        self.name = name


class PlasticBottle(RecycleItem):
    """
    Class for Plastic Bottles
    """

    def __init__(self):
        super().__init__("Plastic Bottle")


class GlassBottle(RecycleItem):
    """
    Class for Glass Bottles
    """

    def __init__(self):
        super().__init__("Glass Bottle")


class AluminumCan(RecycleItem):
    """
    Class for Aluminum Cans
    """

    def __init__(self):
        super().__init__("Aluminum Can")


class CardboardBox(RecycleItem):
    """
    Class for cardboard boxes
    """

    def __init__(self):
        super().__init__("Cardboard Box")


class OtherRecycle(RecycleItem):
    """
    Class for items that are not commonly used
    """

    def __init__(self, item):
        super().__init__(item)


def menu():
    """
    Shows the Main menu
    @return: The users choice of menu item in string
    """
    print("RECYCLE BIN MENU")
    print(f' {"1":5} {"==>":5} See whats in the Recycle Bin')
    print(f' {"2":5} {"==>":5} Add an item to the Recycle bin')
    print(f' {"3":5} {"==>":5} Remove an item from the bin')
    print(f' {"4":5} {"==>":5} Quit ')

    user = input()

    return user


def validate(option):
    """
    Checks to see if user input is a valid option in the menu
    @param option: The users input in string
    @return: If a valid option or not
    """
    menu_options = ["1", "2", "3", "4"]
    test = True

    if option not in menu_options:
        print(f' {option} is a invalided option, please try again')
        test = False

    return test


def runOption(user, bin):
    """
    Runs the methods that are needed for each choice in the menu
    @param user: the users choice
    @param bin: The recycle bin that the choice will be used on
    @return:
    """
    if user == "1":
        showBin(bin)
    elif user == "2":
        addItem(bin)
    elif user == "3":
        removeItem(bin)


def showBin(bin):
    """
    displays what items are in the recycle bin
    @param bin: the recycle bin to be displayed
    @return:
    """

    stash = bin.holding()

    print("Current Items in the bin")
    for item in stash:
        print(f'\t{item}')


def addItem(bin):
    """
    Adds an item to the recycle bin
    @param bin: The recycle bin you are adding an item too
    @return:
    """

    user = input("What item are you adding to the bin?")
    bin.addItem(user)


def removeItem(bin):
    """
    removeing an item from the recycle bin
    @param bin: What recycle bin you are removing from
    @return:
    """

    user = input("What item are you removing from the bin?")
    bin.removeItem(user)


def main():
    """
    Main run of the program
    @return:
    """

    user = menu()
    bin = RecycleBin()
    # Add some sampled items into the bin
    item = "glassbottle"
    item2 = "cardboardbox"
    bin.addItem(item)
    bin.addItem(item2)

    # allows user to keep at the menu unitl they quit
    while user != '4':
        if validate(user):
            runOption(user, bin)
        user = menu()

    print("later, thanks for using this")


if __name__ == '__main__':
    main()
