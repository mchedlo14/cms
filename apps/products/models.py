from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    product_description = models.TextField(max_length=512)
    image = models.ImageField(upload_to='product_images/')
    quantity = models.DecimalField(max_digits=3, decimal_places=0, blank=True)
    product_price = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    sale_percentage = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=0)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    category = TreeForeignKey(
        'Category',
        related_name="products",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if self.sale_percentage > 0:
            self.sale_price = self.product_price - (self.product_price * (self.sale_percentage / 100))
        else:
            self.sale_price = None
        super(Product, self).save(*args, **kwargs)


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
