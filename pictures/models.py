from django.db import models

# Create your models here.


class Hall(models.Model):
    name = models.CharField(max_length=100)
    square = models.DecimalField(max_digits=19, decimal_places=2)
    windows_number = models.IntegerField()


class Picture(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    price = models.IntegerField()
    price_for_which_was_purchased = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)

