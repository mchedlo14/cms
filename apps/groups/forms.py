from django import forms
from django.forms import TextInput, Textarea, Select, ClearableFileInput, SelectMultiple
from mptt.exceptions import InvalidMove

from apps.groups.models import Group, GroupPermission


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'group_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ჯგუფის სახელი',
                'style': "margin-bottom:20px;"
            }),
            'user_related_group ': SelectMultiple(attrs={
                'class': "form-control",
            }),
        }

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['group_name'].label = "ჯგუფის სახელი"
        self.fields['user_related_group'].label = "მომხმარებლის ამორჩევა"


class GroupPermissionForm(forms.ModelForm):
    class Meta:
        model = GroupPermission
        fields = "__all__"

        widgets = {
            'permission_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'უფლების სახელი',
                'style': "margin-bottom:30px;"
            }),
            'permission_group': SelectMultiple(attrs={
                'class': "form-control",

            }),
        }

    def __init__(self, *args, **kwargs):
        super(GroupPermissionForm, self).__init__(*args, **kwargs)
        self.fields['permission_name'].label = "უფლების სახელი"
        self.fields['permission_group'].label = "უფლების მინიჭება"
