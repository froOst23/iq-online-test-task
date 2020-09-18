#!/usr/bin/python3
# -*- coding: utf-8 -*-

def the_year_is_leap(year):
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        return True
    else:
        return False


def bank_interest_rate(number):
    return (number * 10) / 100


def rest_of_day(day, month, year):
    if the_year_is_leap(year) == True:
        if month == '01':
            return 31 - int(day)
        elif month == '02':
            return 29 - int(day)
        elif month == '03':
            return 31 - int(day)
        elif month == '04':
            return 30 - int(day)
        elif month == '05':
            return 31 - int(day)
        elif month == '06':
            return 30 - int(day)
        elif month == '07':
            return 31 - int(day)
        elif month == '08':
            return 31 - int(day)
        elif month == '09':
            return 30 - int(day)
        elif month == '10':
            return 31 - int(day)
        elif month == '11':
            return 30 - int(day)
        elif month == '12':
            return 31 - int(day)
    else:
        if month == '01':
            return 31 - int(day)
        elif month == '02':
            return 28 - int(day)
        elif month == '03':
            return 31 - int(day)
        elif month == '04':
            return 30 - int(day)
        elif month == '05':
            return 31 - int(day)
        elif month == '06':
            return 30 - int(day)
        elif month == '07':
            return 31 - int(day)
        elif month == '08':
            return 31 - int(day)
        elif month == '09':
            return 30 - int(day)
        elif month == '10':
            return 31 - int(day)
        elif month == '11':
            return 30 - int(day)
        elif month == '12':
            return 31 - int(day)
