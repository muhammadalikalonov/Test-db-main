from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products')
    material = models.ForeignKey(Material,on_delete=models.CASCADE,related_name='materials')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name}ga {self.material.name} dan {self.quantity} kerak"


class Warehouses(models.Model):
    material = models.ForeignKey(Material,on_delete=models.CASCADE,related_name='materials_ware')
    reminder = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.material.name
