from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    """ A model to represent a user by its profile

        Atributes:
        user -- one to one relationship with the owner of the profile
        nickname -- a random name that will identify the user to other users
        photo, description -- ways of characterizing a user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(
            upload_to= "images/",
            null = True,
            blank = True,)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """ Creates a profile for every user created """
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """ Saves the profile in the database when a user is created """
        instance.profile.save()

    def get_absolute_url(self):
        """ Return to home when any update or creation is made """
        return reverse('apps:home')
