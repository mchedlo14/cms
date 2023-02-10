from django.db import models
from ckeditor.fields import RichTextField


class Menu(models.Model):
    menu_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    menu_description = RichTextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menu_image = models.ImageField(upload_to="menu_images/", default="default.jpg")

    # menu_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.menu_name
