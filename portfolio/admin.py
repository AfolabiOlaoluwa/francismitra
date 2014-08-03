from django.contrib import admin
from portfolio.models import Categories, Images, Videos

admin.site.register([Categories, Images, Videos])
