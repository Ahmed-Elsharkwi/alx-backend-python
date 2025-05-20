import mysql.connector
import csv


def connect_db():
    """ connect to the mysql """
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahmede2*"
    )


    return mydb

def create_database(connection):
    """ create database function """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")

def connect_to_prodev():
    """ connect to the database """
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahmede2*",
            db="ALX_prodev"
    )

    return mydb

def create_table(connection):
    """ create table if does not exist """
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (user_id VARCHAR(36) PRIMARY KEY, name VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, age VARCHAR(20) NOT NULL)")

def insert_data(connection, file):
    """ add data to the table """
    data = []

    with open(file, mode ='r')as file:
        csvFile = csv.reader(file)
        i = 0
        for line in csvFile:
            if i != 0:
                data.append(tuple(line))
            else:
                i = 1

    cursor = connection.cursor()
    insert_st = "INSERT INTO user_data (user_id, name, email, age) VALUES (UUID(), %s, %s, %s)"
    cursor.executemany(insert_st, data)
    connection.commit()
