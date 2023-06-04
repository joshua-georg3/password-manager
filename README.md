# Secure & encrypted password manager

Most advanced project yet


set username and password on your pc by pasting this on your command prompt:

python
import keyring
keyring.set_password(service_name="password_manager", username="______", password="_____")
x = keyring.get_credential(service_name="password_manager", username=None)

if you dont have keyring - 'pip install keyring' in terminal

copy rest of the code the same. Have fun!