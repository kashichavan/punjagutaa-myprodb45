from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName','age']


class BookAdmin(admin.ModelAdmin):
    list_display=['bookName']

admin.site.register(Author,AuthorAdmin)

admin.site.register(Book,BookAdmin)
