#!/usr/bin/python3

seed = __import__('seed')


def stream_users():
    """ fetch the data and return it using yield """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data;")
    rows = cursor.fetchall()


    for row in rows:
        new_dict = {
            "user_id": row[0],
            "name": row[1],
            "email": row[2],
            "age": row[3]
        }
        yield new_dict

    cursor.close()
