from pathlib import Path
import datetime

# Get the data into lines
data = Path("./timelog.txt").read_text().strip().splitlines()
data = Path("./january_timelog.txt").read_text().strip().splitlines()
# Split the data lines into tuples
# the data is space separated
data = [line.split() for line in data]

# we need to define the wage
normal_wage = 12
overtime_wage = 16

# we need counters for different wage types
normal_wage_hours = datetime.timedelta(0)
overtime_wage_hours = datetime.timedelta(0)

for empid, date, t1, t2 in data:
    date = datetime.date.fromisoformat(date)

    # time1 should be the start
    # time2 should be the end
    # but they are sometimes swapped in the data
    # the one that is greater is the end time
    time1 = datetime.time.fromisoformat(t1)
    time2 = datetime.time.fromisoformat(t2)
    if time2 > time1:
        start = time1
        end = time2
    elif time1 > time2:
        start = time2
        end = time1

    # combine the date and times so we can get a time delta
    startdt = datetime.datetime.combine(date, start)
    enddt = datetime.datetime.combine(date, end)

    # next we need a timedelta to determine the number of hours worked
    hours_worked = enddt - startdt
    print(startdt, enddt, hours_worked)

    # next we need the day of the week
    # monday is 0, sunday is 6
    if date.weekday() == 6:
        overtime_wage_hours += hours_worked
        continue

    # next determine if there was overtime
    overtime_threshold = datetime.timedelta(hours=6)

    if hours_worked > overtime_threshold:
        overtime_wage_hours += hours_worked - overtime_threshold
        normal_wage_hours += overtime_threshold
    elif hours_worked < overtime_threshold:
        normal_wage_hours += hours_worked

# Finally, we need to calculate the wages
# we need the total hours worked so the time deltas need to be converted
# then the rest is math

normal_hours = round(normal_wage_hours.total_seconds() / 3600, 0)
overtime_hours = round(overtime_wage_hours.total_seconds() / 3600, 0)

normal_pmt = normal_hours * normal_wage
overtime_pmt = overtime_hours * overtime_wage

print("normal hours:", normal_hours, normal_pmt)
print("overtime hours:", overtime_hours, overtime_pmt)
print("total pmt", normal_pmt + overtime_pmt)
