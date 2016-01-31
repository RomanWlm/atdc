from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')

class Product(models.Model):
    label = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        blank=True,
        null=True, )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.CharField(max_length=1500)
