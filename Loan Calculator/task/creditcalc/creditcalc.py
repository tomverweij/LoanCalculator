import math
import argparse

# parse arguments
parser = argparse.ArgumentParser("This program calculates loan stuff")

parser.add_argument('--interest', required=True)
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--principal')
parser.add_argument('--payment')
parser.add_argument('--periods')

try:
    args = parser.parse_args()
except:
    print('Incorrect parameters.')
    exit()

# fill loan components from arguments
i = float(args.interest) / 12 / 100

if args.principal is None:
    p = None
else:
    p = int(args.principal)

if args.payment is None:
    a = None
else:
    a = int(args.payment)

if args.periods is None:
    n = None
else:
    n = int(args.periods)

# print(i, p, a, n)

# exit()

def get_output_n():
    # calculate nbr of months
    try:
        n = math.log(a / (a - i * p), 1 + i)
    except ZeroDivisionError:
        print('Monthly payment too close to monthly interest.')
        exit()

    o = (a * math.ceil(n)) - p

    # calculate output string
    output = ['', '']
    n_years = math.floor(n / 12)
    n_months = math.ceil(n % 12)

    if n_years == 0:
        output[0] == ''
    elif n_years == 1 and n_months != 12:
        output[0] = '1 year'
    elif n_years > 1 and n_months != 12:
        output[0] = str(n_years) + ' years'
    elif n_years >= 1 and n_months == 12:
        output[0] = str(n_years + 1) + ' years'

    if n_months == 1:
        output[1] = str(n_months) + ' month'
    elif n_months > 1 and n_months != 12:
        output[1] = str(n_months) + ' months'
    else:
        output[1] = ''

    if output[0] == '':
        print('It will take ', output[1], ' to repay this loan!', sep='')
    elif output[1] == '':
        print('It will take ', output[0], ' to repay this loan!', sep='')
    else:
        print('It will take ', output[0], ' and ', output[1], ' to repay this loan!', sep='')

    print('Overpayment =', math.ceil(o))


def get_output_a():

    # calculate annuity
    a = math.ceil(p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    o = (a * n) - p

    print('Your annuity payment = ', a, '!', sep='')
    print('Overpayment =', math.ceil(o))


def get_output_p():
    # calculate loan principal
    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))

    print('Your loan principal = ', math.floor(p), '!', sep='')


def get_output_d():
    # calculate differentiated payments
    total_dm = 0
    for nth in range(1, n + 1):
        dm = math.ceil((p / n) + (i * (p - (p * (nth - 1)/n))))
        total_dm += dm
        print('Month ', nth, ': payment is ', dm, sep='')

    o = (total_dm) - p
    print('Overpayment =', math.ceil(o))

if n is None:
    get_output_n()
elif args.type == 'diff':
    get_output_d()
elif a is None:
    get_output_a()
elif p is None:
    get_output_p()
else:
    exit()

