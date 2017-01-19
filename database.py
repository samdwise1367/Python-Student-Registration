import sqlite3

class Db:
    def __init__(self):
                self.connection = sqlite3.connect("login.db")
                self.createTable()

    def createTable(self):
                #connection = sqlite3.connect("login.db")
        
        self.connection.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT, USERNAME TEXT NOT NULL,EMAIL TEXT, PASSWORD TEXT)")        
        self.connection.commit()

    def insertTable(self,name,user,email,password):
        print(name)
        print(user)
        print(email)
        print(password)
        self.connection.execute("INSERT INTO STUDENTS VALUES(?,?,?,?)",(name,user,email,password))
        self.connection.commit()

                
    def loginCheck(self,username,password):
        result = self.connection.execute("SELECT * FROM STUDENTS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        count = len(result.fetchall())
        print(count)
        #print(result.fetchall())
        for data in result:
            print("Username : ", data[1])
            print("Email : ", data[2])
            print("Password : ", data[3])
        
        if(count > 0):
            print("Login Successfully")
            return True
                
        else:
            print("You havent registered yet")
            return False



        
