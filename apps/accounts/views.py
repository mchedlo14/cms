from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.forms import AccountAuthenticationForm, AccountRegistrationForm


class AccountRegistrationView(View):
    template_name = 'Oreon_Components/accounts/account_registration.html'

    def get(self, request):
        form = AccountRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = AccountRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('account:login')

        else:
            return render(request, self.template_name, {'form': form})


class AccountAuthenticationView(View):
    template_name = 'Oreon_Components/accounts/account_login.html'

    def get(self, request, *args, **kwargs):
        form = AccountAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = AccountAuthenticationForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('dashboards:dashboard')

        else:
            return render(request, self.template_name, {'form': form})


def accountProfileView(request):
    return render(request, 'Oreon_Components/accounts/account_profile.html')


def accountEditView(request):
    return render(request, 'Oreon_Components/accounts/account_edit.html')


class AccountLogoutView(View):
    template_name = 'Oreon_Components/accounts/account_logout.html'

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return render(request, self.template_name)
