from django.test import TestCase
from .models import Post

class PostModelTests(TestCase):
    """Class to test the Post model from apps package"""

    def test_downvotePost_with_negative_votes(self):
        """ downvotePost will not downvote below zero votes """
        unvoted_post = Post(title="testcase", votes=0)
        unvoted_post.downvotePost()
        self.assertIs(unvoted_post.votes, 0)
        
