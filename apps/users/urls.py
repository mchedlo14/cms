from django.urls import path
from apps.users.views import (
    Oreon_UsersManagments,
    Oreon_SubscribersManagment,
    Customers,

)

app_name = 'users'

urlpatterns = [
    path('users',view =Oreon_UsersManagments,name="users"),
    path('subscribers', view=Oreon_SubscribersManagment, name="subscribers"),
    path('test/', view=Customers.as_view(), name="subs"),
]


