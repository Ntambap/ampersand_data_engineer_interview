# Ampersand Data Engineer Interview.
CSV File Loader for people birth locations and their countries using Python and managed in docker container.

# 1) step is to create a schema on the postgres Database.

Created the two tables for peoples and places data sets , i created a postgres database and created the schema through SQL Shell.
The schema can be found in the people_schema.sql file.

# 2) step was to create the python script that loads the peoples csv and places csv files into the tables created in postgres DB. 

The file is open and read a record at a time into the database. 

# 3) step was to create the docker-compose.yml file.

Create the file with two services database which contains the details for the postgres db and app service which contains the details for the data loading pipeline.

# 4) step was to run the compose command to generate the image.
