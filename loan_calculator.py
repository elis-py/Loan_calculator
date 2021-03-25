# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:48:34 2021

@author: efrem
"""
import math
import argparse


def diff_pay(principal, periods, interest):
    """Computing differential monthly payment"""
    payment_all = 0
    for month in range(1, periods + 1):
        payment = principal / periods + (interest / 1200) * \
            (principal - ((principal * (month - 1)) / periods))
        payment_all += math.ceil(payment)
        print(f'Month {month}: payment is {math.ceil(payment)}')
    print(f'\nOverpayment = {round(payment_all) - principal}')

def annuity_principal(payment, periods, interest): 
    """Computing annuity loan"""
    principal = payment / (((interest / 1200) * (1 + (interest / 1200)) ** periods) / \
                           ((1 + (interest / 1200)) ** periods - 1))
    print(f'Your loan principal = {math.ceil(principal)}!')
    print(f'Overpayment = {periods * payment - math.ceil(principal)}')

def annuity_payment(principal, periods, interest): 
    """Computing annuity payment"""
    payment = principal * (((interest / 1200) * (1 + (interest / 1200)) \
                                 ** periods) / ((1 + (interest / 1200)) ** periods - 1))
    print(f'Your monthly payment = {math.ceil(payment)}!')
    print(f'Overpayment = {periods * math.ceil(payment) - principal}')

def annuity_periods(principal, payment, interest): 
    """Computing periods for annuity loan"""
    periods = math.log((payment /(payment - (interest / 1200) * principal)), ((interest / 1200) + 1))
    if math.ceil(periods // 12) == 0:
        if math.ceil(periods % 12) == 1:
            print('It will take 1 month to repay this loan!')
        elif math.ceil(periods % 12) == 12:
            print('It will take 1 year to repay this loan!')
        else:
            print(f'It will take {math.ceil(args.periods % 12)} months to repay this loan!')
    elif math.ceil(periods // 12) == 1:
        if math.ceil(periods % 12) == 0:
            print('It will take 1 year to repay this loan!')
        elif math.ceil(periods % 12) == 1:
            print('It will take 1 year and 1 month to repay this loan!')
        elif math.ceil(periods % 12) == 12:
            print('It will take 2 years to repay this loan!')
        else:
            print(f'It will take 1 year and {math.ceil(periods % 12)} months to repay this loan!')
    else:
        if math.ceil(periods % 12) == 0:
            print(f'It will take {math.ceil(periods // 12)} years to repay this loan!')
        elif math.ceil(periods % 12) == 1:
            print(f'It will take {math.ceil(periods // 12)} years and 1 month to repay this loan!')
        elif math.ceil(periods % 12) == 12:
            print(f'It will take {math.ceil(periods // 12) + 1} years to repay this loan!')
        else:
            print(f'It will take {math.ceil(periods // 12)} years and {math.ceil(periods % 12)} months to \
            repay this loan!')
    print(f'Overpayment = {math.ceil(periods) * payment - principal}')

parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("--type", help="You need to input type of loan (diff or annuity)")
parser.add_argument("--periods", help="You need to input number of months (positive number)", type=int)
parser.add_argument("--principal", help="You need to input loan amount (positive number)", type=int)
parser.add_argument("--payment", help="You need to input the annuity monthly payment amount (positive number)", type=int)
parser.add_argument("--interest", help="You need to input the interest rate (positive integer or float number)", type=float)

args = parser.parse_args()

t = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
parameters = [principal, periods, interest, payment]

for arg in parameters:  # check if any of the parameters have negative value
    if arg is not None and arg < 0:
        print('Incorrect parameters')
        exit()

if t not in ['diff', 'annuity'] or not interest:  # check the presence of required parameters
    print('Incorrect parameters')
elif parameters.count(None) > 1: 
    print('Incorrect parameters')
else:
    if t == 'diff':
        if payment:
            print('Incorrect parameters')
        else:
            diff_pay(principal, periods, interest)
    elif t == 'annuity':
        if periods == None:
            annuity_periods(principal, payment, interest)
        elif args.payment == None:
            annuity_payment(principal, periods, interest)
        elif args.principal == None:
            annuity_principal(payment, periods, interest)