# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(seconds):

    hour_list = []
    hour = int(seconds/3600)
    if hour > 1 or hour == 0:
        hour_list = ['hours', hour]
    else:
        hour_list = ['hour', hour]

    minute_list = []
    minute = int((seconds - 3600*hour)/60)
    if minute > 1 or minute == 0:
        minute_list = ['minutes', minute]
    else:
        minute_list = ['minute', minute]

    second_list = []
    second = seconds - 3600*hour - 60*minute
    if second > 1 or second == 0:
        second_list = ['seconds', second]
    else:
        second_list = ['second', second]

    # print(hour_list)

    if not type(second) is int:
        return "%d " % (hour_list[1]) + hour_list[0] + ", " + "%d " % (minute_list[1]) + minute_list[0] + ", " + "%.1f " % (second_list[1]) + second_list[0]
    else:
        return "%d " % (hour_list[1]) + hour_list[0] + ", " + "%d " % (minute_list[1]) + minute_list[0] + ", " + "%d " % (second_list[1]) + second_list[0]


print(convert_seconds(3600))

print(convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print(convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds
