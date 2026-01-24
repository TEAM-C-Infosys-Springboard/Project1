import json
import os


class PersistenceManager:
    def __init__(self, file_path="data/store.json"):
        self.file_path = file_path

        # Create data folder if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save(self, data: dict):
        """Save key-value data to file"""
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def load(self):
        """Load key-value data from file"""
        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, "r") as file:
            return json.load(file)
