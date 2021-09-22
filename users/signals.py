from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


#@receiver(post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    print('profile signal Triggered')
    if created:
        user=instance
        profile=Profile.objects.create(user=user,username=user.username,email=user.email,name=user.first_name)

def profiledelete(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    print('deleting user')

post_save.connect(createProfile,sender=User)
post_delete.connect(profiledelete,sender=Profile)
