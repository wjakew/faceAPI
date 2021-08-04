# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com
import mysql
class Database_Connector:

    # constructor
    def __init__(self):
        self.connection = None
        self.database_name = ""
        self.database_user = ""
        self.database_password = ""
        self.database_ip = ""
        self.connector = None
        self.connected = False

    # function for creating connections
    def connection(self,database_ip,database_name,database_user,database_password):
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
            self.connected = True

        except:
            self.connected = False
