from django.db import models
from datetime import date
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    last_name = models.CharField(max_length=50,blank=True,null=False)
    phone = models.CharField(max_length=12,blank=True,null=True)
    mobile = models.CharField(max_length=12,blank=False,null=False)
    email = models.EmailField(max_length=80)
    company = models.CharField(max_length=20,blank=False,null=False)
    date = models.DateField(default=date.today)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    

