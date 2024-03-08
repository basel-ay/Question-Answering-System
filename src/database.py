# Database interaction functions

# Import necessary libraries and modules
import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, database_name):
    """
    Function to create a connection to the MySQL server.

    Args:
        host_name (str): The hostname or IP address of the MySQL server.
        user_name (str): The username used to authenticate with the MySQL server.
        user_password (str): The password used to authenticate with the MySQL server.
        database_name (str): The name of the MySQL database to connect to.

    Returns:
        connection (mysql.connector.connection.MySQLConnection): The MySQL database connection object.
    """
    connection = None

    try:
        # Attempt to establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database_name,
            auth_plugin="mysql_native_password",
            buffered=True,
        )

        return connection

    except Error as err:
        # Handle any errors that occur during connection establishment
        # print(f"Error: {err}")
        return f"Error: {err}"


