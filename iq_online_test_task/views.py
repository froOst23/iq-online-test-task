#!/usr/bin/python3
# -*- coding: utf-8 -*-

from iq_online_test_task import app
from flask import render_template, url_for, request
from iq_online_test_task.accessory import rest_of_day, the_year_is_leap, bank_interest_rate

menus = [
    {'item' : 'Кредитные карты', 'url' : '/index'},
    {'item' : 'Вклады', 'url' : '/index'},
    {'item' : 'Дебетовая карта', 'url' : '/index'},
    {'item' : 'Страхование', 'url' : '/index'},
    {'item' : 'Друзья', 'url' : '/index'},
    {'item' : 'Интернет-банк', 'url' : '/index'}
]

phones = [
    '8-800-100-5005',
    '+7 (3452) 522-000'
]

sub_menus = [
    {'item' : 'Главная', 'url' : '/index'},
    {'item' : 'Вклады', 'url' : '/index'},
    {'item' : 'Калькулятор', 'url' : '/index'}
]

deposit_amount = 1000
deposit_replenishment_amount = 1000
date_contribution = ''
term_of_deposit = 1
deposit_replenishment = True
message = ''


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    global menus, deposit_amount, deposit_replenishment_amount
    global date_contribution, term_of_deposit, deposit_replenishment, message

    if request.method == 'POST':
        date_contribution = request.form.get('date_contribution')
        deposit_amount = request.form.get('deposit_amount')
        term_of_deposit = request.form.get('term_of_deposit')
        deposit_replenishment = request.form.get('deposit_replenishment')
        deposit_replenishment_amount = request.form.get('deposit_replenishment_amount')

    year = date_contribution[0:4]
    month = date_contribution[5:7]
    day = date_contribution[8:10]

    if deposit_replenishment == None or date_contribution == '':
        message = 'Пожалуйста, заполните все необходимые поля'
        result = 0
        pass
    else:
        rest_day = rest_of_day(day, month, year)
        message = ''
        if the_year_is_leap(year) == True:
            if deposit_replenishment == "True":
                result = round(int(deposit_amount) + (int(deposit_amount) + int(deposit_replenishment_amount)) * rest_day * (bank_interest_rate(int(deposit_amount)) / 366), 2)
            else:
                result = round(int(deposit_amount) + rest_day * (bank_interest_rate(int(deposit_amount)) / 366), 2)
        else:
            if deposit_replenishment == "True":
                result = round(int(deposit_amount) + (int(deposit_amount) + int(deposit_replenishment_amount)) * rest_day * (bank_interest_rate(int(deposit_amount)) / 365), 2)
            else:
                result = round(int(deposit_amount) + rest_day * (bank_interest_rate(int(deposit_amount)) / 365), 2) 

    return render_template('index.html', title='web_development_test', 
                                         menus=menus,
                                         phones=phones, 
                                         sub_menus=sub_menus, 
                                         date_contribution=date_contribution, 
                                         deposit_amount=deposit_amount,
                                         term_of_deposit=term_of_deposit,
                                         deposit_replenishment=deposit_replenishment,
                                         deposit_replenishment_amount=deposit_replenishment_amount,
                                         result=result,
                                         message=message)
