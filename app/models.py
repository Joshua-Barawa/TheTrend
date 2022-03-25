
from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='media/default2.png', upload_to='media/', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Post(models.Model):
    content = models.TextField()
    comments = models.IntegerField(default=0)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    posted_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.user.username)


class Comment(models.Model):
    reply = models.TextField()
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Project(models.Model):
    name = models.CharField(max_length=200)
    project_pic = models.ImageField(blank=True, upload_to='media/', null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    link = models.URLField( blank=True, null=True)

    def __str__(self):
        return str(self.name)
