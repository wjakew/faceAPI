# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com
debug = 1
# object for maintaing server functions
class Menu:

    # constructor
    def __init__(self,user_input):
        self.user_input = user_input
        self.auth = False
        self.flag = False

    # function for running the server
    def run(self):
        if debug == 1:
            print("User input: "+self.user_input)
        words = self.user_input.split()

        for word in words:
            # exit option
            if ( word == "exit"):
                print("Exiting server...")
                self.flag = True
                break
            if ( word == "auth"):
                if ( len(words) == 2 ):
                    password = input("password for "+words[1]+": ")
                else:
                    print("no authorization for '' user")

            

