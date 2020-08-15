from docopt import docopt
from api import *
from tabulate import tabulate

usage = '''
Usage:
    spent_app.py --init
    spent_app.py --show [<-Event->]
    spent_app.py --add <Price> <Event> [<-Message->]
'''

args = docopt(usage)

if args['--init']:
    init()
    print('Your table successfully created.')

if args['--show']:
    event = args['<-Event->']
    total_price, result = show(event)
    print()
    print('Total expenses:',total_price)
    print(tabulate(result))

if args['--add']:
    try:
        price = int(args['<Price>'])
        add(price, args['<Event>'], args['<-Message->'])
        print('Item added.')
    except:
        print(usage)
        