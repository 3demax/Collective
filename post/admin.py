from django.contrib import admin
from post.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'publish_date')
    list_filter = ('is_published', 'publish_date')
    search_fields = ['title', 'text', 'publish_date']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['name',]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
