from django.db import models

from accounts.models import User


class Story(models.Model):
    title = models.CharField(max_length=99)
    url = models.URLField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    story = models.ForeignKey(Story, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
