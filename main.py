import praw
from DataSet import DataSet
from praw.models import Redditor
from praw.models import Comment


reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit("toundrabotplayground")

saved_data = DataSet("saved_info.txt")
for submission in subreddit.hot(limit=500):
    submission.comments.replace_more()
    comment: Comment = None
    for comment in submission.comments.list():
        if saved_data.is_in("id", comment.id) is None:
            print("new comment")
            if saved_data.is_in("body", comment.body) is not None:
                comment.reply("flagging for repost")
                print("flagging " + comment.id + " for repost")
                saved_data.add({"id": comment.id, "body": comment.body, "flagged": "t"})
            else:
                saved_data.add({"id": comment.id, "body": comment.body, "flagged": "f"})
        else:
            print("it's already there!")

