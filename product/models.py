from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveSmallIntegerField(null=True)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
