from datetime import datetime,date

def time_machine():
    user_date = input('Enter date, please: ')
    now_date = datetime.now()
    now_day = now_date.day
    now_month = now_date.month
    now_year = now_date.year

    if (len(user_date) == 8):
        new_day = int(user_date[0] + user_date[1])
        new_month = int(user_date[3] + user_date[4])
        new_year = int(user_date[6] + user_date[7])

    elif (len(user_date) == 10):
        new_day = int(user_date[1] + user_date[0])
        new_month = int(user_date[3] + user_date[4])
        new_year = int(user_date[6] + user_date[7] + user_date[8] + user_date[9])

    if (new_year < 100):
        if (new_year < 70):
            new_year = new_year + 2000
        else:
            new_year = new_year + 1900

    if ((date(now_year, now_month, now_day) - date(new_year, new_month, new_day)).days > 0):
        print('This date was '+str((date(now_year, now_month, now_day) - date(new_year, new_month, new_day)).days)+' days ago')
    else:
        print('This date will be in '+str(-(date(now_year, now_month, now_day) - date(new_year, new_month, new_day)).days)+' days')
def main():
    time_machine()

if __name__=='__main__':
    main()