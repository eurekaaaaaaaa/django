from django.contrib import admin

from . import models
admin.site.register(models.Student)
admin.site.register(models.Homework)
# Register your models here.
