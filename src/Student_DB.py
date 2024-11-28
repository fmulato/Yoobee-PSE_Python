import sql_statement as sql_st
import configparser
import mysql.connector
from mysql.connector import Error

configfile = 'C:/Users/fmula/Documents/Yoobee/Subjects/Term_1/PSE-Professional_Software_Eng/Python/configfile.ini'

class Database:

    def __init__(self, filename=configfile):
        self.config_filename = filename
        self.connection = None
        self._init_database()

    def _init_database(self):
        config = self.load_config()
        self.connection = mysql.connector.connect(**config, autocommit=True)
        if self.connection.is_connected():
            self._check_database_exist()
            self._check_table_exist()
            return True
        return False

    def creat_connection_parser(self):
        config = self.load_config()
        self.connection = mysql.connector.connect(**config, autocommit=True)
        if self.connection.is_connected():
                return self.connection.cursor()
        else:
            raise Exception()

    def load_config(self, filename=configfile):
        config = configparser.ConfigParser()
        config.read(filename, encoding='utf-8')
        return {key: value for key, value in config['mysql'].items()}

    def _check_database_exist(self):
        config = self.load_config()
        if not config.get("database"):
            config["database"] = sql_st.DEFAULT_DB_NAME
            self._save_config(config)

        cursor = self.creat_connection_parser()
        cursor.execute(f"{sql_st.CREATE_DB}{config["database"]};")

    def _check_table_exist(self):
        cursor = self.creat_connection_parser()
        cursor.execute(sql_st.CREATE_STUDENT_TABLE)

    def _save_config(self, config):
        config_parser = configparser.ConfigParser()
        config_parser["mysql"] = config
        with open(self.config_filename, 'w') as configfile:
            config_parser.write(configfile)

    def add(self):
        try:
            cursor = self.creat_connection_parser()
            self.name = input("Type the name of the student: ").upper()
            self.address = input("Type the address of the student:").upper()
            self.age = input("Type the age of the student:").upper()
            values = (self.name, self.address, self.age)
            cursor.execute(sql_st.INSERT_STUDENT, values)
            new_student_id =  cursor.lastrowid
            print('Values inserted!')
            print(f'Student added with ID: {new_student_id}')
        except Error as e:
            print(f'Error: {e}')

    def update(self):
        try:
            cursor = self.creat_connection_parser()
            id = input("Type the student's ID to update: ").upper()
            self.address = input("Type the new address of the student: ").upper()
            self.age = int(input("Type the new age of the student: "))
            new_values = (self.address, self.age, id)
            cursor.execute(sql_st.UPDATE_STUDENT, new_values)
            print(f'Values updated for ID = {id}!')
        except Error as e:
            print(f'Error: {e}')

    def delete(self):
        try:
            cursor = self.creat_connection_parser()
            self.id = int(input("Type the student's ID to delete: "))
            value = (self.id,)
            cursor.execute(sql_st.DELETE_STUDENT, value)
            print(f"Student's id {self.id} deleted!")
        except Error as e:
            print(f'Error: {e}')

    def query(self):
        try:
            cursor = self.creat_connection_parser()
            self.name = input("Type the name of the student: ").upper()
            value = (f"%{self.name}%",)
            cursor.execute(sql_st.FIND_STUDENT, value)
            myresult = cursor.fetchall()
            if myresult:
                print(f"Name: {myresult[0][0]}\n"\
                      f"Adress: {myresult[0][1]}\n"\
                      f"Age: {myresult[0][2]}")
            else:
                print("No student found with that name.")
        except Error as e:
            print(f'Error: {e}')

    def list_all(self):
        try:
            cursor = self.creat_connection_parser()
            cursor.execute(sql_st.LIST_ALL)
            myresult = cursor.fetchall()
            if myresult:
                # column's title
                titulos = ['Id', 'Name', 'Address', 'Age']
                print(f"{titulos[0]} - \t{titulos[1]} - \t{titulos[2]} - \t{titulos[3]}")
                # printing rows
                for id, name, address, age in myresult:
                    print(f"{id} - \t{name} - \t{address} - \t{age}")
            else:
                print("No student found with that name.")
        except Error as e:
            print(f'Error: {e}')

    def start(self):
        self.user_input = int(input(f"=================\n"
                           f"Type an option (choose a number):\n"
                           f"1 - to ADD a new student\n"
                           f"2 - to UPDATE a student profile\n"
                           f"3 - to DELETE a student\n"
                           f"4 - to SEARCH a student\n"
                           f"5 - to LIST ALL students\n"
                           f"0 - to EXIT\n"
                           f"-->"))

        if self.user_input == 1:
            self.add()

        elif self.user_input == 2:
            self.update()

        elif self.user_input == 3:
            self.delete()

        elif self.user_input == 4:
            self.query()

        elif self.user_input == 5:
            self.list_all()

        elif self.user_input == 0:
            print("Goodbye")
            quit()

        else:
            print("Invalid input. Please choose a valid option.")


if __name__ == '__main__':

    app = Database(configfile)

    while True:
        app.start()
