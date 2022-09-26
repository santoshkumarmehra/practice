from registration import registration
# from login1 import login
import login1
def login():
    while True:
        print('\t''--select option--''\n''1:Registration\n2:Login\n3:Exit')
        x=input('Choose option = ')
        if x=='1':
            registration()
        elif x=='2':
            login1.login()
        elif x=='3':
            return True
        else:
            print('--try again--')

login()