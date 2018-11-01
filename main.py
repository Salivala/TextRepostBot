import praw
from DataSet import DataSet
from praw.models import Comment
from praw.models import Redditor


reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit("toundrabotplayground")

saved_data = DataSet("saved_info.txt")
while True:
    for submission in subreddit.hot(limit=100):
        submission.comments.replace_more()
        comment: Comment = None
        for comment in submission.comments.list():
            author_name = comment.author.name
            if saved_data.is_in("id", comment.id) is None:
                print("new comment")
                if saved_data.is_in("body", comment.body) is not None and author_name != 'RepostDeputy':
                    author: Redditor = comment.author
                    print("messaging " + author.name + " about post deletion")
                    author.message(subject="Post removed", message="Your post " + comment.body + " is a repost")
                    saved_data.add({"id": comment.id, "body": comment.body, "flagged": "t"})
                    comment.mod.remove()
                else:
                    saved_data.add({"id": comment.id, "body": comment.body, "flagged": "f"})
            else:
                print("l")

