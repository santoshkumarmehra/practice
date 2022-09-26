from bullet import Password
import mysql.connector as c
from getpass import getpass
import base64

mydb = c.connect(
  host="localhost",
  user="santosh",
  password="Mysql@12",
  database="pythondatabase",
  auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()
def registration():
    while True:
        print('\t','--Enter Field--')
        email=input("enter email: ")
        pwd=Password(prompt='enter password: ',hidden='*')
        password=pwd.launch()

        sample_string = password
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        password = base64_bytes.decode("ascii")

        sql = "INSERT INTO school (email,password) VALUES (%s, %s)"
        val = (email,password)
        mycursor.execute(sql, val)
        mydb.commit()
        print('\n1:Enter more user\n2:Exit')
        x=input('select option: ')
        if x=='2':
            return True


