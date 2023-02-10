from django import forms
from mptt.exceptions import InvalidMove

from apps.products.models import Product, Category

from django.forms import TextInput, Textarea, Select, ClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image','product_name', 'slug', 'product_description', 'quantity', 'product_price',
                  'sale_percentage','category']
        widgets = {
            'product_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'სახელი',
                'style': "margin-bottom:20px;"
            }),
            'slug': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ლინკის სახელი',
                'style': "margin-bottom:20px;"
            }),
            'product_description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'აღწერა',
                'rows': 5,
                'style': "margin-bottom:20px;"
            }),
            'image': ClearableFileInput(attrs={
                'multiple': True,
                'class': "form-control",
            }),
            'quantity': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ოდენობა',
                'rows': 5,
                'style': "margin-bottom:20px;"
            }),
            'product_price': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'პროდუქტის ფასი',
                'rows': 5,
                'style': "margin-bottom:20px;"
            }),
            'sale_percentage': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ფასდაკლება',
                'rows': 5,
                'style': "margin-bottom:20px;"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()


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

    # def clean(self):
    #     parent_category = self.cleaned_data['parent']
    #     if parent_category:
    #         if InvalidMove:
    #             raise forms.ValidationError("A node may not be made a child of any of its descendants.")
