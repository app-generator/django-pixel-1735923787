# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    id = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    approved = models.BooleanField()
    password = models.BooleanField()
    birthday = models.DateTimeField(blank=True, null=True, default=timezone.now)
    points = models.IntegerField(null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Student(models.Model):

    #__Student_FIELDS__
    email = models.TextField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    house = models.TextField(max_length=255, null=True, blank=True)
    homeroom = models.TextField(max_length=255, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)

    #__Student_FIELDS__END

    class Meta:
        verbose_name        = _("Student")
        verbose_name_plural = _("Student")



#__MODELS__END
