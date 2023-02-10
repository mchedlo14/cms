from django import forms
from django.forms import ModelForm,TextInput, EmailInput,FileInput,Select,Textarea,ImageField,ClearableFileInput
from apps.settings.models import Web_parametres



class WebparaForms(ModelForm):
    class Meta:
        model = Web_parametres
        fields = ['web_name','web_description','web_logo','web_number','web_email','web_info_adress','web_info_adress_city','web_currency']
        widgets = { 
            'web_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'web_description': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'აღწერა',
                'rows' : 5
                }),
            'web_logo': ClearableFileInput(attrs={
                'input id': 'file',
                'value':'file'
            }),
            'web_info_adress': TextInput(attrs={
                'class': "form-control", 
                }),
            'web_info_adress_city': TextInput(attrs={
                'class': "form-control", 
                }),
            'web_email': EmailInput(attrs={
                'class': "form-control", 
                }) ,
            'web_number': TextInput(attrs={
                'class': "form-control", 
                }) ,
            "web_currency" : Select(attrs={
                'class': "form-select",
                'select id': 'ForminputState',
                'data-choices data-choices-sorting':"true"
            }),
        }

