from flask import Flask, request
app = Flask(__name__)

data_from_post = {}

@app.route('/<id>', methods=['GET'])
def get_id(id):
    posted_id = data_from_post.get("id")
    if str(posted_id) == str(id):
        return "ID is stored."
    else:
        return "ID not stored."

@app.route('/', methods=['POST'])
def post_id():
    global data_from_post
    data_from_post = request.json
    return "Set the payload."