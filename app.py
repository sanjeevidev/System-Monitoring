from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print("Client connected")

def send_system_data():
    # Example real-time update function
    data = {
        'gpu_usage': '75%',
        'memory_usage': '14GB',
        'storage_io': '600MB/s',
        'training_progress': 'Epoch 20/100'
    }
    socketio.emit('system_data', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
