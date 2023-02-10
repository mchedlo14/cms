from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.groups.views import *

urlpatterns = [
    path('', GroupListView.as_view(), name="group-list"),
    path('edit/<int:id>', EditGroupView.as_view(), name="group-edit"),
    path('delete/<int:id>/', GroupDeleteView.as_view(), name="group-delete"),
    path('create/', GroupCreateView.as_view(), name="group-create"),

    path('permission/', PermissionListView.as_view(), name="permission-list"),
    path('permission/edit/<int:id>', EditPermissionView.as_view(), name="permission-edit"),
    path('permission/delete/<int:id>', PermissionDeleteView.as_view(), name="permission-delete"),
    path('permission/create/', PermissionCreateView.as_view(), name="permission-create"),

]
