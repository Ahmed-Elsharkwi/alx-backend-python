#!/usr/bin/python3
seed = __import__('seed')


def stream_users_in_batches(batch_size):
    """ fetch the data and return it in batches using yield """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data;")
    rows = cursor.fetchall()
    empty_list = []
    count = 0

    for row in rows:
        if count == batch_size:
            yield empty_list
            count = 0
            empty_list = []

        new_dict = {
            "user_id": row[0],
            "name": row[1],
            "email": row[2],
            "age": int(row[3])
        }
        empty_list.append(new_dict)
        count += 1

    cursor.close()

def batch_processing(batch_size):
    """ that processes each batch to filter users over the age of25 """
    for batch in stream_users_in_batches(batch_size):
        for element in batch:
            if element['age'] > 25:
                print(element)
