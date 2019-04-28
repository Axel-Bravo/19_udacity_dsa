def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!

    if day2 >= day1:
        year_days = (year2 - year1) * 365
        month_days = (month2 - month1) * 30
        day_days = day2 - day1
        total_days = year_days + month_days + day_days

    else:  # day1 > day2
        day_compensator = (31 - day1) + 1
        if month1 > 11:
            month1 = 1
            year1 += 1
        else:
            month1 += 1
        day1 = 1

        year_days = (year2 - year1) * 365
        month_days = (month2 - month1) * 30
        day_days = day2 - day1

        total_days = year_days + month_days + day_days + day_compensator

    return total_days


daysBetweenDates(2017, 12, 30,  2018, 1,  1)