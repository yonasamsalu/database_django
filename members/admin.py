

from django.contrib import admin
from .models import MemberTable


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname",'age','phone','joined_date')
  
admin.site.register(MemberTable, MemberAdmin )