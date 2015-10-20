# CISC327 Quibble
# Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

import time
import datetime

class Transaction:

    SELL = 1
    RETURN = 2
    CREATE = 3
    ADD = 4
    DELETE = 5
    END = 0

    def __init__(self, eventName, transactionType, date="", numTickets=0):
        self.eventName = eventName
        self.date = date
        self.transactionType = transactionType
        self.numTickets = numTickets

    def validDate(date):
        if len(date) > 6:
            return False

        if not date.isdigit():
            return False

        tomorrow = datetime.date.today() + datetime.timedelta(1)
        unix_time_tommorow= tomorrow.strftime("%s")

        two_years = datetime.date.today() + datetime.timedelta(365*2+1)
        unix_time_two_years= two_years.strftime("%s")

        date_year = int(date[:2])
        date_month = int(date[2:4])
        date_day =  int(date[-2:])

        if date_year > 99 or date_month > 12 or date_day > 31:
            return False

        unixt = datetime.datetime.strptime(str(date), "%y%m%d").strftime("%s")

        try:
            if not unix_time_tommorow <= unixt <= unix_time_two_years:
                return False
        except ValueError as err:
            return False

        return True

    validDate = staticmethod(validDate)

