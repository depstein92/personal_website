from django.contrib import admin

# Register your models here to django admin
from .models import Job, Blog

admin.site.register(Job)
admin.site.register(Blog)
