# Generated by Django 2.1.7 on 2019-02-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190225_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soft_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='类别名称')),
            ],
            options={
                'db_table': 'soft_category',
            },
        ),
    ]
