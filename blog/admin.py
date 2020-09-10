from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish_time',
        'update_time',
    ]
admin.site.register(Post, PostAdmin)


