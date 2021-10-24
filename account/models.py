from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import now

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(blank=True, null=True, max_length=155)
    no_hp = models.CharField(blank=True, null=True, max_length=13)
    is_performer = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    joined = models.DateTimeField(default=now, editable=False)
    group_name = models.CharField(blank=True, null=True, max_length=155)
    group_description = models.CharField(blank=True, null=True, max_length=255)
    group_category = models.CharField(blank=True, null=True, max_length=155)
    profile_picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)