from django.db import models


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField()
    phone=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name
    