from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile

class ProfileModelTests(TestCase):
    """Class to test the Profile model from accounts package """

    def test_profile_creation_with_user(self):
        new_user = User(username="test_user",password="test_user_password")
        new_user.save()
        new_profile = Profile.objects.get(user=new_user)
        self.assertEqual(new_profile.user, new_user)
