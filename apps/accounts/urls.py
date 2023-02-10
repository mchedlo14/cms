from django.urls import path
from django.contrib.auth.decorators import login_required as l

from apps.accounts.views import (AccountRegistrationView,
                                 AccountAuthenticationView,
                                 accountProfileView,
                                 accountEditView,
                                 AccountLogoutView)


app_name = 'account'

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountAuthenticationView.as_view(), name='login'),
    path('profile/', accountProfileView, name='profile'),
    path('profile/edit', accountEditView, name='profile-edit'),
    path('logout/', l(AccountLogoutView.as_view(), redirect_field_name=''), name='logout'),

]
