menu = {
    "Appetizers": ["wings", "cookies", "spring Rolls"],
    "Entrees": ["salmon", "steak", "meat tornado", "a literal garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["coffee", "tea", "unicorn tears"],
}


def welcomeAndMenu():
    print(
        """**************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        **************************************

        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears
        ***********************************
        ** What would you like to order? **
        ***********************************"""
    )
    foundOrder = "false"
    order = 'initial value'
    while order != 'quit':
        order = input('>').lower()
        for key in menu:
            for item in menu[key]:
                if item == order:
                    addToOrder(order)
                    foundOrder = "true"
        
        if foundOrder == "false":
            print(f"Sorry, your order of {order} is not available in our menu")
                    
    
    if order == 'quit': 
        printOrder = ''
        for order in fullOrder:
            printOrder += f"{fullOrder[order]} order of {order} "
            printOrder += "and "
        print('you have successfuly ordered: ', printOrder.removesuffix('and '))
        exit()
        


fullOrder = {}


def addToOrder(order):

    addedToOrder = 'false'
    
    for key in fullOrder:
        if key == order:
            fullOrder[order] +=1
            addedToOrder = 'true'
    
    if addedToOrder == 'false':
        fullOrder[order] =  1
        
    
    print(f"** {fullOrder[order]} order of {order} have been added to your meal **")

welcomeAndMenu()

#new branch

