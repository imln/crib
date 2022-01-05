from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

