import pymongo

client = pymongo.MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority')
db = client['Crowd']
user_story = db.user_story


def sort_by_balance_amount_lth():
    records = user_story.aggregate([
        {'$project': {'_id': 0}},
        {'$sort': {'Balance_amount': 1}}
    ])
    for record in records:
        print(record)


def sort_by_balance_amount_htl():
    records = user_story.aggregate([
        {'$project': {'_id': 0}},
        {'$sort': {'Balance_amount': -1}}
    ])
    for record in records:
        print(record)


def sort_by_amount_lth():
    records = user_story.aggregate([
        {'$project': {'_id': 0}},
        {'$sort': {'Amount': 1}}
    ])
    for record in records:
        print(record)


def sort_by_amount_htl():
    records = user_story.aggregate([
        {'$project': {'_id': 0}},
        {'$sort': {'Amount': -1}}
    ])
    for record in records:
        print(record)


sort_by_balance_amount_htl()
