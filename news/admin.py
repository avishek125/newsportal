from django.contrib import admin
from news.models import News, Category, ContactUs, Subscribe

"""
this lines of codes are used to register class model into admin pannel
"""
admin.site.register(Category)
admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Subscribe)