#!/usr/bin/python3

seed = __import__('seed')


def stream_users_ages():
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
            "age": int(row[3])
        }
        yield new_dict

    cursor.close()

def main():
    """ main function """
    sum_ages = 0
    count = 0

    for user in stream_users_ages():
        count += 1
        sum_ages += user['age']

    print(sum_ages / count)

main()
