# Generated by Django 2.1.7 on 2019-02-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_order_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='package_url',
            field=models.CharField(default='', max_length=150, verbose_name='源码地址'),
        ),
    ]
