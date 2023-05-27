import datetime as dt

#This will calculate days since your birthday, or any other date you desire.

def calculate_days():
    user_bday_str = input("Please input your birthday or significant date in YYYY-MM-DD format. : ")
    user_bday = dt.datetime.strptime(user_bday_str, "%Y-%m-%d")
    todays_date = dt.datetime.today()
    time_since_birth = todays_date - user_bday
    print(time_since_birth.days, "days since the requested date\n")

    again = input("Would you like to calculate another date? (Y/N): ")
    
    if again.lower() == 'y':
        calculate_days()

if __name__ == "__main__":
    calculate_days()