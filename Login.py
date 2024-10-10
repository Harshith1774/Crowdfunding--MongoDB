import pymongo
import bcrypt
from datetime import datetime

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_info = db.user_info
user_logs = db.user_logs


def log_user_login(user_name, email):
    user_logs.insert_one({
        'user_name': user_name,
        'email': email,
        'logged_in_at': datetime.now()
    })


def login_function():
    while True:
        username_or_email = input("Please enter your username or email:").strip()
        user = user_info.find_one({'$or': [{'user_name': username_or_email}, {'email': username_or_email}]})
        if user:
            print(f"Username or email found. Welcome {user['name']}!")
            max_attempts = 5
            attempts = 0
            while attempts < max_attempts:
                password = input("Please enter your password:").strip()

                if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                    log_user_login(user['user_name'], user['email'])
                    print(f'Login successful! Welcome, {user["name"]}!')
                    return
                else:
                    attempts += 1
                    remaining_attempts = max_attempts - attempts
                    print(f"Incorrect password. You have {remaining_attempts} attempts left.")

            print("Too many incorrect password attempts. Login failed.")
            return
        else:
            print('User not found. Please check your username or email and try again.')


login_function()
