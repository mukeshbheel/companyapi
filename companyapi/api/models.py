from django.db import models

# Create your models here.

#Creating company model
class company(models.Model):
    comapny_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobile Phones')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    about=models.TextField()
    position=models.CharField(max_length=50, choices=(
        ('Manager', 'manager'),
        ('Software Developer','SD'),
        ('Project Coordinator','PC')
    ))
    
    company=models.ForeignKey(company, on_delete=models.CASCADE)
    
