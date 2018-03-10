import sqlite3 as mydb
import json
import sys

message = sys.argv[1]

start = message[:6]
end = message[6:]

f = open('/home/pi/EL/Web_Assignment/public/data.json','w')
sys.stdout = f

con = mydb.connect('/home/pi/EL/tempLog/temperature.db')

def query_db(query, args=(), one=False):
  
  cur = con.cursor()
  cur.execute(query, args)
  r = [dict((cur.description[i][0], value) \
    for i, value in enumerate(row)) for row in cur.fetchall()]
  con.close()
  return (r[0] if r else None) if one else r

my_query = query_db('select * from TempData where date(substr(date_time,7,2)||substr(date_time,0,3)||substr(date_time,4,2)) between date(?) and date(?)',(start,end,))

json_output = json.dumps(my_query)

print (json_output)
sys.stdout.flush()
f.close()



