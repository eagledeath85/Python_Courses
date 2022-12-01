from datetime import datetime, timedelta


def timeDifference(hour1, minute1, hour2, minute2):

    # Converting h1:m1 in minutes
    time1 = (hour1 * 60) + minute1

    # Convert h2:m2 in minutes
    time2 = (hour2 * 60) + minute2

    # comparing time1 and time2
    if time2 == time1:
        return print("Both time are same times")

    else:
        # calculate time difference in minutes and convert it in HH:MM format
        difference_in_minutes = time2 - time1
        difference = '{:02d}:{:02d}'.format(*divmod(difference_in_minutes, 60))
        return difference


h1 = int(input("Enter hour of time1: "))
m1 = int(input("Enter minutes of time1: "))
h2 = int(input("Enter hour of time2: "))
m2 = int(input("Enter minutes of time2: "))
print("The difference between", h1, m1, "and", h2, m2, "is", timeDifference(h1, m1, h2, m2))
