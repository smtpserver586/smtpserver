from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)
locked = True  # Initial state is locked
unlock_key = secrets.token_hex(8)  # Generate a random unlock key

def check_unlock_key(key):
    return key == unlock_key

@app.route('/get-key', methods=['GET'])
def get_key():
    return jsonify({"unlock_key": unlock_key})

@app.route('/get', methods=['GET'])
def get_key2():
    return jsonify({"unlock_key": "ssdd55ee"})

@app.route('/unlock/<key>', methods=['POST'])
def unlock():
    global locked
    data = request.json
    if key=='ssdd55ee':
        locked = False
        return jsonify({"message": "Unlocked successfully!"})
    else:
        return jsonify({"message": "Invalid key!"}), 403

@app.route('/locked-status', methods=['GET'])
def locked_status():
    return jsonify({"locked": locked})

if __name__ == '__main__':
    app.run(debug=True)
