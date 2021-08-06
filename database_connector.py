# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com
<<<<<<< HEAD
import mysql.connector
from mysql.connector import Error

=======
import mysql
>>>>>>> b89e7e2f58f16e75902bdd7960917d544e7374d0
class Database_Connector:

    # constructor
    def __init__(self):
<<<<<<< HEAD
=======
        self.connection = None
>>>>>>> b89e7e2f58f16e75902bdd7960917d544e7374d0
        self.database_name = ""
        self.database_user = ""
        self.database_password = ""
        self.database_ip = ""
        self.connector = None
        self.connected = False
<<<<<<< HEAD
        self.cursor = None

    # function for creating connections
    def connect(self,database_ip,database_name,database_user,database_password):
=======

    # function for creating connections
    def connection(self,database_ip,database_name,database_user,database_password):
>>>>>>> b89e7e2f58f16e75902bdd7960917d544e7374d0
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
<<<<<<< HEAD
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
=======
            self.connected = True

        except:
            self.connected = False
>>>>>>> b89e7e2f58f16e75902bdd7960917d544e7374d0
