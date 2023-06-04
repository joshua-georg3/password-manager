from cryptography.fernet import Fernet
import keyring


#set username and password on your pc by pasting this on your command prompt:

# python
# import keyring
# keyring.set_password(service_name="password_manager", username="______", password="_____")
# x = keyring.get_credential(service_name="password_manager", username=None)

#if you dont have keyring - 'pip install keyring' in terminal

x = keyring.get_credential(service_name="password_manager", username=None)
username_var = x.username
password_var = x.password

user = input("Enter the username: ")
passw = input("Enter the password: ")



'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ",
                   fer.decrypt(passw.encode()).decode())    

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    mode = input("Would you like to add new password or view existing ones (view, add or q to quit)? ")
    if mode == "q" and user == username_var and passw == password_var:
        break

    if mode == "view" and user == username_var and passw == password_var:
        print("Welcome " + user + ", Here are your passwords:")
        view()
        continue
    elif mode == "add"and user == username_var and passw == password_var:
        print("Welcome " + user + ", add a new password:")
        add() 
        continue
    
    if mode == "view" and user != username_var or passw != password_var:
        print("Wrong username/password. Please try again")
        break
    elif mode == "add"and user != username_var or passw != password_var:
        print("Wrong username/password. Please try again")
        break
    else: 
        print("Invalid mode.")
        continue