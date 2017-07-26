from __future__ import unicode_literals

from django.db import models

from ..first_app.models import User
# Create your models here.
class FriendManager(models.Manager):
    def MakeFriend(self, postData):
        friend = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'])
        return friend


class Friend(models.Model):
    first_name = models.CharField(max_length = 100, null = True)
    last_name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, null = True, default = 1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = FriendManager()
