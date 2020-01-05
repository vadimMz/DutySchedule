import sqlite3 as sql
import datetime

now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
today = datetime.date.today().strftime('%d.%m.%Y %H:%M:%S')
tomorrow = (datetime.datetime.strptime(today, '%d.%m.%Y %H:%M:%S') + datetime.timedelta(days=1) + datetime.timedelta(hours=20)).strftime('%d.%m.%Y %H:%M:%S')
day_after_tomorrow = (datetime.datetime.strptime(today, '%d.%m.%Y %H:%M:%S') + datetime.timedelta(days=1) + datetime.timedelta(hours=20)).strftime('%d.%m.%Y %H:%M:%S')
select_today = "select name from test where '{}' between beg_date and end_date".format(now)
select_tomorrow = "select name from test where '{}' between beg_date and end_date".format(tomorrow)
print (select_today)
print (select_tomorrow)

def find_who_today():
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute(select_today)
        who_buf = cur.fetchall()
        who = str(who_buf)
    return "Сейчас по ЛИМС дежурит " + who[3:len(who)-4]



def find_who_tomorrow():
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute(select_tomorrow)
        who_buf = cur.fetchall()
        who = str(who_buf)
    return "Завтра по ЛИМС дежурит " + who[3:len(who)-4]


print(find_who_today())
print(find_who_tomorrow())

