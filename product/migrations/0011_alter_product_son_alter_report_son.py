# Generated by Django 4.0.3 on 2022-03-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='son',
            field=models.IntegerField(default=0, verbose_name='Mahsulot soni'),
        ),
        migrations.AlterField(
            model_name='report',
            name='son',
            field=models.IntegerField(default=0, verbose_name='Mahsulot soni'),
        ),
    ]
