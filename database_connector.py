# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com
import mysql.connector
from mysql.connector import Error

class Database_Connector:

    # constructor
    def __init__(self):
        self.database_name = ""
        self.database_user = ""
        self.database_password = ""
        self.database_ip = ""
        self.connector = None
        self.connected = False
        self.cursor = None

    # function for creating connections
    def connect(self,database_ip,database_name,database_user,database_password):
        self.database_name = database_name
        self.database_user = database_user
        self.database_password = database_password
        self.database_ip = database_ip

        try:
            self.connector = mysql.connector.connect(
                host=self.database_ip,
                database = self.database_name,
                user=self.database_user,
                password=self.database_password
            )
            db_Info = self.connector.get_server_info()
            print("Connected to MySQL Server version " + db_Info)
            self.cursor = self.connector.cursor()
            self.cursor.execute("select database();")
            record = self.cursor.fetchone()
            print("You're connected to database: ", record)
            self.connected = True

        except Error as e:
            print("Error connecting to the database: ",e)
            self.connected = False

database = Database_Connector()
database.connect("localhost","entrc_database","root","password")
print(database.connected)
