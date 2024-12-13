import pymysql
from peewee import *


def connect_db():
    mysql_db = MySQLDatabase('ZagS1234_TaxiServ',
                             user='ZagS1234_taxi',
                             password='123456',
                             host='10.11.13.118',
                             port=3306)
    return mysql_db

if __name__ ==  "__main__":
    try:
        connect_db().connect()
        print("Вы подключены к БД")
    except OperationalError as error:
        print(f'Ошибка подключения к базе данных, {error}')