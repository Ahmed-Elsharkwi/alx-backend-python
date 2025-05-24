import time
import sqlite3
import functools


def with_db_connection(func):
    """handles opening and closing database connections"""
    def wrapper(query):
        conn = sqlite3.connect('users.db')
        users = func(conn, query)
        conn.close()
        return users

    return wrapper

query_cache = {}

def cache_query(func):
    """ cache the result of the query """
    def wrapper(conn, query):
        if query not in query_cache:
            query_cache[query] = func(conn, query)
        
        return query_cache[query]
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
