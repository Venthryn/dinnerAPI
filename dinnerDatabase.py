import sqlite3
import random
from datetime import datetime

def connectDatabase(dbName, rowMethod=sqlite3.Row):
    conn = sqlite3.connect(dbName)
    conn.row_factory = rowMethod
    cur = conn.cursor()
    return cur

def dataToDict(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def wipeDinnerList():
    conn = sqlite3.connect('dinners.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM WEEK')
    conn.commit()

def allDinners():
    cur = connectDatabase('dinners.db')
    cur.execute('SELECT * from MEALS')
    return str(cur.fetchall())
    
def randDinners():
    cur = sqlite3.connect('dinners.db')
    allDinners = cur.execute('SELECT ID, FOOD FROM MEALS WHERE EATEN = 0')
    allDinners = dict(allDinners)
    dinners = []
    n = random.sample(range(1, len(allDinners)), 7)
    for i in n:
        dinners.append(allDinners[i])
    setToEaten(allDinners, dinners)
    #dinners = random.sample(allDinners, 7)
    return dinners
def getKeys(d, val):
    return [i for i, v in d.items() if v == val]

def setToEaten(d, l):
    conn = sqlite3.connect('dinners.db')
    cur = conn.cursor()
    n = []
    for i in l:
        n.append(getKeys(d, i))
    for i in n:
        cur.execute(f'UPDATE MEALS SET EATEN = 1 WHERE ID = {i[0]}')
        conn.commit()
    
def revertEatenValues():
    cur = connectDatabase('dinners.db')
    cur.execute('UPDATE MEALS SET EATEN = 0')

def createDinnerList():
    conn = sqlite3.connect('dinners.db')
    cur = conn.cursor()
    rows = ('(DAY, FOOD)')
    values = ''
    n = 0
    for i in randDinners():
        values += f'({n}, \'{i}\'),'
        n += 1
    values = values[:-1]
    print(f'INSERT INTO WEEK {rows} VALUES {values};')
    cur.execute(f'INSERT INTO WEEK {rows} VALUES {values};')
    conn.commit()

def getTodaysDinner():
    day = datetime.today().weekday()
    cur = connectDatabase('dinners.db')
    cur.execute(f'SELECT * FROM WEEK WHERE DAY IS {day}')
    rows = cur.fetchall()
    return dict(rows)

def resetDinnerList():
    wipeDinnerList()
    createDinnerList()
    




if __name__ == '__main__':

    #wipeDinnerList()
    #createDinnerList()
    #print('dinners: ', randDinners())
    #createDinnerList()
    resetDinnerList()