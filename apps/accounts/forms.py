from django import forms
from django.contrib.auth import authenticate

from apps.accounts.models import CustomAccount


class AccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control mb-2 position-relative',
                                                                 'placeholder': 'პაროლი', 'id': 'password'}),
                               required=True)
    password_confirm = forms.CharField(label='Password confirmation',
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control mb-2 position-relative',
                                                  'placeholder': 'გაიმეორეთ პაროლი', 'id': 'password confirm'}),
                                       required=True)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'მეილი', 'id': 'email'}))
    first_name = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'სახელი', 'id': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'გვარი', 'id': 'Last Name'}))

    class Meta:
        model = CustomAccount
        fields = ('email', 'first_name', 'last_name')

    def clean(self):
        taken_email = CustomAccount.objects.filter(email=self.cleaned_data['email']).exists()
        # Check that the two password entries match
        if self.is_valid():
            password = self.cleaned_data["password"]
            password_confirm = self.cleaned_data["password_confirm"]
            if password != password_confirm:
                self.add_error('password', "Passwords don't match")
            # Check That Email Exists Or Not
            if taken_email:
                self.add_error('email', 'This Email Is Already Taken')
            # Check that Username has valid characters

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control mb-2 position-relative',
                                                                 'placeholder': 'პაროლი', 'id': 'password'}),
                               required=True)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'მეილი', 'id': 'email'}))

    class Meta:
        model = CustomAccount
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            taken_email = CustomAccount.objects.filter(email=email).exists()
            if not taken_email:
                if not authenticate(email=email):
                    self.add_error('email', "Email Is Not Registered")
            if taken_email:
                if not authenticate(email=email, password=password):
                    self.add_error('password', "password is incorrect")
