import smtplib

import  pandas as pd
import  datetime
import  random
today = (datetime.datetime.now().month,datetime.datetime.now().day)
# print(today)
data = pd.read_csv("birthdays.csv")
# print(data)
new_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today in new_dict:
    rn = random.randint(1,3)
    file_path=f"letter_templates/letter_{rn}.txt"
    print(file_path)
    birth_person =new_dict[today]
    print(birth_person["name"])
    with open(file_path) as letter_file:
        content = letter_file.read()
        content=content.replace("[NAME]",birth_person["name"])
        print(content)
    my_user="manpatel080802@gmail.com"
    password="jmqsbnavffcmsnne"
    print(birth_person["email"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_user,password=password)
        connection.sendmail(from_addr=my_user,to_addrs=birth_person["email"],msg=f"Subject:Happy Birthday\n\n {content}")

    # print(content)

