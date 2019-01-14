import sqlite3
import time
import hashlib
import getPassword


def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        with sqlite3.connect("UPDB.db") as db:
            cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE username=? AND password=?",(username, hashlib.sha224(password.encode('utf-8')).hexdigest(),))
        results = cursor.fetchall()
        print(results)

        if results:
            print("Welcome ")
            break
        else:
            print("Username and password not recognized.")
            again = input("Do you wanna try again?(y/n): ")
            if(again.lower() == "n"):
                print("Bye!")
                time.sleep(1)
                break

def newUser():
    found = 0
    while found == 0:
        username = input("Please enter a username: ")
        if(" " not in username):
            db = sqlite3.connect("UPDB.db")
            cursor = db.cursor()
            findUser = ("SELECT * FROM user WHERE username = ?")
            cursor.execute(findUser,[(username)])

            if(cursor.fetchall()):
                print("Username taken.")
            else:
                found = 1
        else:
            print("No spaces aloud.")

    firstName = input("Enter your first name: ")
    surName = input("Enter your surname: ")
    password = input("Enter your password: ")
    password1 = input("Re-Enter your password: ")
    while password != password1:
        print("Passwords don't match please try again.")
        password = input("Enter your password: ")
        password1 = input("Re-Enter your password: ")
    insertData = """INSERT INTO user(username,firstname,surname,password)
    VALUES(?,?,?,?)"""
    cursor.execute(insertData, [(username),(firstName),(surName),(hashlib.sha224(password.encode('utf-8')).hexdigest())])
    db.commit()
    db.close()

def add_new_website(user_ID, website_name):
    level = 5
    length = 20
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO bank(userID,Website,website_password)
    VALUES(?,?,?)"""
    cursor.execute(insertData,[(user_ID),(website_name),(getPassword.generate(length,level))])
    print("Added website!")
    db.commit()
    db.close()

def get_website_password(user_ID, website_name):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT website_password FROM bank WHERE userID=? AND website=?",(user_ID,website_name),)
    results = cursor.fetchall()
    if(not results):
        print("no password found")
    else:
        print(results)


add_new_website(1,"facebook")