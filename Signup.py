import re
import pymongo
import bcrypt

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_info = db.user_info


def is_valid_phone(phone_number):
    pattern = re.compile(r"^\d{10}$")
    return pattern.match(phone_number)


def is_valid_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return pattern.match(email)


def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
    return pattern.match(password)


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def signup_function():
    while True:
        user_name = input("Please enter your username (max 16 characters, no special symbols):").strip()
        if len(user_name) > 16 or not re.match(r"^[a-zA-Z0-9_]+$", user_name):
            print('Invalid username. Must be max 16 characters, alphanumeric with underscores allowed.')
        elif user_info.find_one({'user_name': user_name}):
            print('Username already exists. Please choose a different one.')
        else:
            break

    while True:
        name = input("Please enter your full name (max 50 characters):").strip()
        if not (1 <= len(name) <= 50):
            print('Name must be between 1 and 50 characters.')
        elif not all(char.isalpha() or char.isspace() for char in name):
            print('Name must only contain alphabetic characters and spaces.')
        else:
            break

    while True:
        phone_number = input("Please enter your phone number (10 digits):").strip()
        if not is_valid_phone(phone_number):
            print('Invalid phone number. Must be exactly 10 digits.')
        else:
            break

    while True:
        email = input("Please enter your email:").strip()
        if not is_valid_email(email):
            print('Invalid email format.')
        elif user_info.find_one({'email': email}):
            print('Email already exists. Please use a different one.')
        else:
            break

    while True:
        password = input(
            "Please enter your password (at least 8 characters, with an uppercase, number, and special character):").strip()
        if not is_valid_password(password):
            print('Password does not meet the required criteria. Please try again.')
        else:
            password_hashed = hash_password(password)
            break

    valid_genders = ['male', 'female', 'transgender', 'trans', 'm', 'f', 't']
    while True:
        gender = input("Please enter your gender (Male/Female/Transgender):").strip().lower()
        if gender in valid_genders:
            break
        else:
            print('Invalid gender. Please enter Male, Female, or Transgender.')

    while True:
        try:
            age = int(input("Please enter your age (between 10 and 100):").strip())
            if 10 <= age <= 100:
                break
            else:
                print('Age must be between 10 and 100.')
        except ValueError:
            print('Invalid age. Please enter a numeric value.')

    user_info.insert_one({
        'user_name': user_name,
        'name': name,
        'phone_number': phone_number,
        'email': email,
        'password': password_hashed,
        'gender': gender,
        'age': age
    })

    print('Registered successfully! You can now log in.')


signup_function()
