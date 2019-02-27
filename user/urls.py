from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.login, name='login'),
    re_path('login/$', views.login, name='login'),
    re_path('register/$', views.register, name='register'),
    re_path('index/$', views.index, name='index'),
    re_path('upload_file/$', views.upload_file, name='upload_file'),
    re_path('logout/$', views.logout, name='logout'),
    re_path('get_categories/$', views.get_categories, name='get_categories'),
    re_path('get_new_orders/$', views.get_new_orders, name='get_new_orders'),
    re_path('my_order/$', views.my_order, name='my_order'),
    re_path('delete_order/$', views.delete_order, name='delete_order'),
    re_path('edit_order_info/$', views.edit_order_info, name='edit_order_info'),
    re_path('edit_order/$', views.edit_order, name='edit_order'),
    re_path('get_orders/$', views.get_orders, name='get_orders'),
    re_path('receive_order/$', views.receive_order, name='receive_order'),
    re_path('programer_order/$', views.programer_order, name='programer_order'),
    re_path('achive_order/$', views.achive_order, name='achive_order'),

]
