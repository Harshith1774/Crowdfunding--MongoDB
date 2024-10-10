import pymongo

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_story = db.user_story


def fetch_all_stories():
    return list(user_story.find({}, {'_id': 0}).sort('Upload_date', -1))


def main():
    stories = fetch_all_stories()
    if stories:
        for story in stories:
            print(f"Name: {story.get('Name', 'N/A')}")
            print(f"Age: {story.get('Age', 'N/A')}")
            print(f"Tag: {story.get('Tag', 'N/A')}")
            print(f"Idea: {story.get('Idea', 'N/A')}")
            print(f"Amount: {story.get('Amount', 'N/A')}")
            print(f"Balance Amount: {story.get('Balance_amount', 'N/A')}")
            print(f"Upload Date: {story.get('Upload_date', 'N/A')}")
            print("=" * 40)
    else:
        print("No user stories found.")


if __name__ == "__main__":
    main()
