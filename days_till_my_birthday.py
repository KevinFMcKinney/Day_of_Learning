from datetime import date
from prefect import flow, task

@task
def get_next_birthday(todays_date, birthday_day, birthday_month):
    if todays_date.month >= birthday_month:
        if todays_date.day > birthday_day:
            next_birthday = date(todays_date.year + 1, birthday_month, birthday_day)
        elif todays_date.day == birthday_day and todays_date.month == birthday_month:
            next_birthday = todays_date
        elif todays_date.day < birthday_day and todays_date.month == birthday_month:
            next_birthday = date(todays_date.year, birthday_month, birthday_day)
    else:
        next_birthday = date(todays_date.year, birthday_month, birthday_day)

    return next_birthday

@task
def get_days_till_birthday(todays_date, next_birthday):
    if next_birthday == todays_date:
        print("Today is my birthday.")
    else:
        print("Today is not my birthday. Next birthday is in", (next_birthday - todays_date).days, "days.")

@flow(log_prints=True)
def days_till_my_birthday():
    
    todays_date = date.today()

    next_birthday = get_next_birthday(todays_date, 6, 6)

    get_days_till_birthday(todays_date, next_birthday)

if __name__ == "__main__":
    days_till_my_birthday()