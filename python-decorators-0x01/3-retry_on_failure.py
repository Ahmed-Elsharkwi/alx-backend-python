import time
import sqlite3 
import functools

def with_db_connection(func):
    """handles opening and closing database connections"""
    def wrapper():
        conn = sqlite3.connect('users.db')
        users = func(conn)
        conn.close()
        return users

    return wrapper


def retry_on_failure(retries, delay):
    """ retry on failure """
    def inner(func):
        def wrapper(conn):
            users = "there is an error happend"
            for _ in range(0, retries):
                try:
                    users = func(conn)
                except sqlite3.Error:
                    time.sleep(delay)
            return users
        return wrapper
    return inner

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
