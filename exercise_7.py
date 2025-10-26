hourly_wage = float(input("Hourly wage: "))
worked_hours = float(input("Hours worked: "))
day = str(input("Day of the week: "))

if day != "Sunday":
    print(f"Daily wages: {hourly_wage * worked_hours}")
else:
    print(f"Daily wages: {2 * hourly_wage * worked_hours}")