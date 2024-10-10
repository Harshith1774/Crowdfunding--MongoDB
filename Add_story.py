import re
import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_story = db.user_story


def is_valid_name(name):
    return 3 <= len(name) <= 16 and name.replace(' ', '').isalpha()


def is_valid_gender(gender):
    return gender.lower() in ['male', 'female', 'transgender']


def is_valid_age(age):
    return 10 <= age <= 100


def is_valid_tag(tag):
    return 1 <= len(tag) <= 16 and re.match("^[a-zA-Z0-9_-]+$", tag)


def is_valid_idea(idea):
    return 1 <= len(idea.strip()) <= 150


def is_valid_amount(amount):
    return isinstance(amount, int) and amount > 0


def submit_user_story(name, gender, age, tag, idea, amount):
    user_story.insert_one({
        'Name': name,
        'Gender': gender,
        'Age': age,
        'Tag': tag,
        'Idea': idea,
        'Amount': amount,
        'Balance_amount': amount,
        'Upload_date': datetime.now()
    })
    return "User story submitted successfully."


def main():
    while True:
        name = input("Name (3-16 alphabetic characters): ").strip()
        if not is_valid_name(name):
            print("Name must be alphabetic and between 3 and 16 characters.")
        else:
            break

    while True:
        gender = input("Gender (Male/Female/Transgender): ").strip().lower()
        if not is_valid_gender(gender):
            print("Invalid gender. Please choose 'Male', 'Female', or 'Transgender'.")
        else:
            break

    while True:
        try:
            age = int(input("Age (10-100): ").strip())
            if not is_valid_age(age):
                print("Age must be between 10 and 100.")
            else:
                break
        except ValueError:
            print("Please enter a valid numeric age.")

    while True:
        tag = input("Funding Tag (1-16 characters, letters, numbers, _, -): ").strip()
        if not is_valid_tag(tag):
            print(
                "Tag must be between 1 and 16 characters and can only contain letters, numbers, underscores, or hyphens.")
        else:
            break

    while True:
        idea = input("Idea (1-150 characters): ").strip()
        if not is_valid_idea(idea):
            print("Idea must be non-empty and no longer than 100 characters.")
        else:
            break

    while True:
        try:
            amount = int(input("Amount (positive integer): ").strip())
            if not is_valid_amount(amount):
                print("Amount must be a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid numeric amount.")

    print(submit_user_story(name, gender, age, tag, idea, amount))


if __name__ == "__main__":
    main()
