from django.db import models

# Create your models here.
class Item(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.FloatField()

class Bill(models.Model):
    item_code = models.ForeignKey(Item)
    bill_comment = models.CharField(max_length=80)
    number = models.IntegerField()