# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def isLeapYear(year):
    """Given a year returns True if it's a leap year, else False"""
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


def daysInMonth(year, month):
    """
    Given a month, returns the number of days it has.
    Takes into consideration leap years.
    """
    if isLeapYear(year):
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def equal_dates(year1, month1, day1, year2, month2, day2):
    """ Checks if two dates are equal or not"""
    return year1 == year2 and month1 == month2 and day1 == day2


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    num_days = 0

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    while not equal_dates(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        num_days += 1
    return num_days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()