from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=99)
    url = models.URLField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
