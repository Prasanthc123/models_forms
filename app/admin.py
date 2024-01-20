from django.contrib import admin

# Register your models here.
from app.models import *

class CustomizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['url']
    list_editable=['name']
    list_filter=['name']
    list_per_page=2
    search_fields=('name',)
admin.site.register(Topic)

admin.site.register(Webpage,CustomizeWebpage)

admin.site.register(Accessrecord)