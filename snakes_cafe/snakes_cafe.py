menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
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
    order = 'initial value'
    while order != 'quit':
        order = input('>')
        for key in menu:
            for item in menu[key]:
                if item == order:
                    addToOrder(order)
                    
    
    if order == 'quit': 
        # do something? 
        pass


fullOrder = {}


def addToOrder(order):
    # print the confirmation, create a meal counter dictionary, add 1 to meal counter.
    print('add to order')
    fullOrderIndex=0
    for key in fullOrder:
        if key == order:
            fullOrder[key] +=1
        
        elif fullOrderIndex > len(fullOrder):
            fullOrder[order] =  1
        fullOrderIndex += 1
    
    print('** {fullOrder[order]} order of {order} have been added to your meal **')

welcomeAndMenu()


