import datetime as dt
import pandas as pd
import smtplib
import random

# Email info
MY_EMAIL = ""
MY_PASSWORD = ""

# Today's date
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today_tuple = (today_month, today_day)

# Read csv and make it a dictionary
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today is the birthday
if today_tuple in birthdays_dict:
    # Handle the letter
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", birthdays_dict[today_tuple]["name"])

    # Send e-mail with the letter
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today_tuple]["email"],
            msg=f"Subject:Happy Birthday!!\n\n{letter_content}",
        )
