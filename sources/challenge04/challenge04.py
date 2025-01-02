# generate data for stage 4
#
# The idea here will be that a timelog from a punch card machine will have mixed up data.
# So, it should have an employee number, start, and end
# But the start and end are swapped
# Not related necessarily to the data, but there will be some other considerations about payment
# For example, working on Monday gets a bonus rate
# Working over 6 hours also gets a bonus rate
# year is 2034

import datetime
import random


def generate_data(employee_id, year, start_month, end_month, number_of_entries, seed=3):
    """generates punch card data with columns employeeid, date, start, end"""

    random.seed(seed)
    # get some random dates, but make sure they are unique
    dates = []
    for x in range(number_of_entries):
        while True:
            month = random.randint(start_month, end_month)
            day = random.randint(1, 28)
            date = datetime.date(year=year, month=month, day=day)
            if date not in dates:
                dates.append(date)
                break

    timelog = []
    for date in dates:
        start_hour = random.randint(9, 11)
        end_hour = random.randint(13, 22)
        start_min = random.randint(0, 59)
        end_min = random.randint(0, 59)
        start_time = datetime.time(hour=start_hour, minute=start_min)
        end_time = datetime.time(hour=end_hour, minute=end_min)

        if random.randint(0, 1) == 1:
            timelog.append((employee_id, date, start_time, end_time))

        else:
            timelog.append((employee_id, date, end_time, start_time))

    return timelog


# First we need some data for when Fat Tony shows data and explains it. Ten entries will be fine.
employee_id = "0028"
timelog = generate_data(
    employee_id, year=2034, start_month=1, end_month=1, number_of_entries=10
)

with open("january_timelog.txt", "w") as f:
    for id, date, start, end in timelog:
        print(date.strftime("%a"), id, date, start, end)
        f.write(f"{id} {date} {start} {end}\n")


# Next, we need some data that will be used to parse through. This will just be a text file in the end. It's not going to be a CSV file.
# Will set the number of entries to something reasonable in a two month period (feb, jan)

employee_id = "0028"
timelog = generate_data(
    employee_id, year=2034, start_month=2, end_month=3, number_of_entries=37
)

with open("timelog.txt", "w") as f:
    for id, date, start, end in timelog:
        f.write(f"{id} {date} {start} {end}\n")
