from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    content = models.ImageField(
        upload_to='images/',
        default='images/404image.jpg'
        )
    post_owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def upvotePost(self):
        self.votes = self.votes + 1
        self.save()

    def downvotePost(self):
        if self.votes > 0:
            self.votes = self.votes - 1
        self.save()

class Comment(models.Model):
    content = models.TextField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
