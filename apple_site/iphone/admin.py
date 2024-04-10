from django.contrib import admin
from .models import Iphone, Description



@admin.register(Iphone)
class IphoneAdmin(admin.ModelAdmin):
    fields = ['name', 'memory', 'color', 'price', 'image', 'slug', 'vid', 'promo']
    list_display = ['name', 'price', 'vid']
    list_display_links = ['name']
    search_fields = ['name__startswith', 'vid__name']
    list_filter = ['vid__name']

@admin.register(Description)
class Description(admin.ModelAdmin):
    fields = ['model', 'img_1', 'img_2']




