import praw
import json
from DataSet import DataSet


reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit("toundrabotplayground")

saved_data = DataSet("saved_info.txt")
saved_data.populate()

for submission in subreddit.hot(limit=500):
    submission.comments.replace_more()
    for comment in submission.comments.list():
        matches = [item for item in saved_data.data if item['id'] == comment.id]
        item = {"id": comment.id, "body": comment.body, "flagged": 'f'}
        if item not in matches:
            saved_data.add(item)
        for item in saved_data.data:
            if comment.id == item['id'] and item['flagged'] == 'f':
                comment.reply("This is a repost of another comment on this sub")
                saved_data.add({"id": comment.id, "body": comment.body, "flagged": "t"})
            else:
                saved_data.add({"id": comment.id, "body": comment.body, "flagged": "f"})
