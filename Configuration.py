# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com

#config.entrconf
file_path = "config.entrconf"
class Configuration:

    # constructor
    def __init__(self):
        self.loaded = False
        self.error = False
        self.nofile = False
        self.database_ip = ""
        self.database_name = ""
        self.database_user = ""
        self.database_password = ""
        self.config_file = None


    # function for loading data from user input
    def insert_data(self):
        self.database_ip = input("ip?")
        self.database_name = input("database name?")
        self.database_user = input("database user?")
        self.database_password = input("database password?")
        print("Data loaded")

    # function for showing config
    def show_config(self):
        print("Loaded data:")
        print("ip: "+self.database_ip)
        print("database: "+self.database_name)
        print("databaseuser: "+self.database_user)
        print("databasepass: "+self.database_password)
        print("END.")

    # function for creating file
    def create_file(self):
        self.config_file = open(file_path,"w")

        self.config_file.write("ip%"+self.database_ip+"\n")
        self.config_file.write("database%"+self.database_name+"\n")
        self.config_file.write("databaseuser%"+self.database_user+"\n")
        self.config_file.write("databasepass%"+self.database_password+"\n")

        self.config_file.close()
        print("File created.")

    # function for loading file
    def load_file(self):
        try:
            self.config_file = open(file_path, "r")
            print("Loading file...")
            # reading the file
            for line in self.config_file.readlines():
                if "ip" in line:

                    try:
                        self.database_ip = line.split("%")[1][0:len(line.split("%")[1])-1]
                    except:
                        self.loaded = False
                        self.error = True
                        break
                        

                elif "database%" in line:

                    try:
                        self.database_name = line.split("%")[1][0:len(line.split("%")[1])-1]
                    except:
                        self.loaded = False
                        self.error = True
                        break
                elif "databaseuser%" in line:

                    try:
                        self.database_user = line.split("%")[1][0:len(line.split("%")[1])-1]
                    except:
                        self.loaded = False
                        self.error = True
                        break

                elif "databasepass%" in line:
                    try:
                        self.database_password = line.split("%")[1][0:len(line.split("%")[1])-1]
                    except:
                        self.loaded = False
                        self.error = True
                        break

            self.loaded = True
        
        except Exception as e:
            print("Error loading configuration file: "+str(e))
            self.error = True
            self.loaded = False
            self.nofile = True

