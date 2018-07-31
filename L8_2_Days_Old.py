# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
# Based on python2

def divisible(year, n):
    val = year/n
    str_val = str(val)
    pos = str_val.find('.')
    digit = int(str_val[pos+1:])
    # print digit
    if digit == 0:
        return True
    else:
        return False


def testleapyear(year, month, day):
    daysOfMonths_nonleap = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths_leap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if divisible(year, 4.0) is False:
        # print 'hello'
        result = False # -'common year'
    elif divisible(year, 100.0) is False:
        # print 'hello2'
        result = True # -'leap year'
    elif divisible(year, 400.0) is False:
        # print 'hello3'
        result = False # -'common year'
    else:
        # print 'hello4'
        result = True # -'leap year'

    if result:
        days = daysOfMonths_leap[month-1:]
    else:
        days = daysOfMonths_nonleap[month-1:]
    if day == 31:
        total = sum(days) - day
    else:
        total = sum(days) - day + 1

    return total

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    if abs(year2-year1) == 0:
        total1 = testleapyear(year1, month1, day1)
        total2 = testleapyear(year2, month2, day2)
        delta = abs(total1 - total2)
        return delta
    else:
        iter = 0
        year = year1
        month = month1
        day = day1
        sum = 0

        while iter != abs(year2-year1)+1:
            total = testleapyear(year, month, day)
            sum = sum + total
            iter = iter + 1
            year = year + iter
            month = 1
            day = 1
        sum = sum - testleapyear(year2, month2, day2)
    return sum

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    # test_cases = [((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        # print(result)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()

# print(testleapyear(1900,1,1))
