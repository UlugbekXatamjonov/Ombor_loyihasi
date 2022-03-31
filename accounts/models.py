from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

# Create your models here.

class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='Profile_pic/%Y/%m/%d/', verbose_name='Admin rasmi', null=True, blank=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False,  null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

    def avatar(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.photo) ) # default='<img src="/media/default_pictures/"'

    avatar.short_description = 'Admin rasmi'
