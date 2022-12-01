from datetime import datetime, timedelta

# to get the current date and local time
print(datetime.now())

# to get the yesterday date and local time
print(datetime.now() - timedelta(1))

# to get the tomorrow date and local time
print(datetime.now() + timedelta(1))

