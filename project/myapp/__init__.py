import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="Library", user='postgres', password='tanmay', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

sql = '''insert into public.\"Users\" values('1','Test','passwd')
 '''
  
cursor.execute(sql)
# Fetch a single row using fetchone() method.
cursor.execute("select * from public.\"Users\"")
data = cursor.fetchall()
print("Data: ",data)
conn.commit()
#Closing the connection
conn.close()
