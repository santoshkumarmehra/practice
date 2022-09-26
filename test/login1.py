from bullet import Password
import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="santosh",
  password="Mysql@12",
  database="pythondatabase",
  auth_plugin='mysql_native_password',
)
mycursor = mydb.cursor()

def login():
    while True:
        import base64
        f="select * from school"
        mycursor.execute(f)
        myresult = mycursor.fetchall()
        s1=set()
        s2=set()
        for e,p in myresult:
            base64_string=p
            base64_bytes = base64_string.encode("ascii")
            sample_string_bytes = base64.b64decode(base64_bytes)
            p = sample_string_bytes.decode("ascii")
            s1.add(e)
            s2.add(p)
        email=input("enter email: ")
        if email in s1:
            pwd=Password(prompt='enter password: ',hidden='*')
            password=pwd.launch()
            if password in s2:
                print("--you have login successfully--")
                return True                
        else:
            print('\t'"--try again--")


# login()
# mycursor.execute("delete from school")
# mydb.commit()

