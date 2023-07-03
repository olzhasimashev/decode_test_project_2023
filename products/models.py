from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    color = models.CharField(max_length=35, blank=True, default='white')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт' 
        verbose_name_plural = 'Продукта'