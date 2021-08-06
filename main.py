# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com

from menu import Menu
from Tester import Tester
from server import Server
version = "v.1.0.0B2"
auth = False   # function for setting the auth
log = []       # function for logging data
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
    menu = Menu(user_input)
    menu.run()
    auth = menu.auth
    flag = menu.flag

# main function for running script
def run():
    print("faceAPI is currently running")
    flag = True
    while(flag):
        user_input  =input(">")
        understand(user_input)

if __name__ == '__main__':
    show_header()
    run()



