from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'date_updated')
    list_filter = ('author', 'date_posted', 'date_updated')
    search_fields = ('title', 'content')
    ordering = ('-date_posted',)

admin.site.register(Post, PostAdmin)