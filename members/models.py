

from typing import Any, Iterable
from django.db import models
from django.db.models.query import QuerySet

# Create your models here.  
class MemberTable(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField(null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  
  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.age} {self.phone}"



 