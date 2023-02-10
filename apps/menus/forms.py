from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput

from apps.menus.models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'menu_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'სახელი',
                'style': "margin-bottom:20px;"
            }),
            'slug': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ლინკის სახელი',
                'style': "margin-bottom:20px;"
            }),
            'menu_description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'აღწერა',
                'rows': 5,
                'style': "margin-bottom:20px;"
            }),
            'menu_image': ClearableFileInput(attrs={
                'class': "form-control",
            })
        }

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['menu_name'].label = "მენიუს სახელი"
        self.fields['slug'].label = "მენიუს ლინკის სახელი"
        self.fields['menu_description'].label = "მენიუს აღწერა"
        # self.fields['menu_category'].label = "მენიუს აღწერა"
