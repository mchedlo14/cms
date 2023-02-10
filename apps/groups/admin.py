from django.contrib import admin

from apps.groups.models import Group, GroupPermission

admin.site.register(Group)
admin.site.register(GroupPermission)
