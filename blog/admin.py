from django.contrib import admin
from blog.models import Posts, PostImages

class ImageInline(admin.TabularInline):
    model = PostImages

class PostsAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Posts, PostsAdmin)