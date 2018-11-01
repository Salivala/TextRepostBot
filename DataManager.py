from DataSet import DataSet
from praw import models


class DataManager:
    def __init__(self, data: DataSet):
        self.data = data

    def is_in(self, comment_key: str, comment_value: str) -> models.Comment or None:
        for item in self.data.data:
            if comment_value == item[comment_key]:
                return item
        return None
