from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    #will have an image here

    def upvotePost(self):
        self.votes = self.votes + 1
        self.save()

    def downvotePost(self):
        if self.votes > 0:
            self.votes = self.votes - 1
        self.save()
