# Generated by Django 3.2 on 2023-05-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20230505_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='timestamp',
            field=models.DateTimeField(default='2023-05-05 11:18:54', verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='isbn',
            field=models.CharField(max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default='2023-05-05 11:18:54', verbose_name='创建时间'),
        ),
    ]
