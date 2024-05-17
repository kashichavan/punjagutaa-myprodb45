from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName']

class ContactAdmin(admin.ModelAdmin):
    list_display=['city','phone','sid']


admin.site.register(StudentInfo,StudentAdmin)
admin.site.register(ContactInfo,ContactAdmin)