Day = range(1, 32)

Month = [
    'january',
    'febuary',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
i = 0
year = int(input())


if year > 0:

    for i, month in enumerate(Month):

        if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
            days = 31

        elif month in ['febuary']:
            if leap_year(year):
                days = 29
            else:
                days = 28

        else:
            days = 30

        print("\n", Month[i], "\n")

        for day in range(1, days + 1):
            print(day, end=" ")

            if day % 7 == 0:
                print()

print("\n")

