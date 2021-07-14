from django.contrib import admin
from .models import Todolist, items
# Register your models here.
admin.site.register(Todolist)
admin.site.register(items)