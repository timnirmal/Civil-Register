# -- User Table
# ---- UserID, Name, Password
import sqlite3

import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd

dataString = ""


def random_join_date_generator():
    now = datetime.datetime.now()
    generated = randomtimestamp.randomtimestamp(start_year=2005, end_year=2022)

    # IF generated timestamp is in the future, then generate a new one
    while generated > now:
        generated = randomtimestamp.randomtimestamp(start_year=2005, end_year=2022)

    return generated.strftime("%m/%d/%Y, %H:%M:%S")


def random_date_generator():
    now = datetime.datetime.now()
    generated = randomtimestamp.randomtimestamp(start_year=1900, end_year=2022)

    # IF generated timestamp is in the future, then generate a new one
    while generated > now:
        generated = randomtimestamp.randomtimestamp(start_year=1900, end_year=2022)

    return generated.strftime("%m/%d/%Y, %H:%M:%S")


def generate_person():
    first_name = randominfo.get_first_name(gender=None)
    name = first_name + " " + randominfo.get_last_name()
    password = randominfo.random_password(length=8)
    dob = randominfo.get_birthdate()
    phone = randominfo.get_phone_number()
    joined_date = random_join_date_generator()

    # to json Name, Password, DOB, Phone, JoinedAt
    person = {
        "Name": name,
        "Password": password,
        "DOB": dob,
        "Phone": phone,
        "JoinedAt": joined_date
    }

    return person


def generate_people(count):
    people = [generate_person() for i in range(count)]
    return people


if __name__ == "__main__":
    with sqlite3.connect('../Database.db') as db:
        c = db.cursor()

    print("Generating Data...")
    people = generate_people(10)
    # list to dataframe
    df = pd.DataFrame(people)
    print(df)

    # save data to sqllite database in users table
    insert = 'INSERT INTO user(Name,Password,DOB,Phone,JoinedAt) VALUES(?,?,?,?,?)'
    # for each item in df c.execute(insert, (df['Name'], df['Password'], df['DOB'], df['Phone'], df['JoinedAt']))
    for index, row in df.iterrows():
        c.execute(insert, (row['Name'], row['Password'], row['DOB'], row['Phone'], row['JoinedAt']))

    db.commit()
    db.close()


