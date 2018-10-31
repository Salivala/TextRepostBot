import os
import json


class DataSet:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = []

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

    def write(self):
        with open(self.file_name, "w") as f:
            f.write(json.dumps(self.data, sort_keys=True, indent=4))
