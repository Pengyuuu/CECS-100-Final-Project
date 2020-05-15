departure = int(input('What time are you leaving your house (e.g. 7am = 7, ' \
                      '7pm = 19): '))

while (departure < 0 or departure > 24):
    departure = int(input('What time are you leaving your house (e.g. 7am = 7, ' \
                      '7pm = 19): '))

arrival = int(input('What time are you arriving back home (e.g. 7am= 7, ' \
                    '7pm = 19): '))

while (arrival < 0 or arrival > 24):
    arrival = int(input('What time did you arrive (e.g. 7am= 7, ' \
                    '7pm = 19): '))

days = int(input('How many days are you spending on the trip?: '))

def departureArrival():
    global departure
    if (departure > 12):
        depTime = departure - 12
        depTime = str(depTime)
        depTime = depTime + 'pm'
    else:
        depTime = departure
        depTime = str(depTime)
        depTime = depTime + 'am'

    global arrival
    if (arrival > 12):
        arriTime = arrival -  12
        arriTime = str(arriTime)
        arriTime = arriTime + 'pm'
    else:
        arriTime = arrival
        arriTime = str(arriTime)
        arriTime = arriTime + 'am'

    return depTime, arriTime

def carRental():
    cars = int(input('How many cars are you renting?: '))

    return cars

def private_cars():
    private_car = int(input("Please enter amount of miles you've driven in" \
                            " a private car: "))
    while private_car < 0:
        private_car = int(input("Please enter amount of miles you've driven in" \
                            " a private car: "))
    fee = float( 0.27 * private_car )
    print("You have spent", fee, "dollars on the car you've been driving" \
          " during your trip")

def parking_fees():
    parking_fee = int(input("Please input how many times you've paid for" \
                            " a parking fee during your trip: "))
    if (parking_fee > days):
        Fee = (6 * (parking_fee - days))
        FeE = (6 * days) 
        print("After calculating the amount, the money you've spent is", Fee,\
              "dollars.", "While the company paid", FeE, "Dollars")
    else:
        FeE = (6 * days)
        print("The Company paid", FeE, \
              "While you have paid nothing out of your pocket")

def taxi_fees():
    taxi_fee = input("Did you take a taxi? Y/N:")
    if (taxi_fee == "Y" or taxi_fee == "y"):
        taxi = float(input("What is the amount of money spent on taking taxi rides?"))
        if (taxi_fee == "Y" or taxi_fee == "y"):
            fee = taxi - (days * 10)
            fEe = (days * 10)
            print("Since the company is helping pay for taxi rides they've paid", fEe,"dollars.","While you've paid the remainder if any..", fee, "dollars.")
        elif (taxi_fee == "N" or taxi_fee == "n"):
            counter = 0
            x = 1


def conference_fees():
    userInput = int(input("Enter the amount spent on the conference " \
                          "or seminar registration: "))
    while userInput < 0:
        userInput = int(input("Enter the amount spent on the conference " \
                              "or seminar registration: "))

def hotel_expenses():
    userInput = int(input("Enter the amount spent on hotel expenses: "))
    while userInput < 0:
        userInput = int(input("Enter the amount spent on hotel expenses: "))
    if userInput > 90:
        excess = userInput - 90
        print("The excess amount you owe is $", excess, sep = "")
    else:
        print("You spent", userInput, "on hotel expenses.")
        
def meal_time():
    depTotal = 0
    ariTotal = 0
    global departure
    global arrival
    if (departure < 7):
        userInput = int(input('How much did you spend on breakfast on ' \
                              'your day of departure?: '))
        while userInput < 0:
            userInput = int(input('How much did you spend on breakfast on ' \
                              'your day of departure?: '))
        dep_breakfast = userInput - 9
        print('You owe $', dep_breakfast,'for your breakfast on departure.')
        depTotal += dep_breakfast
    elif (departure < 12):
        userInput = int(input("How much did you spend on lunch on " \
                              "your day of departure?: "))
        while userInput < 0:
            userInput = int(input("How much did you spend on lunch on " \
                              "your day of departure?: "))
        dep_lunch = userInput - 12
        print("You owe $", dep_lunch,"for your lunch on departure.")
        depTotal += dep_lunch
    elif (departure < 18):
        userInput = int(input("How much did you spend on dinner on " \
                              "your day of departure?: "))
        while userInput < 0:
            userInput = int(input("How much did you spend on dinner on " \
                              "your day of departure?: "))
        dep_dinner = userInput - 16
        print("You owe $", dep_dinner,"for your dinner on departure.")
        depTotal += dep_dinner

    if (arrival > 8 and arrival < 13):
            userInput = int(input("How much did you spend on breakfast on " \
                                      "your day of arrival?: "))
            while userInput < 0:
                userInput = int(input("How much did you spend on breakfast on " \
                                      "your day of arrival?: "))
            arrival_breakfast = userInput - 9
            print("You owe $", arrival_breakfast,"for your breakfast on arrival.")
            ariTotal += arrival_breakfast
    elif (arrival > 13 and arrival < 19):
            userInput = int(input("How much did you spend on lunch on " \
                                      "your day of arrival?: "))
            while userInput < 0:
                userInput = int(input("How much did you spend on lunch on " \
                                      "your day of arrival?: "))
            arrival_lunch = userInput - 12
            print("You owe $", arrival_lunch,"for your lunch on arrival.")
            ariTotal += arrival_lunch
    elif (arrival > 19):
            userInput = int(input("How much did you spend on dinner on " \
                                      "your day of arrival?: "))
            while userInput < 0:
                userInput = int(input("How much did you spend on dinner on " \
                                      "your day of arrival?: "))
            arrival_dinner = userInput - 16
            print("You owe $", arrival_dinner,"for your dinner on arrival.")
            ariTotal += arrival_dinner

    return depTotal, ariTotal


def main():
    b, c = departureArrival()
    d = carRental()
    print('You are spending' ,days, 'days')
    print('You are departing your house at',b)
    print('You are arriving back home at',c)
    print('You rented',d, 'cars')
    private_cars()
    parking_fees()
    taxi_fees()
    conference_fees()
    hotel_expenses()
    z, y = meal_time()

main()
