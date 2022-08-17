from django.db import models

# Create your models here.

class Stores(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"Store: {self.name}"

class Delivers(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"Deliver: {self.name}"

class StoreModel(models.Model):
    store_name = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)

    deliver = models.CharField(max_length=256)
    del_quantity = models.IntegerField()
    del_price = models.DecimalField(max_digits=10, decimal_places=3)
    del_currency = models.CharField(max_length=50)

    remained = models.IntegerField()
    percent = models.DecimalField(max_digits=10, decimal_places=3)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Store: {self.store_name}; Product: {self.product_name}"

class InventoryModel(models.Model):
    product_name = models.CharField(max_length=256)

    deliver = models.CharField(max_length=256)
    del_quantity = models.IntegerField()
    del_price = models.DecimalField(max_digits=10, decimal_places=3)
    del_currency = models.CharField(max_length=50)

    remained = models.IntegerField()
    percent = models.DecimalField(max_digits=10, decimal_places=3)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventory: {self.product_name}"
    
class ActionModel(models.Model):
    store_name = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    quantity = models.IntegerField()
    del_currency = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From inventory -> to {self.to}"


