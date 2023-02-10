from django.db import models
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


class Service(models.Model):
    service_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    service_description = RichTextField(max_length=512)
    service_price = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    sale_percentage = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=0)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    category = TreeForeignKey(
        'Category',
        related_name="services",
        on_delete=models.CASCADE
    )
    service_image = models.ImageField(upload_to="service_images/", default="default.jpg")

    # service_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        if self.sale_percentage > 0:
            self.sale_price = self.service_price - (self.service_price * (self.sale_percentage / 100))
        else:
            self.sale_price = None
        super(Service, self).save(*args, **kwargs)


class Category(MPTTModel):
    name = models.CharField(max_length=200)  # noqa
    slug = models.SlugField(unique=True)
    category_images = models.ImageField(upload_to='category_images/')
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
