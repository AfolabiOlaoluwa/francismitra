from django.contrib import admin
from django.contrib.contenttypes import generic
from blog.models import Posts, PostImages

class ImageInline(admin.TabularInline):
	model = PostImages

class PostsAdmin(admin.ModelAdmin):
	inlines = [ImageInline]


admin.site.register(Posts, PostsAdmin)