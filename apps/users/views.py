from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.auth_backends import get_user_model


class Oreon_UsersManagment(LoginRequiredMixin, TemplateView):
    pass


Oreon_UsersManagments = Oreon_UsersManagment.as_view(template_name="Oreon_Components/users/users.html")
Oreon_SubscribersManagment = Oreon_UsersManagment.as_view(template_name="Oreon_Components/users/subscribers.html")


class Customers(View):
    def get(self, request, *args, **kwargs):
        all_customers = get_user_model
        print(all_customers)
        context = {
            "all_customers": all_customers,
        }
        return render(request, 'Oreon_Components/users/subscribers.html', context)
