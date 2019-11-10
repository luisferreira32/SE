from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    content = models.ImageField(
        upload_to='images/',
        default='images/404image.jpg'
        )

    def upvotePost(self):
        self.votes = self.votes + 1
        self.save()

    def downvotePost(self):
        if self.votes > 0:
            self.votes = self.votes - 1
        self.save()
