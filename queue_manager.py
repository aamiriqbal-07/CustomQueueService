import pickle
import os

class QueueManager:
    def __init__(self, state_file="queue_manager_state.pkl"):
        self.state_file = state_file
        self.queues = self.load_state()
        self.initialize_queues()

    def load_state(self):
        if not os.path.exists(self.state_file):
            return {}
        try:
            with open(self.state_file, 'rb') as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return {}

    def save_state(self):
        with open(self.state_file, 'wb') as f:
            pickle.dump(self.queues, f)

    def create_queue(self, queue_name):
        if queue_name not in self.queues:
            self.queues[queue_name] = queue_name
            self.save_state()
            print(f"Queue '{queue_name}' created.")
        else:
            print(f"Queue '{queue_name}' already exists.")

    def initialize_queues(self):
        initial_queues = ["example_queue", "another_queue"]
        for q in initial_queues:
            self.create_queue(q)

    def get_queue(self, queue_name):
        return self.queues.get(queue_name)

    def list_queues(self):
        return list(self.queues.keys())

    def delete_queue(self, queue_name):
        if queue_name in self.queues:
            del self.queues[queue_name]
            self.save_state()
            print(f"Queue '{queue_name}' deleted.")
        else:
            print(f"Queue '{queue_name}' does not exist.")
