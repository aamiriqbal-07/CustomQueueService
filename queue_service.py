from flask import Flask, request, jsonify
from queue_manager import QueueManager
from message_queue import MessageQueue
import json

app = Flask(__name__)
queue_manager = QueueManager()


@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    topic = data.get('topic')
    content = data.get('content')

    if not topic or not content:
        return jsonify({"error": "Invalid request. 'topic' and 'content' are required."}), 400

    if topic not in queue_manager.list_queues():
        return jsonify({"error": f"Queue '{topic}' not found."}), 404

    message_queue = MessageQueue(topic)
    message_queue.publish_message(json.dumps(content))
    return jsonify({"message": f"Message published to queue: {topic}"}), 200


@app.route('/consume', methods=['GET'])
def consume():
    topic = request.args.get('topic')

    if not topic:
        return jsonify({"error": "Invalid request. 'topic' is required."}), 400

    if topic not in queue_manager.list_queues():
        return jsonify({"error": f"Queue '{topic}' not found."}), 404

    message_queue = MessageQueue(topic)
    message = message_queue.consume_message()

    if message:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"message": "No messages available."}), 204


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
