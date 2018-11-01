import os
import json
from praw import models


class DataSet:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = []
        self.populate()

    def populate(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, "r") as f:
                file_data = f.read()
            if "[" not in file_data:
                self.write()
            else:
                self.data = json.loads(file_data)
        else:
            self.write()

    def add(self, item: dict):
        self.data.append(item)
        self.write()

    def is_in(self, comment_key: str, comment_value: str) -> models.Comment or None:
        for item in self.data:
            if comment_value == item[comment_key]:
                return item
        return None

    def write(self):
        with open(self.file_name, "w") as f:
            f.write(json.dumps(self.data, sort_keys=True, indent=4))
