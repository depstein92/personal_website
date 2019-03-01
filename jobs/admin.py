from django.contrib import admin

# Register your models here to django admin
from .models import Job, Blog, Education, Experience

admin.site.register(Job)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Experience)
