# Generated by Django 4.0.3 on 2022-03-28 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_shcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shcode',
            new_name='barecode',
        ),
    ]
