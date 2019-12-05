from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """ A model to implement the posts in the site

        Attributes
        title -- is what is displayed in the top of the post
        content -- is going to be an image of a dog (preferably)
        votes -- are a way of sorting posts by popularity
        post_owner -- is the one who uploaded the post
    """
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
        """ Edit the votes +1 and save to the database """
        self.votes = self.votes + 1
        self.save()

    def downvotePost(self):
        """ Edit the votes -1 and save to the database """
        if self.votes > 0:
            self.votes = self.votes - 1
        self.save()

class Comment(models.Model):
    """ A model to implement the comments to posts in the site

        Attributes
        content -- the only thing the user inputs, a text related to a post
    """
    content = models.TextField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
