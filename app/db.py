import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


def get_connect():
    conn = pymysql.connect(host=os.getenv("DB_HOST")
                           , user=os.getenv("DB_USER")
                           , password=os.getenv("DB_PASS"))
    return conn


def create_db(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydata")
    conn.select_db("mydata")
    conn.commit()
    cursor.close()


def create_tabel(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS weapon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weapon_id VARCHAR(50),
    weapon_name VARCHAR(50),
    weapon_type VARCHAR(50),
    range_km INT ,
    weight_kg float, 
    manufacturer VARCHAR(50),
    origin_country VARCHAR(50),
    storage_location VARCHAR(50),
    year_estimated INT,
    risk_level VARCHAR(50))  """)
    conn.commit()
    cursor.close()



def insert_into_db(conn,data):
    cursor = conn.cursor()
    sql = """INSERT INTO weapon
        (weapon_id,weapon_name,weapon_type,range_km,
        weight_kg,manufacturer,origin_country,
        storage_location,year_estimated,risk_level)
        VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)"""
    for d in data:
        cursor.execute(sql,(d['weapon_id'],d['weapon_name'],d['weapon_type'],
                            d['range_km'],d['weight_kg'],d['manufacturer'],
                            d['origin_country'],d['storage_location'],
                            d['year_estimated'],d['risk_level']))
    conn.commit()
    cursor.close()

#
# d = {'weapon_id': 'W-001',
#  'weapon_name': 'Falcon-7',
#   'weapon_type': 'Missile',
#    'range_km': 15,
#     'weight_kg': 85.5,
#      'manufacturer': 'Orion Systems',
#      'origin_country': 'Iran',
#       'storage_location': 'Warehouse-A'
#       , 'year_estimated': 2016,
#        'risk_level': 'low'}
#
#
# insert_into_db(c,[d])
