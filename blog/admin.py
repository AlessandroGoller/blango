# Register your models here.

from django.contrib import admin
from .models import Tag, Post

admin.site.register(Tag)
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}