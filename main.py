import smtplib
import datetime as dt
import random
import pandas as pd
#################################################################
PLACEHOLDER = "[NAME]"
lists = ['letter_1.txt','letter_2.txt']
########################################################################

my_email = "kichukip80@gmail.com"
pass_word = "adithyanbg"

def sendmail(email, subject):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=pass_word)
        connection.sendmail(from_addr=my_email, to_addrs= email,msg=f'subject:birthday\n\n{subject}')
###############################################################################################

dataset = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
mins = now.minute
if month in dataset['month'].values and day in dataset['day'].values:
  ds = dataset[(dataset['month'] == month) & (dataset['day'] == day)]
  a = ds.to_dict('records')
  for i in a:
    ram = random.choice(lists)
    s = i['name']
    y = i['email']
    with open(ram, 'r') as file:
      filedata = file.read()
    filedata = filedata.replace(PLACEHOLDER, s)
    with open('letter_3.txt', 'w') as file:
      file.write(filedata)
      print(filedata)
    sendmail(y, filedata)
    ########################################################################
    with open(ram, 'r') as file:
      filedata = file.read()
    filedata = filedata.replace(s, PLACEHOLDER)
    with open('letter_3.txt', 'w') as file:
      file.write(filedata)
    print(s, y)
