import time
import random

def greeting():
    timeNow = time.localtime()
    if timeNow.tm_hour < 12:
        return "Good Morning!"
    elif timeNow.tm_hour <= 12 & timeNow.tm_hour < 16:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def check_in():
    name = input(f"{greeting()} Please can I get your name: ")
    name = name.upper()
    reservations = {}

    if name in reservations:
        key = reservations[name]
        return f"Your key is {key}, Goodbye and have a nice day."
    else:
        reservations[name] = random.randint(1, 100**5)
        return f"You booking was successful and your key is {reservations[name]}!"

def check_out():
    # room = int(input(f"{greeting()} Please what room did you stay in? "))

    # expenses = {10: 20000}
    # if room in expenses:
    #     expense = expenses[room]
    #     return f"Your bill for the duration of your stay in our hotel was {expense}, Goodbye and do have a wonderful day."

    # elif room not in expenses:
    #     print("Wrong room, please re-enter the room number")
    #     print(check_out())
    #     return
    count = 0
    while True:
        if count > 5:
            break

        room = int(input(f"{greeting()} Please what room did you stay in? "))

        expenses = {10: 20000}
        if room in expenses:
            expense = expenses[room]
            return f"Your bill for the duration of your stay in our hotel was {expense}, Goodbye and do have a wonderful day."

        else:
            print("Wrong room, please re-enter the room number")
            count += 1

    return "Too much invalid room numbers"
    
def clean():
    knock = input(f"Room service! I am here to clean the room\nTo allow them in type E else type B\nKey: ")
    if knock.upper() == "E":
        print("Cleaning and arranging bed...")
        time.sleep(30)
        print("Cleaning mirrors...")
        time.sleep(30)
        print("Cleaning bathroom...")
        time.sleep(30)
        print("Vacuuming floors...")
        time.sleep(30)
        return f"That is all, Thank you sir/ma and do have a lovely day."
    elif knock.upper() == "B":
        return "Thank you sir, we will be back later!"

if __name__ == '__main__':
    what = input(f"What would you like to do today!\nFor Check In press I\nFor Check Out press O.\nFor Cleaning press C\nKey: ")
    if what.upper() == "I":
        print(check_in())
    elif what.upper() == "O":
        print(check_out())
    elif what.upper() == "C":
        print(clean())