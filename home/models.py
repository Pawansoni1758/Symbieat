from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('BR', 'Burger'),
    ('MG', 'Maggie'),
    ('PST', 'Pasta'),
    ('BVG', 'Beverages'),
    ('SDH', 'Sandwitch')
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    Product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title