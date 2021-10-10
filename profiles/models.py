from django.core.checks import messages
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.contrib.auth.models import User
from datetime import date
import random
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
       
        if not self.slug:
            self.slug = slugify(self.user.username)
        
        super(Profile, self).save(*args, **kwargs)

def save_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user)


post_save.connect(save_profile, sender=User)


def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_delete.connect(delete_profile, sender=Profile)
