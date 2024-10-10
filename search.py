import pymongo

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_story = db.user_story

# Creating a text index on multiple fields
user_story.create_index([('Name', 'text'), ('Tag', 'text'), ('Age', 'text'), ('Idea', 'text')])


def global_search(parameter):
    for record in user_story.find({'$text': {'$search': parameter}}, {'_id': 0}):
        print(record)


global_search()
