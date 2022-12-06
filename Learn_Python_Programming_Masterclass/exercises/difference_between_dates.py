import datetime
from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 8, 11)

def date_difference(input_date2: date, input_date1: date) -> datetime.timedelta:
    """

    :param input_date2:
    :param input_date1:
    :return:
    """
    delta = input_date2 - input_date1
    print(type(delta))
    return delta


difference = date_difference(date2, date1)
print(difference)