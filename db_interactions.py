import os
import psycopg2 as postgres

DATABASE_PASS = os.environ.get('DATABASE_PASS')

# UTILITY FUNCTION DEFINITION
def create_conn():
    return postgres.connect(
        host="localhost",
        database="grillvalley",
        user="gvbot",
        password=DATABASE_PASS
    )

# These functions are by design Injection safe. (As long as you pass the user input as parameter in the query) 
# Or at least this is what the docs says. And I'm blindly trusting them 
def __execute_query_single(conn: any, sql_statement: str, vars: list[str]):
    cursor = conn.cursor()

    try:
        cursor.execute(sql_statement, vars)
    except (Exception, postgres.DatabaseError) as error:
        cursor = None;
    
    result = None
    if cursor != None:
        result = cursor.fetchone();
        cursor.close()
    conn.commit()

    return result


def __execute_query_multiple(conn: any, sql_statement: str, vars: list[str]):
    cursor = conn.cursor()

    try:
        cursor.execute(sql_statement, vars)
    except (Exception, postgres.DatabaseError) as error:
        cursor = None;
    
    result = None
    if cursor != None:
        result = cursor.fetchall();
        cursor.close()

    conn.commit()
    return result


def __execute_mutation(conn: any, sql_statement: str, vars: list[str]):
    cursor = conn.cursor()

    try:
        cursor.execute(sql_statement, vars)
    except (Exception, postgres.DatabaseError) as error:
        cursor = None;

    if cursor != None:        
        cursor.close()

    conn.commit()
    return cursor != None;




# ACTUAL FUNCTIONS
# check user existence/validity
def check_if_user_exists(conn: any, user: str):
    statement = "SELECT username FROM bot.subscriptions WHERE username = %s;"
    found = __execute_query_single(conn, statement, [user])
    
    if found == None:
        # should never get here (I hope)
        return False;

    if found == None or found[0] != user:
        return False
    return True


def check_if_user_exists_and_valid(conn: any, user: str):
    statement = "SELECT username FROM bot.subscriptions WHERE username = %s AND withdrawn = 'N';"
    found = __execute_query_single(conn, statement, [user])
    
    if found == None:
        # should never get here (I hope)
        return False;

    if found == None or found[0] != user:
        return False
    return True



# Handle user
def add_user(conn: any, user: str, fullname: str):
    insert = "INSERT INTO bot.subscriptions (username, fullname, withdrawn) VALUES (%s, %s, 'N');"
    update = "UPDATE bot.subscriptions SET fullname = %s, withdrawn = 'N' WHERE username = %s;"

    if check_if_user_exists(conn, user):
        # user exist (it must have withdrawn some time ago)
        return __execute_mutation(conn, update, [fullname, user])
    else:
        # user is a new one
        return __execute_mutation(conn, insert, [user, fullname])

def withdraw_user(conn:any, user: str):
    withdraw = "UPDATE bot.subscriptions SET withdrawn = 'Y' WHERE username = %s;"

    if check_if_user_exists_and_valid(conn, user):
        # user exist 
        return __execute_mutation(conn, withdraw, [user])
    else:
        return False



# Manage the user direct input
def __wait_for_user_input(conn: any, user: str, input: str):
    query = "SELECT input_id FROM bot.inputs WHERE input_description = %s;"
    insert = "INSERT INTO bot.input_users VALUES (%s, %s);"

    result = __execute_query_single(conn, query, [input])
    
    if result == None:
        return False;

    input_id = result[0]
    return __execute_mutation(conn, insert, [user, input_id])


def wait_for_name_change(conn: any, user: str):
    return __wait_for_user_input(conn, user, "name_change")


def wait_for_food_allergies(conn: any, user: str):
    return __wait_for_user_input(conn, user, "food_allergies")


def wait_for_notes(conn: any, user: str):
    return __wait_for_user_input(conn, user, "notes")


def waiting_user(conn: any, user: str):
    query = "SELECT i.input_description FROM bot.inputs i INNER JOIN bot.input_users u ON i.input_id = u.input_type WHERE u.username = %s;"
    result = __execute_query_single(conn, query, [user])

    if result == None:
        return "no request";

    return result[0]


def stop_waiting(conn: any, user: str):
    deletion = "DELETE FROM bot.input_users WHERE input_users.username = %s;"
    return __execute_mutation(conn, deletion, [user])




if __name__ == "__main__":
    print(stop_waiting(create_conn(), "IvanMartini"))