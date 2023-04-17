from django.db import models

# Create your models here.

class Employee(models.Model):
    emps=models.CharField(max_length=12)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name