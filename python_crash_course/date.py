from datetime import datetime, timedelta

current_date = datetime.now()
print('Toady is: ' + str(current_date))

# timedelta定义一个时间的时间
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

print("Day: " + str(current_date.day))
print("Month: " + str(current_date.month))
print("Year: " + str(current_date.year))

birthday = input("When is your birthday (dd/mm/yyyy)? ")

birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print("Birthday: " + str(birthday_date))