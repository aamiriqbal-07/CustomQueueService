import json
import os


class MessageQueue:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.queue_path = f"{self.queue_name}.json"
        self.queue = self.load_queue()

    def load_queue(self):
        try:
            with open(self.queue_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_queue(self):
        with open(self.queue_path, 'w') as f:
            json.dump(self.queue, f)

    def publish_message(self, message):
        self.queue.append(message)
        self.save_queue()

    def consume_message(self):
        if self.queue:
            message = self.queue.pop(0)
            self.save_queue()
            return message
        return None

    def refresh_queue(self):
        self.queue = self.load_queue()
