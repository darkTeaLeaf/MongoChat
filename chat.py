#!flask/bin/python
from flask import Flask, jsonify, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo0.example.com:27017,mongo1.example.com:27018,mongo2.example.com:27019$db = client.mymongodb  # Select the database
messages_collection = db.message  # Select the collection name
initial_messages = [message for message in messages_collection.find()]

if (len(initial_messages)) == 0:
    messages_collection.insert({
        'title': 'Hello'
    })
    messages_collection.insert({
        'title': 'How are you doing?'
    })

# home page - list of messages
@app.route('/', methods=['GET'])
def get_messages():
    all_messages = messages_collection.find()
    messages_list = []
    for message in all_messages:
        messages_list.append({'title': message['title']})

    return jsonify({'messages': messages_list})

# send a message to chat via URL address
@app.route('/send/<string:message>', methods=['GET'])
def create_message(message):
    new_message = {"title": message}
    messages_collection.insert(new_message)
    return redirect('/')


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'This is a Test'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
