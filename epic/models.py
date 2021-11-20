from django.db import models


# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    Image = models.ImageField(upload_to='images/',default="")
    def __str__(self):
        return self.productname

