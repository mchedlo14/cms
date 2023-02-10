from django.db import models
from django.contrib.auth.models import Permission, ContentType
from apps.accounts.models import CustomAccount


class Group(models.Model):
    group_name = models.CharField(max_length=200, blank=False)
    user_related_group = models.ManyToManyField(CustomAccount)

    def __str__(self):
        return self.group_name


class GroupPermission(models.Model):
    permission_name = models.CharField(max_length=200)
    permission_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.permission_name
