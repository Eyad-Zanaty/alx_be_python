import datetime
def display_current_datetime(current_date = datetime.datetime.now()):
    print(current_date)
display_current_datetime()
def calculate_future_date(future_date):
    x= future_date + datetime.datetime.now()
    print(x)
calculate_future_date(datetime.timedelta(days= int(input("Number of days: "))))