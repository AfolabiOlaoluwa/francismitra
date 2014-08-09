from django.contrib import admin
from blog.models import Posts, PostImages

admin.site.register([Posts, PostImages])