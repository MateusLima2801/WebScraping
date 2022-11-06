from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import mysql.connector;

db_connection = mysql.connector.connect( host='localhost', user='root',
                        password='xxxx', database='jsons')

cursor = db_connection.cursor()
table = 'jsons.info'

html = urlopen('http://jsonplaceholder.typicode.com/todos')
bs = BeautifulSoup(html.read(), 'html.parser')
data = json.loads(bs.text)

query = f'delete from {table} where id > 0'
cursor.execute(query)

for i in range(0,len(data)):
    data[i]['completed'] = 1 if (data[i]['completed'] == True) else 0
    query = 'insert into {} values({}, {}, \'{}\', {})'.format(table, data[i]['userId'], data[i]['id'], data[i]['title'], data[i]['completed'])
    cursor.execute( query )  

db_connection.commit()
cursor.close()
db_connection.close()