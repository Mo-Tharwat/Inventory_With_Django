#Step 13; Add the following libraries:
from django.contrib.auth.models import User 
from .models import Profile
from django.db.models.signals import *
from django.dispatch import receiver

#Step 13; Create two methods for create or modify (for create user or modify data user)
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(staff=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()