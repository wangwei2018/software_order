from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # 显示的字段数
    list_display = ['id', 'username', 'role', 'email']

    # 过滤器 分类效果
    list_filter = ['username']

    # 添加用户时需要添加的字段
    fields = ['username', 'role', 'email']


class Soft_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'soft_name', 'user_id', 'programer_id', 'status']
    list_filter = ['user_id', 'programer_id', 'status']
    fields = ['soft_name', 'user_id', 'status']


class OrderNewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'count']
    list_filter = ['user_id']
    fields = ['user_id', 'count']


admin.site.register(User, UserAdmin)
admin.site.register(Soft_Category, Soft_CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_New, OrderNewAdmin)
