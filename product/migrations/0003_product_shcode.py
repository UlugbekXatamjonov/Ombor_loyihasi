# Generated by Django 4.0.3 on 2022-03-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_kompania_alter_product_mudat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shcode',
            field=models.ImageField(blank=True, null=True, upload_to='Shtrx_codes/%Y/%m/%d/', verbose_name='Mahsulot Shtrx codi'),
        ),
    ]
