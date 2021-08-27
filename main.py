# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com

from Configuration import Configuration
from database_connector import Database_Connector
from menu import Menu
from Tester import Tester
from server import Server
version = "v.1.0.0B3"
auth = False   # function for setting the auth
log = []       # function for logging data
flag = True
# global database connection
database = Database_Connector()
configuration = Configuration()

# main function of the program
# how to run server script:
#python3 main.py

# function for showing header
def show_header():
    header = "faceAPI "+version +"\n"
    header = header +"by Jakub Wawak 2021"
    print(header)

# function for understanding user input
def understand(user_input):
    menu = Menu(user_input,database)
    menu.run()
    global auth
    auth = menu.auth
    global flag
    flag = menu.flag

# main function for running script
def run():
    print("faceAPI is currently running")
    print("Searching for configuration file...")
    configuration.load_file()   # loading configuration file
    
    #creating configruation file if load_file = error
    if configuration.nofile:
        print("Cannot find configuration file")
        print("Loading configuration file creator:")
        configuration.insert_data()
        configuration.create_file()

    if  configuration.loaded :
        print("Configuration loaded!")
        print("Raw data:")
        configuration.show_config()
        database.connect(configuration.database_ip,configuration.database_name,configuration.database_user,configuration.database_password)

        if database.connected :
            print("faceAPI connected to "+database.database_name)

            api_password = database.check_api_state()
            # checking if API is ON on the database
            if  api_password != None:
                api_password = str(api_password)
                api_password.strip()
                print("API is active on the database")
                user_pass = input("password>")
                user_pass = "('"+user_pass+"',)"
                if user_pass == api_password:
                    print("Password correct")
                    # main loop of the program
                    while(flag):
                        user_input  =input(">")
                        understand(user_input)
                else:
                    print("Wrong password")
            else:
                print("API is not active on the database")
        else:
            print("Cannot connect to database")


# main function of the program
if __name__ == '__main__':
    show_header()
    run()



