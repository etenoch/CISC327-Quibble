# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# The transaction class verifies that the date is entered correctly, and assigns attributes to the object.

import time
import datetime

class Transaction:

    SELL = 1
    RETURN = 2
    CREATE = 3
    ADD = 4
    DELETE = 5
    END = 0

    def __init__(self, eventName, transactionType, numTickets=0,date=""):
        self.eventName = eventName
        self.date = date
        self.transactionType = transactionType
        self.numTickets = numTickets

    def validDate(date):
        if len(date) > 6: # If the date is entered incorrectly
            return False

        if not date.isdigit(): # If the date is entered incorrectly
            return False

        tomorrow = datetime.date.today() + datetime.timedelta(1)
        unix_time_tommorow= tomorrow.strftime("%s")

        two_years = datetime.date.today() + datetime.timedelta(365*2+1) # Time for two year after tommorow
        unix_time_two_years= two_years.strftime("%s")

        date_year = int(date[:2]) # Gets the year
        date_month = int(date[2:4]) # Gets the month
        date_day =  int(date[-2:]) # Gets the date

        if date_year > 99 or date_month > 12 or date_day > 31: # When the data is entered is entered incorrectly
            return False

        unixt = datetime.datetime.strptime(str(date), "%y%m%d").strftime("%s")

        try:
            if not unix_time_tommorow <= unixt <= unix_time_two_years: # If the data is not in range
                return False
        except ValueError as err:
            return False

        return True

    validDate = staticmethod(validDate)

