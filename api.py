import sqlite3 as db
from datetime import datetime

#Here we made a connection to database
conn = db.connect('spent.db')

#Here we use "c" as a cursor for database
c = conn.cursor()

def init():
    ''' initialize a new table to store data'''
    c.execute('''CREATE TABLE IF NOT EXISTS expenses(
                price INTEGER,
                event TEXT COLLATE NOCASE,
                message TEXT,
                date TEXT
                )''')
    conn.commit()
    conn.close()


def add(price, event, message = ''):
    # add new item to data base
    now_time = str(datetime.now().strftime('%Y - %m - %d | %H : %M'))
    c.execute('INSERT INTO expenses VALUES (:price, :event, :message, :date)',{'price' : price , 'event' : event , 'message' : message , 'date' : now_time})
    conn.commit()
    conn.close()
    

def show(event = None):
    #Show all data in data base or with an event 
    if event:
        c.execute('SELECT * FROM expenses WHERE event = (:event)',{'event' : event})
        result = c.fetchall()
        c.execute('SELECT sum(price) FROM expenses WHERE event = :event',{'event':event })
        total_price = c.fetchone()[0]
    else:
        c.execute('SELECT * FROM expenses')
        result = c.fetchall()
        c.execute('SELECT sum(price) FROM expenses')
        total_price = c.fetchone()[0]

    return total_price, result
    conn.close()

