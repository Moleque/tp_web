from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    rating = models.IntegerField()


class Question(models.Model):
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Answer(models.Model):
    author = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    right_flag = models.BooleanField(default=True)
    text = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    question = models.ManyToManyField(Question)
    word = models.CharField(max_length=25)


class Like(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(Profile)
    value = models.BooleanField()

