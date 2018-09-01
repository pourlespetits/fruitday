from django.contrib import admin
from .models import *
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    """docstring for Users"""
    list_display = ['uname', 'uphone', 'uemail']
    fields = ['uname', 'uphone', 'uemail', 'hasbuy']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'spec', 'picture']
    list_editable = ['price']


class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['tname', 'gpicture', 'tdesc']


admin.site.register(Users, UsersAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
