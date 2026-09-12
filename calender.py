Week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]

Month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def weekday(year, month, day):
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    f = day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)

    return (f + 6) % 7


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


year = int(input("Enter year: "))

if year > 0:

    for i, month in enumerate(Month):

        if month in [
            "January",
            "March",
            "May",
            "July",
            "August",
            "October",
            "December",
        ]:
            days = 31

        elif month == "February":
            if leap_year(year):
                days = 29
            else:
                days = 28

        else:
            days = 30

        print("\n", month, "\n")

        for week in Week:
            print(week, end=" ")

        print()

        first_day = weekday(year, i + 1, 1)

        for _ in range(first_day):
            print("   ", end="")

        for day in range(1, days + 1):
            print(f"{day:2}", end=" ")

            if (day + first_day) % 7 == 0:
                print()

        print()
