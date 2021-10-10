from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import student
from import_export.admin import ImportExportModelAdmin

@admin.register(student)
class userdat(ImportExportModelAdmin):
    pass