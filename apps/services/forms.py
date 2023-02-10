from django import forms
from django.forms import TextInput, Textarea, Select, ClearableFileInput
from mptt.exceptions import InvalidMove

from apps.services.models import Service, Category


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'service_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'სახელი',
                'style': "margin-bottom:20px;"
            }),
            'slug': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ლინკის სახელი',
                'style': "margin-bottom:20px;"
            }),
            'service_description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'აღწერა',
                'rows': 5,
                'style': "margin-bottom:20px;"
            }),
            'service_price': TextInput(attrs={
                'class': "form-control",
                'placeholder': "ფასი",
                'style': "margin-bottom:20px;"

            }),
            'sale_percentage': TextInput(attrs={
                'class': "form-control",
                'placeholder': "ფასდაკლება",
                'style': "margin-bottom:20px;"
            }),
            'sale_price': TextInput(attrs={
                'class': "form-control",
                'placeholder': "ფასდაკლება",
                'style': "visibility:hidden;"
            }),
            'service_image': ClearableFileInput(attrs={
                'class': "form-control",
                'style': "display: flex;"
            }),
            "category": Select(attrs={
                'class': "form-control",
                'style': "margin-left:0px;margin-bottom:20px"
            })
        }

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['service_name'].label = "სერვისის სახელი"
        self.fields['slug'].label = "სერვისის ლინკის სახელი"
        self.fields['service_description'].label = "სერვისის აღწერა"
        self.fields['service_price'].label = "სერვისის ფასი"
        self.fields['sale_percentage'].label = "სერვისის ფასდაკლება"
        self.fields['sale_price'].label = ""
        self.fields['category'].label = "კატეგორიები"
        self.fields['service_image'].label = "სურათი"
        # self.fields['service_category'].label = "სერვისის კატეგორია"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent', 'category_images']

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'სახელი',
                'style': "margin-bottom:30px;"
            }),
            'slug': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ლინკის სახელი',
                'style': "margin-bottom:30px;"
            }),
            'parent': Select(attrs={
                'class': "form-control",
                'placeholder': 'აღწერა',
                'style': "margin-bottom:30px;"
            }),
            'category_images': ClearableFileInput(attrs={
                'multiple': True,
                'class': "form-control",
            }),
        }

    def clean(self):
        parent_category = self.cleaned_data['parent']
        if parent_category:
            if InvalidMove:
                raise forms.ValidationError("A node may not be made a child of any of its descendants.")
