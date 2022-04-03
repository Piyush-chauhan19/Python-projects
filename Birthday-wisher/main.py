import datetime as dt
import smtplib
import pandas
import random

user = "YOUR MAIL ID"
password = "YOUR PASSWORD"

birthdays = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
birthdates = {a: (b["month"], b["day"]) for (a, b) in birthdays.iterrows()}

for date in birthdates:
    if birthdates[date] == (now.month, now.day):
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as content:
            message = content.read()
            msg = message.replace("[NAME]", birthdays.values[date][0])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs=birthdays.values[date][0], msg=f"Happy Birthday!!!\n\n{msg}")
        print(f"from {user} to {birthdays.values[date][0]}", f"Subject:Happy Birthday\n\n{msg}")
