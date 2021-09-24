# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com
from server import Server
debug = 1
# object for maintaing server functions
class Menu:

    # constructor
    def __init__(self,user_input,database):
        self.user_input = user_input
        self.auth = False
        self.flag = True
        self.database = database

    # function for running the server
    def run(self):
        if debug == 1:
            print("User input: "+self.user_input)
        words = self.user_input.split()

        for word in words:
            # exit option
            if ( word == "exit"):
                print("Exiting server...")
                self.flag = False
                break
            elif (word == "run"):
                print("Preparing to run server...")
                server = Server()
                server.run()
                break;
            else:
                print("No keyword found")
            

