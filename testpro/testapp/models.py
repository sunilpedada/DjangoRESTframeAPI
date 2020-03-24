from django.db import models

# Create your models here.
class EmployeDetails(models.Model):
    ename=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    esalary=models.IntegerField()
    
