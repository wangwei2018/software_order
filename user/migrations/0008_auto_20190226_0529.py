# Generated by Django 2.1.7 on 2019-02-26 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190226_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_new',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_orders', to=settings.AUTH_USER_MODEL, verbose_name='用户id'),
        ),
    ]
