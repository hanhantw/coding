# input (2020, 3, 29, 3) -> (2020, 4, 1)
# input (2021, 5, 9, 1129) -> (2024, 6, 11)
# input (2003, 12, 15, 100) -> (2004, 3, 24)
#
# Leap year
# can be divided by 4 but not 100 --> leap year
# can be divided by 100 but not 400 --> not leap year
# can be divided by 400 --> leap year


def date_calculator(year: int, month: int, day: int, days_to_add: int) -> set:
    day += days_to_add
    month_for_30 = [4, 6, 9, 11]
    month_for_31 = [1, 3, 5, 7, 8, 10, 12]

    def is_leap_year(year: int):
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        return False

    if day > 365:
        if is_leap_year(year) and month <= 2:
            day -= 366
        else:
            day -= 365
        year += 1

    while day > 30:
        if day > 365:
            if is_leap_year(year):
                day -= 366
            else:
                day -= 365
            year += 1
        else:
            if month in month_for_31:
                day -= 31
            elif month in month_for_30:
                day -= 30
            elif month == 2:
                if is_leap_year(year):
                    day -= 29
                else:
                    day -= 28
            month += 1
            if month > 12:
                year += month // 12
                month = month % 12

    month = month % 12
    year += month // 12

    return (year, month, day)


date_calculator(2021, 5, 9, 1129)
