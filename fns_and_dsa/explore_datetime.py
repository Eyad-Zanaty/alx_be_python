from datetime import datetime, timedelta
def display_current_datetime(current_date):
    print(current_date)
display_current_datetime(datetime.now())
def calculate_future_date(future_date):
    x= future_date + datetime.now()
    print(x)
calculate_future_date(timedelta(days= int(input("Number of days: "))))