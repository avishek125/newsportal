from django.contrib import admin
from news.models import News, Category


admin.site.register(Category)
admin.site.register(News)
