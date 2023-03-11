from django.db import models
from datetime import date
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100,blank=False,null=False),
    description = models.TextField(blank=True,null=True),
    date = models.DateField(date.today),
    estimated_end = models.DateField(blank=True,null=True),
    priority = models.IntegerField(default=2),

    def __str__(self):
        return self.title
    

