from django.contrib import admin

# Register your models here.
from project_app import models

admin.site.register(models.Todo)