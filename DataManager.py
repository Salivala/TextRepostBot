from DataSet import DataSet
from praw import models


class DataManager:
    def __init__(self, data: DataSet):
        self.data = data

    def is_in(self, comment_id: str) -> models.Comment or None:
        item: models.Comment = None
        for item in self.data.data:
            if comment_id is item["id"]:
                return item
            else:
                continue
        return item
