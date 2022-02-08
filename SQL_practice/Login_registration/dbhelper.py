import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                database="hit-db-demo")

            self.mycursor = self.conn.cursor()        # cursor is an object which is interact with database.
                                                      # eta diye data base er sathe kotha bola jay.
        except:
            print("Some error occured.Could not connect to database")
        else:
            print("Connected with Database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute("""        
            INSERT INTO `users_info` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}','{}','{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1    # something wrong
        else:
            return 1
    def search(self,email,password):

        self.mycursor.execute(""" SELECT * FROM users_info WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))

        data = self.mycursor.fetchall()
        print(data)

