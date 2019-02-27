from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=10, verbose_name="角色")

    class Meta:
        db_table = "user"


class Soft_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="类别名称")

    class Meta:
        db_table = 'soft_category'

    def __str__(self):
        return self.name


class Order(models.Model):
    '''
    订单
    '''
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=0,verbose_name="订单状态")
    category_id = models.ForeignKey(Soft_Category, on_delete=models.CASCADE, related_name="orders", verbose_name="类别id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="用户")
    programer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="has_orders",
                                     verbose_name="程序员")
    soft_name = models.CharField(max_length=50, verbose_name="软件名称")
    desc = models.CharField(max_length=100, verbose_name="订单描述")

    package_url = models.CharField(max_length=150, verbose_name="源码地址", default="")

    class Meta:
        db_table = "indent"


class Order_New(models.Model):
    '''
    未读的订单数
    '''
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="new_order", verbose_name="用户")

    count = models.IntegerField(default=0, verbose_name="未读订单数")

    class Meta:
        db_table = "order_new"
