from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MedicineRecord)
admin.site.register(MedicineName)
admin.site.register(MedicineType)