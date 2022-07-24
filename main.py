#!/usr/bin/env python

import csv
import json
import sqlalchemy

base_path="D:\\Nebo\\ampersand\\data-engineering-main (1)\\data-engineering-main"

# connect to the database
#engine = sqlalchemy.create_engine("postgresql://username:password@hostname:portnumber/database")
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
connection = engine.connect()


metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
people = sqlalchemy.schema.Table('peoples', metadata, autoload=True, autoload_with=engine)
place = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)

# read the CSV people data file into the table
with open(f'{base_path}\\data\\people.csv', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        connection.execute(people.insert().values(given_name = row[0], family_name = row[1], date_of_birth = row[2], place_of_birth = row[3]))

# read the CSV places data file into the table
with open(f'{base_path}\\data\\places.csv', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        connection.execute(place.insert().values(city = row[0], county = row[1], country = row[2]))


# output the table to a JSON file
with open(f'{base_path}\\data\\summary_output.json', 'w', encoding="utf8") as json_file:     
    dob_place = connection.execute(f'select country, count(*) count_of_people_born  from (select a.given_name , a.family_name, a.date_of_birth, b.country from  {people} a left join {place} b on a.place_of_birth=b.city) a group by country')
    rows = [{'country': row[0], 'count_of_people_born': row[1]} for row in dob_place]
    json.dump(rows, json_file, separators=(',', ':'))
    
