import datetime
import time

date_string = str(input("Enter your date here: "))

element = datetime.datetime.strptime(date_string, "%d/%m/%Y")
tuple = element.timetuple()
timestamp = time.mktime(tuple)
print(timestamp)
