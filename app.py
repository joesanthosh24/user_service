# user_service.py

from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

users = {
    '1': {'name': 'Alice', 'email': 'alice@example.com'},
    '2': {'name': 'Bob', 'email': 'bob@example.com'}
}

@app.route('/user/<id>')
def user(id):
    print(id)
    user_info = users.get(id, {})
    print(user_info)
    return jsonify(user_info)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    new_user_id = str(uuid.uuid1())

    users[new_user_id] = { 'name': name, 'email': email }

    return jsonify({
        'new_user': users[new_user_id],
        'all_users': users
    })

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user_ids = list(users.keys())

    if id in user_ids:
        data = request.json
        email = users[id]['email']
        name = users[id]['name']
        if data.get('email'):
            email = data.get('email')
        if data.get('name'):
            name = data.get('name')

        users[id] = { email: email, name: name }

        return jsonify({
            'updated_user': users[id],
            'all_users': users
        })
    
    return jsonify('User with this id does not exist')

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user_ids = list(users.keys())

    if id in user_ids:
        user_to_delete = users[id]
        users.pop(id)

        return jsonify({
            'deleted_user': user_to_delete,
            'all_users': users
        })
    
    return jsonify({'User with this id does not exist'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
