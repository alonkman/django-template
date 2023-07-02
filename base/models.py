from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exmpale (models.Model):
    exmaple_field = models.CharField(max_length=50,null=True,blank=True)
#     exmaple_field(number) = models.DecimalField(max_digits=5,decimal_places=2)
#     exmaple_field(number) = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

 
    def __str__(self):
           return self.desc
    
