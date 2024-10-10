import pymongo

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_story = db.user_story


def fetch_top_stories():
    return user_story.aggregate([
        {'$sort': {'Balance_amount': 1}},
        {'$limit': 5},
        {'$project': {'_id': 0, 'Upload_date': 0}}
    ])


def display_stories(stories):
    if stories:
        for story in stories:
            print(f"Name: {story.get('Name', 'No Name')}")
            print(f"Age: {story.get('Age', 'N/A')}")
            print(f"Tag: {story.get('Tag', 'N/A')}")
            print(f"Idea: {story.get('Idea', 'N/A')}")
            print(f"Amount: {story.get('Amount', 'N/A')}")
            print(f"Balance Amount: {story.get('Balance_amount', 'N/A')}")
            print("-" * 50)  # Add ending to separate stories
    else:
        print("No user stories found.")


def main():
    stories = list(fetch_top_stories())
    display_stories(stories)


if __name__ == "__main__":
    main()
