from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    
    def __str__(self):
        return self.name    

class CustomUser(AbstractUser):
    GENDER = (('male','MALE'), ('female', 'FEMALE'))
    ROLL = (('HR','HR'),('Branch Manager','Branch Manager'),('Employee','Employee'),('Department Manager','Department Manager'))

    active = models.CharField(max_length=10,null=False,blank=False,choices=[('Active','Active'),('Inactive','Inactive')],default='Active')
    roll = models.CharField(max_length=30,null=False,blank=False,choices=ROLL,default='HR')
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',default="50000")
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    mobile = models.CharField(max_length=15)
    thumb = models.ImageField(blank=True,null=True)
    

    def __str__(self):
        return self.username



